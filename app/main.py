#!/usr/bin/env python3
"""PicoClaw launcher for Home Assistant Add-on."""

from __future__ import annotations

import http.server
import os
import signal
import socketserver
import subprocess
import sys
import threading
import time
from typing import Optional


class HealthHandler(http.server.BaseHTTPRequestHandler):
    """Simple health endpoint."""

    def do_GET(self) -> None:  # noqa: N802 (required method name)
        if self.path not in {"/", "/health", "/healthz"}:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"ok","service":"picoclaw-addon"}')

    def log_message(self, _format: str, *_args: object) -> None:
        # Keep HTTP endpoint quiet in addon logs.
        return


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def log(level: str, message: str) -> None:
    print(f"[{level}] {message}", flush=True)


def start_health_server(port: int, stop_event: threading.Event) -> threading.Thread:
    def run_server() -> None:
        with ReusableTCPServer(("0.0.0.0", port), HealthHandler) as server:
            server.timeout = 1
            log("INFO", f"Health endpoint listening on 0.0.0.0:{port}")
            while not stop_event.is_set():
                server.handle_request()

    thread = threading.Thread(target=run_server, name="health-server", daemon=True)
    thread.start()
    return thread


def main() -> int:
    command = os.getenv("PICOCLAW_COMMAND", "picoclaw").strip()
    auto_restart = os.getenv("AUTO_RESTART", "true").lower() == "true"
    listen_port = int(os.getenv("LISTEN_PORT", "8099"))

    if not command:
        log("ERROR", "PICOCLAW_COMMAND ist leer.")
        return 2

    stop_event = threading.Event()
    health_thread = start_health_server(listen_port, stop_event)

    should_exit = False

    def handle_signal(signum: int, _frame: Optional[object]) -> None:
        nonlocal should_exit
        should_exit = True
        log("INFO", f"Signal {signum} erhalten, fahre herunter...")

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    exit_code = 0
    while not should_exit:
        log("INFO", f"Starte Prozess: {command}")
        process = subprocess.Popen(command, shell=True)

        while process.poll() is None and not should_exit:
            time.sleep(0.5)

        if should_exit and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)

        exit_code = process.returncode or 0
        log("WARNING", f"PicoClaw-Prozess beendet mit Exit Code {exit_code}")

        if should_exit or not auto_restart:
            break

        log("INFO", "Neustart in 3 Sekunden...")
        time.sleep(3)

    stop_event.set()
    health_thread.join(timeout=2)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
