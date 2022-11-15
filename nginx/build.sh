#!/bin/sh

if [ ! -f "nginx-1.22.1.tar.gz" ]; then
    wget http://nginx.org/download/nginx-1.22.1.tar.gz
fi

tar -xvf nginx-1.22.1.tar.gz

cd nginx-1.22.1
./configure --prefix=native
make -j16
make install

./configure --prefix=camp
make -j16 CC=/home/moe/violet/tools/vcc
make install

./configure --prefix=asan
make -j16 CC="clang -fsanitize=address -fsanitize-recover=address -mllvm -asan-stack=0 -mllvm -asan-globals=0"
make install

