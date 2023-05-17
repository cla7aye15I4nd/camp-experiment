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
clang_base_path = "/usr/lib/llvm-12/"
clang_use_chrome_plugins = false
is_asan = true
is_debug = false
is_component_build = true
symbol_level = 1
treat_warnings_as_errors = false

enable_nacl = false
```


## CAMP
```
patch -p1 < final.patch
```

Fix the `src/third_party/boringssl/src/crypto/mem.c`:

```diff
diff --git a/crypto/mem.c b/crypto/mem.c
index 0491f150b..1c2b02a16 100644
--- a/crypto/mem.c
+++ b/crypto/mem.c
@@ -112,11 +112,11 @@ WEAK_SYMBOL_FUNC(void, OPENSSL_memory_free, (void *ptr));
 WEAK_SYMBOL_FUNC(size_t, OPENSSL_memory_get_size, (void *ptr));
 
 void *OPENSSL_malloc(size_t size) {
-  if (OPENSSL_memory_alloc != NULL) {
-    assert(OPENSSL_memory_free != NULL);
-    assert(OPENSSL_memory_get_size != NULL);
-    return OPENSSL_memory_alloc(size);
-  }
+  // if (OPENSSL_memory_alloc != NULL) {
+  //   assert(OPENSSL_memory_free != NULL);
+  //   assert(OPENSSL_memory_get_size != NULL);
+  //   return OPENSSL_memory_alloc(size);
+  // }
 
   if (size + OPENSSL_MALLOC_PREFIX < size) {
     return NULL;
 void *OPENSSL_malloc(size_t size) {
-  if (OPENSSL_memory_alloc != NULL) {
-    assert(OPENSSL_memory_free != NULL);
-    assert(OPENSSL_memory_get_size != NULL);
-    return OPENSSL_memory_alloc(size);
-  }
+  // if (OPENSSL_memory_alloc != NULL) {
+  //   assert(OPENSSL_memory_free != NULL);
+  //   assert(OPENSSL_memory_get_size != NULL);
+  //   return OPENSSL_memory_alloc(size);
+  // }
 
   if (size + OPENSSL_MALLOC_PREFIX < size) {
     return NULL;
@@ -138,21 +138,21 @@ void OPENSSL_free(void *orig_ptr) {
     return;
   }
 
-  if (OPENSSL_memory_free != NULL) {
-    OPENSSL_memory_free(orig_ptr);
-    return;
-  }
+  // if (OPENSSL_memory_free != NULL) {
+  //   OPENSSL_memory_free(orig_ptr);
+  //   return;
+  // }
 
   void *ptr = ((uint8_t *)orig_ptr) - OPENSSL_MALLOC_PREFIX;
   __asan_unpoison_memory_region(ptr, OPENSSL_MALLOC_PREFIX);
 
   size_t size = *(size_t *)ptr;
   OPENSSL_cleanse(ptr, size + OPENSSL_MALLOC_PREFIX);
-  if (sdallocx) {
-    sdallocx(ptr, size + OPENSSL_MALLOC_PREFIX, 0 /* flags */);
-  } else {
+  // if (sdallocx) {
+  // sdallocx(ptr, size + OPENSSL_MALLOC_PREFIX, 0 /* flags */);
+  // } else {
     free(ptr);
-  }
+  // }
 }
 
 void *OPENSSL_realloc(void *orig_ptr, size_t new_size) {
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
