#!/bin/sh

cd nginx-1.22.1
# sudo ./asan/sbin/nginx -s stop
sudo ./native/sbin/nginx -s stop
sudo LD_LIBRARY_PATH=/root/CAMP/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx -s stop
# sudo ASAN_OPTIONS=use_sigaltstack=0,detect_leaks=0,halt_on_error=0 ./asanmm/sbin/nginx -s stop