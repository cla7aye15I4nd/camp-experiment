# camp-experiment

## Softbound

### setup
```bash
## compile llvm (must install python2)
cd softboundcets-llvm-clang34
./configure --enable-optimized
make -j8
## compile runtime
cd softboundcets-lib
make
```