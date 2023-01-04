## Juliet

```
## fetch code
./build.sh
```
modify `dataset/testcasessupport/io.c`, replace `int globalReturnsTrueOrFalse()` with
```
int globalReturnsTrueOrFalse() { return 1; }
```
to ensure every bug always can be triggered.

```
python3 test_fp.py
python3 test_fn.py
```