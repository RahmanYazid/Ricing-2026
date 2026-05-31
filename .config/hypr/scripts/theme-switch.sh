#!/bin/bash

WALLPAPER_DIR="$HOME/Pictures/wallpapers"

# Pilih wallpaper dengan rofi
WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) | \
    rofi -dmenu \
         -i \
         -p "Wallpaper" \
         -theme-str 'window {width: 50%;}' \
         -display-column-separator "/" \
         -show-icons)

# Batalkan jika tidak ada yang dipilih
[ -z "$WALLPAPER" ] && exit 0

# Set wallpaper dan generate colorscheme dengan pywal
wal -i "$WALLPAPER" -n

# Simpan path wallpaper terakhir
echo "$WALLPAPER" > "$HOME/.cache/wal/current-wallpaper"

# Set wallpaper via hyprpaper
hyprctl hyprpaper unload all
hyprctl hyprpaper preload "$WALLPAPER"
hyprctl hyprpaper wallpaper ",$WALLPAPER"

# Reload waybar
pkill waybar
waybar &

# Reload rofi colors (pywal sudah generate ~/.config/rofi/colors.rasi)
# Pastikan config rofi import @/home/$USER/.cache/wal/colors-rofi-dark.rasi

# Reload kitty (kirim signal ke semua instance)
pkill -USR1 kitty

# Reload hyprland colors jika pakai pywal-hyprland atau source colors
hyprctl reload

echo "Theme switched to: $WALLPAPER"
