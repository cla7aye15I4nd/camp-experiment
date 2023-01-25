tag = 'valgrind'

file_list = [
    f'{tag}_2006_c.txt',
    f'{tag}_2006_cpp.txt',
    f'{tag}_2017_int.txt',
    # f'{tag}_2017_fp.txt',
]

result = []
last = None
for file in file_list:
    with open(file) as f:
        text = f.read().splitlines()
        while text:
            print(text[0].split())
            name = text.pop(0).split()[3].split('/')[2].split('_')[0]
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

for item in result:
    print(item[0], item[1]/1000, item[3])

print('Mem')
for item in result:
    print(item[3])
print('Time')
for item in result:
    print(item[1]/1000)

