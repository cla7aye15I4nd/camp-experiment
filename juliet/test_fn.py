import os
import string
import socket
import subprocess
import time
import threading

badout = {
    'CWE122_Heap_Based_Buffer_Overflow': [],
    'CWE124_Buffer_Underwrite': [],
    'CWE126_Buffer_Overread': [],
    'CWE127_Buffer_Underread': [],
    'CWE415_Double_Free': [],
    'CWE416_Use_After_Free': [],
    'CWE476_NULL_Pointer_Dereference': [],
    'CWE761_Free_Pointer_Not_at_Start_of_Buffer': [],
}

for path, _, filelist in os.walk('dataset'):
    for file in filelist:
        if file.endswith('badout'):
            filepath = os.path.join(path, file)
            for vtype in badout.keys():
                if vtype in filepath:
                    badout[vtype].append(filepath)

for key, value in badout.items():
    print(f'{key} : {len(value)}')

with open("/tmp/file.txt", 'w') as f:
    f.write(string.ascii_letters)

def common_setup(path):
    def setup_listen():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    s.bind(('127.0.0.1', 27015))
                    break
                except:
                    pass            
            s.listen()
            try:
                c, _ = s.accept()      
                c.send(b'AAAS\n')
                c.close()
            except:
                pass  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.bind(('127.0.0.1', 27015))
                break
            except:
                pass

    with open("/tmp/file.txt") as f:
        if 'listen' in path:
            p = subprocess.Popen(
                [f'{path}'],
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc', 'ADD': 'AAAS'},
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            time.sleep(0.5)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect(("127.0.0.1", 27015))
                    s.sendall(b'AAS\n')
                except:
                    pass
        elif 'connect' in path:
            th = threading.Thread(target=setup_listen)
            th.start()
            p = subprocess.Popen(
                [f'{path}'],
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc', 'ADD': 'AAAS'},
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            th.join()
        else:
            p = subprocess.Popen(
                [f'{path}'],
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc', 'ADD': 'AAAS'},
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        out, err = p.communicate()
    
    return p.returncode, out, err

def test_must_be_detected(vtype):
    for idx, path in enumerate(badout[vtype]):
        name = path[len("dataset/testcases/"):-len(".badout")]
        print(f'[{idx+1}/{len(badout[vtype])}]{name}{" " * (110 - len(name))}', end='\r')

        ## These programs only have good parts, they do not have bugs.
        whitelist = [
            'dataset/testcases/CWE415_Double_Free/s02/CWE415_Double_Free__no_assignment_op_01_good1.badout',
            'dataset/testcases/CWE415_Double_Free/s02/CWE415_Double_Free__no_copy_const_01_good1.badout',
        ]

        if path in whitelist:
            continue
        
        ## Some program's bugs are triggerd randomly
        for _ in range(50):
            exitcode, out, err = common_setup(path)
            if b'double/invalid free detected' in err:
                break
            time.sleep(1)
        else:
            print('[FAIL]', path)
    print(f'\n[FINISHED] {vtype}')

def test_must_be_detected_with_gdb(vtype, gdbscript='uaf.gdb'):
    for idx, path in enumerate(badout[vtype]):
        name = path[len("dataset/testcases/"):-len(".badout")]
        print(f'[{idx+1}/{len(badout[vtype])}]{name}{" " * (110 - len(name))}', end='\r')
        
        ## I have manually checked the two cases
        whitelist = [
            'dataset/testcases/CWE416_Use_After_Free/CWE416_Use_After_Free__operator_equals_01_good1.badout',
            'dataset/testcases/CWE416_Use_After_Free/CWE416_Use_After_Free__operator_equals_01_bad.badout'
        ]

        if path in whitelist: continue

        for _ in range(50):
            p = subprocess.Popen(
                ['gdb', '--batch', '--command', gdbscript, f'{path}'],
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc'},
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            
            out, err = p.communicate()
            if b'UAF detected' in out:
                break
            time.sleep(0.5)
        else:
            print('[FAIL]', path)
    
    print(f'\n[FINISHED] {vtype}')

def test_heap_overflow(vtype):
    fail = 0
    ignore = 0
    for idx, path in enumerate(badout[vtype]):
        name = path[len("dataset/testcases/"):-len(".badout")]
        print(f'[{idx}/{len(badout[vtype])}]{name}{" " * (110 - len(name))}', end='\r')

        exitcode, out, err = common_setup(path)
        if b'OOB detected' in err:
            continue
        if exitcode == 0:
            bad_exitecode, bad_out, bad_err = common_setup(path[:-len('out')] + 'ans')
            if bad_exitecode == 0:
                ignore += 1
            continue

        fail += 1
        print('[FAIL]', path)

    print(f'\n[FAIL/IGNORE/ALL][{fail}/{ignore}/{len(badout[vtype])}] {vtype}')

# test_heap_overflow("CWE122_Heap_Based_Buffer_Overflow")

## [TESTED]
# test_must_be_detected('CWE415_Double_Free')

## [TESTED]
# test_must_be_detected_with_gdb('CWE416_Use_After_Free')

## [TESTED]
# test_must_be_detected_with_gdb('CWE476_NULL_Pointer_Dereference', gdbscript='null.gdb')

## [TESTED]
# test_must_be_detected('CWE761_Free_Pointer_Not_at_Start_of_Buffer')