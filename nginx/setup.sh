# Set up basic nginx DIR
mkdir -p /usr/local/nginx/logs
mkdir -p /usr/local/nginx/conf
mkdir -p /usr/local/nginx/html
echo "" > /usr/local/nginx/html/index.html
​
# clone wrk
mkdir benmark_nginx
cd benmark_nginx
mkdir log
git clone https://github.com/wg/wrk.git
pushd wrk
make -j`nproc`
popd
​
# clone nginx
git clone --branch release-1.22.1 https://github.com/nginx/nginx.git
pushd nginx
./auto/configure
make CC=/root/CAMP/tools/vcc CXX=/root/CAMP/tools/v++ -j`nproc`
popd
​
# copy nginx basic conf
cp nginx/conf/* /usr/local/nginx/conf/
​
# run nginx
./nginx/objs/nginx
./nginx/objs/nginx -h
ps -ef | grep nginx
​
# run a test through wrk
./wrk/wrk -t1 -c1 -d3s --latency http://localhost:80/index.html
