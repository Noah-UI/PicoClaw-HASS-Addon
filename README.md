# PicoClaw Home Assistant Add-on

Dieses Repository enthält ein vollständiges Supervisor Add-on, um `picoclaw` in Home Assistant auszuführen.

## Features

- Startet einen konfigurierbaren PicoClaw-Prozess
- Optionaler Auto-Restart bei Absturz
- Health-Endpoint auf konfigurierbarem Port (`/healthz`)
- Konfiguration direkt über Home Assistant Add-on UI

## Konfiguration

| Option | Typ | Standard | Beschreibung |
|---|---|---:|---|
| `log_level` | string | `info` | Log-Level für das Add-on |
| `listen_port` | port | `8099` | Port für den Health-Endpoint |
| `picoclaw_command` | string | `picoclaw` | Kommando, das gestartet wird |
| `auto_restart` | bool | `true` | Neustart bei Prozessende |

## Beispiel

```yaml
log_level: info
listen_port: 8099
picoclaw_command: "picoclaw --config /config/picoclaw/config.yaml"
auto_restart: true
```

## Nutzung

1. Repository als Add-on-Store in Home Assistant hinzufügen.
2. Add-on `PicoClaw` installieren.
3. Konfiguration setzen.
4. Starten und Logs prüfen.
