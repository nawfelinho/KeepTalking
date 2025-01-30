#!/bin/sh
#script de création du socket can sous linux (version utilisée : Debian 12.9)
sudo apt install can-utils

sudo modprobe can
sudo modprobe can-raw
sudo modprobe can-dev

sudo slcand -o -c -s6 /dev/ttyUSB0 can0
sudo ip link set can0 up type can bitrate 20000
sudo ip link set up can0