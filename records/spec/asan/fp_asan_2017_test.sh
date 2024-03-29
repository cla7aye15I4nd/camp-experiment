#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2017/benchspec/CPU/619.lbm_s/run/run_peak_refspeed_asan.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_asan.0000/lbm_s_peak.asan 2000 reference.dat 0 0 200_200_260_ldc.of

cd /home/moe/cpu2017/benchspec/CPU/638.imagick_s/run/run_peak_refspeed_asan.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_asan.0000/imagick_s_peak.asan -limit disk 0 refspeed_input.tga -resize 817% -rotate -2.76 -shave 540x375 -alpha remove -auto-level -contrast-stretch 1x1% -colorspace Lab -channel R -equalize +channel -colorspace sRGB -define histogram:unique-colors=false -adaptive-blur 0x5 -despeckle -auto-gamma -adaptive-sharpen 55 -enhance -brightness-contrast 10x10 -resize 30% refspeed_output.tga

cd /home/moe/cpu2017/benchspec/CPU/644.nab_s/run/run_peak_refspeed_asan.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_asan.0000/nab_s_peak.asan 3j1n 20140317 220

