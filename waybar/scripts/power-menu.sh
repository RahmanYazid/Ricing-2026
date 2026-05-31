#!/usr/bin/env bash
# ═══════════════════════════════════════════
#  Power Menu — menggunakan wofi atau rofi
#  Tombol: Logout · Lock · Restart · Shutdown
# ═══════════════════════════════════════════

LOGOUT="󰗽 Logout"
LOCK="󰌾 Lock"
RESTART="󰑓 Restart"
SHUTDOWN="󰐥 Shutdown"

# Deteksi apakah menggunakan wofi atau rofi
if command -v wofi &>/dev/null; then
    MENU="wofi --dmenu --style=$HOME/.config/waybar/scripts/power-menu-wofi.css \
        --width=200 --height=220 --location=top_right --yoffset=8 \
        --prompt='' --hide-scroll --no-actions --insensitive --cache-file=/dev/null"
elif command -v rofi &>/dev/null; then
    MENU="rofi -dmenu -theme-str '
        window { width: 200px; location: north east; anchor: north east; y-offset: 8px; }
        listview { lines: 4; }
        element { padding: 8px 16px; }
    ' -p '' -no-fixed-num-lines"
else
    # fallback: bemenu
    MENU="bemenu -l 4 --fn 'JetBrainsMono Nerd Font 12' --nb '#1e1e2e' --nf '#cdd6f4' --sb '#89b4fa' --sf '#1e1e2e'"
fi

CHOICE=$(printf '%s\n' "$LOGOUT" "$LOCK" "$RESTART" "$SHUTDOWN" | eval $MENU)

case "$CHOICE" in
    "$LOGOUT")
        # Hyprland
        if command -v hyprctl &>/dev/null; then
            hyprctl dispatch exit
        # Sway
        elif command -v swaymsg &>/dev/null; then
            swaymsg exit
        else
            loginctl terminate-session "$XDG_SESSION_ID"
        fi
        ;;
    "$LOCK")
        # Coba beberapa locker yang umum
        if command -v hyprlock &>/dev/null; then
            hyprlock
        elif command -v swaylock &>/dev/null; then
            swaylock -f -c 1e1e2e
        elif command -v i3lock &>/dev/null; then
            i3lock -c 1e1e2e
        fi
        ;;
    "$RESTART")
        systemctl reboot
        ;;
    "$SHUTDOWN")
        systemctl poweroff
        ;;
esac
