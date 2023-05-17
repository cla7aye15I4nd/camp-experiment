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
git checkout tags/89.0.4389.128
```

## Native
```config
clang_base_path = "/usr/lib/llvm-12/"
clang_use_chrome_plugins = false
is_debug = false
is_component_build = true
symbol_level = 1
treat_warnings_as_errors = false
enable_nacl = false
```

## ASAN
```
patch -p1 < final.patch
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
patch -p1 < final.patch
```

```config
clang_base_path = "/usr/lib/llvm-12/"
clang_use_chrome_plugins = false
is_camp = true
is_debug = false
is_component_build = true
symbol_level = 1
treat_warnings_as_errors = false

enable_nacl = false
```

## Compile V8 only
```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH:${HOME}/depot_tools"
mkdir v8 && cd v8
fetch v8	# download v8 source code
./build/install-build-deps.sh
gclient sync
# git reset --hard VERSION
patch -p1 < camp.patch # if it fails, we can modify it manually
gn gen out/camp
# set args as camp 
# may set `is_debug = true` and `v8_optimized_debug = false` for debugging
gn args out/camp	
autoninja -C out/camp/ d8
```
