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
git checkout tags/110.0.5454.1
```

## Native
```config
is_clang = true                                                                                       clang_base_path = "/usr/lib/llvm-14"
is_asan = false
is_debug = true
clang_use_chrome_plugins = false
symbol_level = 1
is_component_build = true
treat_warnings_as_errors = false   
```

## ASAN
```
patch -p1 < asan.patch
```
```config
is_clang = true                                                                                       clang_base_path = "/usr/lib/llvm-14"
is_asan = true
is_debug = true
clang_use_chrome_plugins = false
symbol_level = 1
is_component_build = true
treat_warnings_as_errors = false   
```