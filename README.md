# Ricing-2026

Dotfiles untuk setup Arch Linux + Hyprland dengan tema dinamis berbasis pywal.

---

## Dependensi

```bash
yay -S hyprland waybar rofi dunst kitty fish python-pywal awww neovim
```

---

## Instalasi

Clone repo:

```bash
git clone git@github.com:RahmanYazid/Ricing-2026.git ~/dotfiles
```

Copy config ke `~/.config`:

```bash
cp -r ~/dotfiles/hypr ~/.config/
cp -r ~/dotfiles/waybar ~/.config/
cp -r ~/dotfiles/rofi ~/.config/
cp -r ~/dotfiles/dunst ~/.config/
cp -r ~/dotfiles/kitty ~/.config/
cp -r ~/dotfiles/fish ~/.config/
cp -r ~/dotfiles/nvim ~/.config/
```

Chmod script:

```bash
chmod +x ~/.config/hypr/scripts/theme-switch.sh
```

Setup pywal dengan wallpaper pilihan:

```bash
wal -i /path/to/wallpaper.jpg
```

---

## Theme Switching

Script `theme-switch.sh` mengganti wallpaper sekaligus update color scheme via pywal dan awww-daemon. Bisa dijalankan manual atau lewat keybind di `hyprland.conf`.

---

## Struktur

```
dotfiles/
├── dunst/
├── fish/
├── hypr/
├── kitty/
├── nvim/
├── rofi/
└── waybar/
```

---

## Catatan

- Neovim menggunakan LazyVim.
- Semua warna di-generate otomatis oleh pywal dari wallpaper aktif.
- Wallpaper picker tersedia via rofi.
- Set fish sebagai default shell: `chsh -s /usr/bin/fish`
