#!/bin/sh

cd nginx-1.22.1

sudo ./asan/sbin/nginx
../wrk/wrk -t8 -c100 -d60s --latency http://localhost:80/index.html
sudo ./asan/sbin/nginx -s stop 1>/dev/null 2>&1
sleep 1

sudo ./native/sbin/nginx
../wrk/wrk -t8 -c100 -d60s --latency http://localhost:80/index.html
sudo ./native/sbin/nginx -s stop
sleep 1

sudo LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx 
../wrk/wrk -t8 -c100 -d60s --latency http://localhost:80/index.html
sudo LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc ./camp/sbin/nginx -s stop

sudo ASAN_OPTIONS=use_sigaltstack=0,detect_leaks=0,halt_on_error=0 ./asanmm/sbin/nginx 
../wrk/wrk -t8 -c100 -d60s --latency http://localhost:80/index.html
sudo ASAN_OPTIONS=use_sigaltstack=0,detect_leaks=0,halt_on_error=0 ./asanmm/sbin/nginx -s stop