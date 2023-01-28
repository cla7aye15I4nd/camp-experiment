#!/bin/sh

cd nginx-1.22.1
sudo ./asan/sbin/nginx -s stop
sudo ./native/sbin/nginx -s stop
sudo LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx -s stop
