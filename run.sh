#!/usr/bin/with-contenv bashio
set -euo pipefail

LOG_LEVEL="$(bashio::config 'log_level')"
LISTEN_PORT="$(bashio::config 'listen_port')"
TERMINAL_PORT="$(bashio::config 'terminal_port')"
TERMINAL_SHELL="$(bashio::config 'terminal_shell')"
TERMINAL_WORKDIR="$(bashio::config 'terminal_workdir')"
PICOCLAW_COMMAND="$(bashio::config 'picoclaw_command')"
AUTO_RESTART="$(bashio::config 'auto_restart')"

bashio::log.info "Starte PicoClaw Add-on"
bashio::log.info "Log Level: ${LOG_LEVEL}"
bashio::log.info "Health Port: ${LISTEN_PORT}"
bashio::log.info "Terminal Port: ${TERMINAL_PORT}"
bashio::log.info "Command: ${PICOCLAW_COMMAND}"
bashio::log.info "Auto Restart: ${AUTO_RESTART}"

mkdir -p "${TERMINAL_WORKDIR}"
cd "${TERMINAL_WORKDIR}"

bashio::log.info "Starte eingebautes Web-Terminal (ttyd)"
ttyd \
  --writable \
  --port "${TERMINAL_PORT}" \
  --check-origin=false \
  "${TERMINAL_SHELL}" &

export LOG_LEVEL LISTEN_PORT PICOCLAW_COMMAND AUTO_RESTART
exec python3 /app/main.py
