import subprocess
import time
import numpy as np

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

websites = [
    "http://www.google.com",
    "http://www.facebook.com",
    "http://www.amazon.com",
    "http://www.openai.com",
    "http://www.twitter.com",
    "http://www.gmail.com",
    "http://www.youtube.com",
    "http://www.wikipedia.org"
]

camp_overheads = []
asan_overheads = []

for website in websites:
    print(f"Accessing {website}...")

    start_time = time.time()
    subprocess.run(["/home/moe/chrome-with-camp/src/out/native/chrome", "--disable-sync", "--disable-gpu",
                   "--headless", "--screenshot", "--no-sandbox", website], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end_time = time.time()
    native_time = int((end_time - start_time) * 1000)

    start_time = time.time()
    subprocess.run(["/home/moe/chrome-with-camp/src/out/camp/chrome", "--disable-sync", "--disable-gpu",
                   "--headless", "--screenshot", "--no-sandbox", website], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   env={"LD_LIBRARY_PATH": "/home/moe/violet/build/src/safe_tcmalloc/tcmalloc/"})
    end_time = time.time()
    camp_time = int((end_time - start_time) * 1000)

    start_time = time.time()
    subprocess.run(["/home/moe/chrome-with-camp/src/out/asan/chrome", "--disable-sync", "--disable-gpu",
                   "--headless", "--screenshot", "--no-sandbox", website], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env={"ASAN_OPTIONS": "detect_odr_violation=0"})
    end_time = time.time()
    asan_time = int((end_time - start_time) * 1000)

    # Calculate the overhead in xx.xx% format
    camp_overhead = (camp_time - native_time) * 100 / native_time
    asan_overhead = (asan_time - native_time) * 100 / native_time

    print(f"Native: {native_time} ms")
    print(f"Camp: {camp_time} ms, {camp_overhead:.2f}%")
    print(f"ASAN: {asan_time} ms, {asan_overhead:.2f}%\n")

    camp_overheads.append(camp_overhead)
    asan_overheads.append(asan_overhead)

print(f"Geometric mean of CAMP overhead: {geo_mean(camp_overheads):.2f}%")
print(f"Geometric mean of ASAN overhead: {geo_mean(asan_overheads):.2f}%")