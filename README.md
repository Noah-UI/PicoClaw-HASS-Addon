# PicoClaw Home Assistant Add-on

Dieses Repository enthält ein Supervisor Add-on, um `picoclaw` in Home Assistant auszuführen.

## Features

- Startet einen konfigurierbaren PicoClaw-Prozess
- Optionaler Auto-Restart bei Absturz
- Health-Endpoint auf konfigurierbarem Port (`/healthz`)
- Eingebautes Web-Terminal (Ingress) für Erstkonfiguration/Onboarding
- Konfiguration direkt über Home Assistant Add-on UI

## Konfiguration

| Option | Typ | Standard | Beschreibung |
|---|---|---:|---|
| `log_level` | string | `info` | Log-Level für das Add-on |
| `listen_port` | port | `8099` | Port für den Health-Endpoint |
| `terminal_port` | port | `7681` | Interner Port des eingebauten Web-Terminals |
| `terminal_shell` | string | `/bin/bash` | Shell für das Web-Terminal |
| `terminal_workdir` | string | `/config` | Startverzeichnis im Web-Terminal |
| `picoclaw_command` | string | `picoclaw` | Kommando, das gestartet wird |
| `auto_restart` | bool | `true` | Neustart bei Prozessende |

## First-time setup (wie OpenClaw-Flow)

1. Add-on installieren und starten.
2. Auf **Öffnen (Open Web UI)** klicken.
3. Du siehst das eingebettete Terminal.
4. Im Terminal z. B. ausführen:

```bash
mkdir -p /config/picoclaw
nano /config/picoclaw/config.yaml
```

5. Danach `picoclaw_command` auf die gewünschte Config setzen, z. B.:

```yaml
picoclaw_command: "picoclaw --config /config/picoclaw/config.yaml"
```

## Beispiel

```yaml
log_level: info
listen_port: 8099
terminal_port: 7681
terminal_shell: /bin/bash
terminal_workdir: /config
picoclaw_command: "picoclaw --config /config/picoclaw/config.yaml"
auto_restart: true
```
