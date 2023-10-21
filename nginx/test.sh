#!/bin/sh

cd nginx-1.22.1

sudo ./asan/sbin/nginx
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../asan.txt
sudo ./asan/sbin/nginx -s stop
sleep 1

sudo ./native/sbin/nginx
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../native.txt
sudo ./native/sbin/nginx -s stop
sleep 1

sudo LD_LIBRARY_PATH=/root/CAMP/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../camp.txt
sudo LD_LIBRARY_PATH=/root/CAMP/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx -s stop
