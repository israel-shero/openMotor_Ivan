#!/bin/zsh
cd "$(dirname "$0")"
if [[ -x ".venv/bin/python" ]]; then
  exec .venv/bin/python main.py "$@"
fi

export QT_PLUGIN_PATH="/opt/anaconda3/plugins"
export QT_QPA_FONTDIR="/System/Library/Fonts"
unset QT_QPA_PLATFORM
exec /opt/anaconda3/bin/pythonw main.py "$@"
