# PicoClaw Home Assistant Add-on

Dieses Repository enthält ein Home-Assistant-Supervisor-Add-on, um `picoclaw` kontrolliert auszuführen.

## Features

- Startet einen konfigurierbaren PicoClaw-Prozess
- Optionale Auto-Restart-Strategie bei Prozessende
- Health-Endpoint (`/`, `/health`, `/healthz`) mit Prozessstatus
- Log-Level direkt über Add-on-Konfiguration steuerbar

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

## Logs & Betrieb

- Add-on-Logs in Home Assistant: **Einstellungen → Add-ons → PicoClaw → Protokoll**
- `debug`/`trace` hilft bei Startproblemen
- Health-Status:
  - `200`: PicoClaw läuft
  - `503`: Prozess läuft nicht

## Best Practices, die hier angewendet werden

- Konfiguration über `options`/`schema` statt Hardcoding
- Sauberes Signal-Handling für Supervisor Stop/Restart
- Gesundheitsprüfung getrennt vom Hauptprozess
- Vermeidung von `shell=True` beim Prozessstart
- Multi-Arch Build-Konfiguration für HA-typische Plattformen

## Nutzung

1. Repository als Add-on-Store in Home Assistant hinzufügen.
2. Add-on `PicoClaw` installieren.
3. Konfiguration setzen.
4. Starten und Logs prüfen.
