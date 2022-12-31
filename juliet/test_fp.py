import os
import socket
import subprocess

goodans = {}
goodout = {}

for path, _, filelist in os.walk('dataset'):
    for file in filelist:
        if file.endswith('goodans'):
            goodans[file.split('.')[0]] = os.path.join(path, file)
        if file.endswith('goodout'):
            goodout[file.split('.')[0]] = os.path.join(path, file)

with open("dump", 'w') as f:
    for i in range(1000):
        f.write(f'{i}\n')

assert len(goodans) == len(goodout)

for idx, (key, path_ans) in enumerate(goodans.items()):
    print(f'[{idx}/{len(goodans)}]{path_ans}{" " * (150 - len(path_ans))}', end='\r')

    path_out = goodout[key]
    with open("dump") as f:
        p = subprocess.Popen(
                [f'{path_ans}'], 
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        if 'listen' in key:
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversocket.bind(("127.0.0.1", 27015))
            try:
                clientsocket, addr = serversocket.accept()      
                clientsocket.send(b'0\n')
                clientsocket.close()
            except:
                pass

        ans, _ = p.communicate()

    with open("dump") as f:
        p = subprocess.Popen(
                [f'{path_out}'], 
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc'},
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        if 'listen' in key:
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversocket.bind(("127.0.0.1", 27015))
            try:
                clientsocket, addr = serversocket.accept()      
                clientsocket.send(b'0\n')
                clientsocket.close()
            except:
                pass

        out, _ = p.communicate()

    if ans != out:
        print("\n[FAIL]", key)
        print(f"[OUT] {repr(out)}")
        print(f"[ANS] {repr(ans)}")

print("\n[FINISHED]")