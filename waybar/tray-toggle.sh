#!/bin/bash
TOGGLE_FILE="/tmp/tray-visible"

if [ -f "$TOGGLE_FILE" ]; then
  rm "$TOGGLE_FILE"
  pkill -SIGUSR1 waybar # trigger update
else
  touch "$TOGGLE_FILE"
  pkill -SIGUSR1 waybar
fi
