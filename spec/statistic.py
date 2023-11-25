import os
import sys

def fetch_reslut(tag):
    file_list = [
        f'{tag}_2006_c.txt',
        f'{tag}_2006_cpp.txt',
        f'{tag}_2017_int.txt',
        f'{tag}_2017_fp.txt',
    ]

    result = []
    last = None
    for file in file_list:
        with open(file) as f:
            text = f.read().splitlines()
            while text:
                name = text.pop(0).split()[1].split('/')[2].split('_')[0]
                if '2017' in file:
                    name = name + '_s'

                time = int(text.pop(0).split()[2])
                cputime = int(text.pop(0).split()[3])
                memory = int(text.pop(0).split()[2])
                exit = text.pop(0)

                if name == last:
                    result[-1][1] += time
                    result[-1][2] += cputime
                    result[-1][3] += memory
                else:
                    last = name
                    result.append([name, time, cputime, memory])

    return result

native = fetch_reslut('native')
camp = fetch_reslut('camp')

print('CPU2017')

time_geo_mean = 1
mem_geo_mean = 1
count = 0
for i in range(len(native)):
    name = native[i][0]
    if not name.endswith('_s') or name == 'omnetpp_s': ## skip
        continue
    
    count += 1
        
    time_overhead = (camp[i][1] - native[i][1]) / native[i][1] * 100
    mem_overhead = (camp[i][3] - native[i][3]) / native[i][3] * 100
    
    print(f'{name}{" " * (12 - len(name))} {time_overhead:.2f}% \t{mem_overhead:.2f}%')
    time_geo_mean *= time_overhead / 100
    mem_geo_mean *= mem_overhead / 100 + 1
    
time_geo_mean = (time_geo_mean ** (1 / count)) * 100
mem_geo_mean = (mem_geo_mean ** (1 / count) - 1) * 100

print(f'Geomean      {time_geo_mean:.2f}% \t{mem_geo_mean:.2f}%')


print('CPU2006')
time_geo_mean = 1
mem_geo_mean = 1
count = 0
for i in range(len(native)):
    name = native[i][0]
    if name.endswith('_s') or name == 'dealII': 
        continue
    
    count += 1
        
    time_overhead = (camp[i][1] - native[i][1]) / native[i][1] * 100
    mem_overhead = (camp[i][3] - native[i][3]) / native[i][3] * 100
    
    print(f'{name}{" " * (12 - len(name))} {time_overhead:.2f}% \t{mem_overhead:.2f}%')
    time_geo_mean *= time_overhead / 100
    mem_geo_mean *= mem_overhead / 100 + 1
    
time_geo_mean = (time_geo_mean ** (1 / count)) * 100
mem_geo_mean = (mem_geo_mean ** (1 / count) - 1) * 100

print(f'Geomean      {time_geo_mean:.2f}% \t{mem_geo_mean:.2f}%')
