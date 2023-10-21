import os

def patch(omit):
    for path, dirlist, filelist in os.walk('dataset'):
        for filename in filelist:
            if filename == 'Makefile':
                with open(os.path.join(path, filename)) as f:
                    lines = f.read().splitlines()
                    content = ''
                    for line in lines:
                        if line.startswith('INCLUDE_MAIN'):
                            if omit == 'bad':
                                content += 'INCLUDE_MAIN=-DINCLUDEMAIN -DOMITBAD'
                            else:
                                content += 'INCLUDE_MAIN=-DINCLUDEMAIN -DOMITGOOD'
                        else:
                            content += line
                        content += '\n'
                
                with open(os.path.join(path, filename), 'w') as f:
                    f.write(content)

def collect(tag):
    for path, dirlist, filelist in os.walk('dataset'):
        if any(f.endswith('.out') for f in filelist):
            os.system(f'cd {path} && rename "s/.out/.{tag}/" *.out')


os.system('find dataset | grep "\.out$" | xargs rm')
os.system('find dataset | grep "\.goodout$" | xargs rm')
os.system('find dataset | grep "\.badout$" | xargs rm')
os.system('find dataset | grep "\.goodans$" | xargs rm')
os.system('find dataset | grep "\.badans$" | xargs rm')

patch('bad')
os.system('cd dataset && make individuals -j`nproc`')
collect('goodans')

patch('good')
os.system('cd dataset && make individuals -j`nproc`')
collect('badans')

patch('bad')
os.system('cd dataset && make CC=/root/CAMP/tools/vcc CPP=/root/CAMP/tools/v++ individuals -j`nproc`')
collect('goodout')

patch('good')
os.system('cd dataset && make CC=/root/CAMP/tools/vcc CPP=/root/CAMP/tools/v++ individuals -j`nproc`')
collect('badout')