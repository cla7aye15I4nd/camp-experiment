import os
import time
import socket
import subprocess

def main():
    executables = []
    false_positive = []
    false_negative = []

    with open("dump", 'w') as f:
        f.write('100 ' * 0x1000)

    for cwe in ['CWE761_Free_Pointer_Not_at_Start_of_Buffer']:
        for path, dirs, files in os.walk(f'test/C/testcases/{cwe}'):
            for file in files:
                if file.endswith('.out'):
                    executables.append(os.path.join(path, file))
        
    for idx, executable in enumerate(sorted(executables)):
        print(f"Running {idx}.{executable}")
        
        with open('dump') as f:
            p = subprocess.Popen(
                [f'{executable}'], 
                env={'LD_LIBRARY_PATH': '/home/moe/violet/build/src/safe_tcmalloc/tcmalloc'},
                stdin=f,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        p.wait()

        stdout, stderr = p.communicate()
        assert b'Calling good' in stdout
        if b'Finished good' not in stdout:
            print (f"FP: {executable}")
            false_positive.append(executable)
        
        assert b'Calling bad' in stdout
        if b'Finished bad' in stdout:
            print (f"FN: {executable}")
            false_negative.append(executable)
    
    for fn in false_negative:
        print(f"FN: {fn}")
    for fp in false_positive:
        print(f"FP: {fp}")
    
    print(f"FN/FP/ALL {len(false_negative)}/{len(false_positive)}/{len(executables)}")

if __name__ == "__main__":
    main()

# cd test/C && make CC=/home/moe/violet/tools/vcc CPP=/home/moe/violet/tools/v++ individuals -j16 && cd -
# find . | grep "\.out$" | xargs rm