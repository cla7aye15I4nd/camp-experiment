#!/bin/sh

cd httpd-2.4.54

sudo ./asan/bin/apachectl -k start
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../asan.txt
sudo ./asan/bin/apachectl -k stop
sleep 1

sudo ./native/bin/apachectl -k start
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../native.txt
sudo ./native/bin/apachectl -k stop
sleep 1

sudo LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc ./camp/bin/apachectl -k start
ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../camp.txt
sudo LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc ./camp/bin/apachectl -k stop
