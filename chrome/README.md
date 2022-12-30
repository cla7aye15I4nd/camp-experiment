# Chrome
## Setup

Follow the [Google Doc](https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md).

```bash
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH:${HOME}/depot_tools"
mkdir ~/chromium && cd ~/chromium
fetch --nohooks chromium
cd src
./build/install-build-deps.sh
gclient runhooks
git checkout tags/111.0.5505.0
```

## Native
```config
clang_base_path = "/usr/lib/llvm-14"
treat_warnings_as_errors = false
clang_use_chrome_plugins = false
is_debug = false
is_asan = false
symbol_level = 1
is_component_build = true 
```

## ASAN
```
patch -p1 < asan.patch
```
```config
clang_base_path = "/usr/lib/llvm-14"
treat_warnings_as_errors = false
clang_use_chrome_plugins = false
is_debug = false
is_asan = true
symbol_level = 1
is_component_build = true
```


## CAMP
```
patch -p1 < camp.patch
```
in `src/third_party/boringssl/src/crypto/mem.c:OPENSSL_free:188`, replace code between `#else` and `#elseif` with:
```c
(void)sdallocx;
free(ptr);
```

```config
clang_base_path = "/usr/lib/llvm-14"
treat_warnings_as_errors = false
clang_use_chrome_plugins = false
is_debug = false
is_camp = true
symbol_level = 1
is_component_build = true
```