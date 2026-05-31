function ganti-wall
    wal -i $argv[1]
    # Update warna Waybar
    pkill -USR2 waybar
    # Restart Dunst
    killall dunst; and dunst &
    # Set wallpaper (swww)
    awww img $argv[1] --transition-type wipe
end
