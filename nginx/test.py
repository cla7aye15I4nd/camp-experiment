import subprocess
import os
import time
import sys

env_map = {
    'asan': {'ASN_OPTIONS': 'halt_on_error=0'},
    'camp': {'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc'},
    'native': {},
}

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()

def test_nginx(tag):
    start_nginx = subprocess.Popen(
        [f'./{tag}/sbin/nginx'], 
        env=env_map[tag],
        cwd='/home/moe/camp-experiment/nginx/nginx-1.22.1')

    start_nginx.communicate()

    # ab -n 10000000 -c 100 http://0.0.0.0/index.html > ../asan.txt
    benchmark = subprocess.Popen(
        ['ab', '-n', '10000000', '-c', '100', 'http://0.0.0.0/index.html'],
        stdout=subprocess.PIPE)

    proc = os.popen("ps -aux | grep nginx | grep worker").read().split()[1]
    
    time.sleep(0.5)

    vms = []
    while benchmark.poll() is None:
        with open(f'/proc/{proc}/status') as f:
            for line in f.read().splitlines():
                if line.startswith('VmRSS'):
                    eprint(line.strip())
                    vms.append(int(line.split()[1]))
        time.sleep(1)
        
    out, _ = benchmark.communicate()
    eprint(out.decode())

    # with open(f'../{tag}_time.txt', 'w') as f:
    #     f.write(out.decode())
    # with open(f'../{tag}_vm.txt', 'w') as f:
    #     f.write(str(vms))
        
    stop_nginx = subprocess.Popen(
        [f'./{tag}/sbin/nginx', '-s', 'stop'],
        env=env_map[tag],
        cwd='/home/moe/camp-experiment/nginx/nginx-1.22.1')
    stop_nginx.communicate()

    time.sleep(1)

    for line in out.decode().splitlines():
        if line.startswith('Time taken for tests:'):
            return line.split()[4], vms[-1]

for tag in ['camp', 'asan', 'native']:
    t, m = test_nginx(tag)
    eprint(f'{tag}: {t}s {m}kb')