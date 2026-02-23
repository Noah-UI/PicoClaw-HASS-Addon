#!/usr/bin/with-contenv bashio
set -euo pipefail

LOG_LEVEL="$(bashio::config 'log_level')"
LISTEN_PORT="$(bashio::config 'listen_port')"
PICOCLAW_COMMAND="$(bashio::config 'picoclaw_command')"
AUTO_RESTART="$(bashio::config 'auto_restart')"

bashio::log.level "${LOG_LEVEL}"
bashio::log.info "Starte PicoClaw Add-on"
bashio::log.debug "Health Port: ${LISTEN_PORT}"
bashio::log.debug "Auto Restart: ${AUTO_RESTART}"

if bashio::string.is_empty "${PICOCLAW_COMMAND}"; then
  bashio::log.fatal "Konfiguration 'picoclaw_command' darf nicht leer sein."
  exit 1
fi

export LOG_LEVEL LISTEN_PORT PICOCLAW_COMMAND AUTO_RESTART
exec python3 /app/main.py
