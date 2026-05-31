#!/bin/sh

# Buat config sementara
config_file="/tmp/cava_config_waybar"
echo "[general]
bars = 12
sleep = 0.7

[output]
method = raw
raw_target = /dev/stdout
data_format = ascii
ascii_max_range = 7" > $config_file

# Jalankan cava
# 1. 'tr -d ";"' menghapus semua titik koma agar sisa angka saja
# 2. 'sed' mengubah angka tersebut menjadi bar
cava -p $config_file | stdbuf -o0 tr -d ';' | stdbuf -o0 sed -u 's/0/ /g; s/1/▂/g; s/2/▃/g; s/3/▄/g; s/4/▅/g; s/5/▆/g; s/6/▇/g; s/7/█/g'
