#!/bin/sh

if [ ! -f "httpd-2.4.54.tar.gz" ]; then
    wget https://dlcdn.apache.org/httpd/httpd-2.4.54.tar.gz
fi

if [ ! -f "apr-1.7.0.tar.gz" ]; then
    wget https://dlcdn.apache.org//apr/apr-1.7.0.tar.gz
fi

if [ ! -f "apr-util-1.6.1.tar.gz" ]; then
    wget https://dlcdn.apache.org//apr/apr-util-1.6.1.tar.gz
fi

tar -xvf httpd-2.4.54.tar.gz
tar -xvf apr-1.7.0.tar.gz
tar -xvf apr-util-1.6.1.tar.gz

mv apr-util-1.6.1 httpd-2.4.54/srclib/apr-util
mv apr-1.7.0      httpd-2.4.54/srclib/apr

cd httpd-2.4.54
make clean
./configure --prefix=/home/moe/camp-experiment/apache/httpd-2.4.54/native -with-included-apr
make -j16
make install
echo "ServerName localhost" >> native/conf/httpd.conf

make clean
./configure --prefix=/home/moe/camp-experiment/apache/httpd-2.4.54/camp -with-included-apr
LD_LIBRARY_PATH=/home/moe/violet/build/src/safe_tcmalloc/tcmalloc make -j16 CC=/home/moe/violet/tools/vcc
make install
echo "ServerName localhost" >> camp/conf/httpd.conf

make clean
./configure --prefix=/home/moe/camp-experiment/apache/httpd-2.4.54/asan -with-included-apr
make -j16 CC="clang -fsanitize=address -fsanitize-recover=address -mllvm -asan-stack=0 -mllvm -asan-globals=0"
make install
echo "ServerName localhost" >> asan/conf/httpd.conf
