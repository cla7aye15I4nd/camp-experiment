import os
import string
import socket
import subprocess
import time
import threading

buffer_underread_whitelist = [
    ## Buffer UnderRead Whitelist
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_01.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_02.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_03.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_04.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_05.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_06.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_07.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_08.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_09.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_10.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_11.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_12.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_13.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_14.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_15.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_16.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_17.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_18.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_21.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_22.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_31.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_32.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_33.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_34.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_41.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_42.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_43.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_44.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_45.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_51.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_52.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_53.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_54.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_61.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_62.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_63.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_64.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_65.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_66.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_67.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_68.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_72.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_73.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_74.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_81.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_82.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_83.badout',
    'dataset/testcases/CWE127_Buffer_Underread/s02/CWE127_Buffer_Underread__CWE839_rand_84.badout',
]

buffer_overread_whitelist = [
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_01.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_02.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_03.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_04.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_05.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_06.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_07.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_08.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_09.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_10.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_11.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_12.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_13.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_14.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_15.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_16.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_17.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_18.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_21.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_22.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_31.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_32.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_33.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_34.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_41.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_42.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_43.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_44.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_45.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_51.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_52.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_53.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_54.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_61.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_62.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_63.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_64.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_65.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_66.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_67.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_68.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_72.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_73.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_74.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_81.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_82.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_83.badout',
    'dataset/testcases/CWE126_Buffer_Overread/s01/CWE126_Buffer_Overread__CWE129_rand_84.badout',
]

buffer_underwrite_whitelist = [
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_01.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_02.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_03.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_04.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_05.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_06.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_07.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_08.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_09.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_10.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_11.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_12.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_13.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_14.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_15.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_16.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_17.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_18.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_21.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_22.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_31.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_32.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_33.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_34.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_41.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_42.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_43.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_44.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_45.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_51.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_52.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_53.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_54.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_61.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_62.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_63.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_64.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_65.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_66.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_67.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_68.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_72.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_73.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_74.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_81.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_82.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_83.badout',
    'dataset/testcases/CWE124_Buffer_Underwrite/s02/CWE124_Buffer_Underwrite__CWE839_rand_84.badout',
]

stack_oob_whitelist = buffer_underread_whitelist + buffer_overread_whitelist + buffer_underwrite_whitelist

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
        print(f'[{idx + 1}/{len(badout[vtype])}]{name}{" " * (110 - len(name))}', end='\r')
        # if 'connect' in path or 'listen' in path:
        #     continue
        
        if path in stack_oob_whitelist:
            ignore += 1
            continue

        exitcode, out, err = common_setup(path)
        if b'OOB detected' in err:
            continue
        if exitcode == 0:
            bad_exitecode, bad_out, bad_err = common_setup(path[:-len('out')] + 'ans')
            if bad_exitecode == 0:
                # print('[IGNORE]', path)
                ignore += 1
            continue

        fail += 1
        print('[FAIL]', path)

    print(f'\n[FAIL/IGNORE/ALL][{fail}/{ignore}/{len(badout[vtype])}] {vtype}')

## [UNTESTED]
# test_heap_overflow("CWE122_Heap_Based_Buffer_Overflow")

## [TESTED]
test_heap_overflow("CWE124_Buffer_Underwrite")

## [TESTED]
test_heap_overflow("CWE126_Buffer_Overread")

## [TESTED]
test_heap_overflow("CWE127_Buffer_Underread")

## [TESTED]
# test_must_be_detected('CWE415_Double_Free')

## [TESTED]
# test_must_be_detected_with_gdb('CWE416_Use_After_Free')

## [TESTED]
# test_must_be_detected_with_gdb('CWE476_NULL_Pointer_Dereference', gdbscript='null.gdb')

## [TESTED]
# test_must_be_detected('CWE761_Free_Pointer_Not_at_Start_of_Buffer')