import os

def create_spec2017_script():
    script = {
        'int': [
            '600.perlbench_s',
            '602.gcc_s',
            '605.mcf_s',
            '620.omnetpp_s',
            '623.xalancbmk_s',
            '625.x264_s',
            '631.deepsjeng_s',
            '641.leela_s',
            '657.xz_s',
        ],
        'fp': [
            '619.lbm_s',
            '638.imagick_s',
            '644.nab_s',
        ],
    }

    tags = ['asan', 'camp', 'native']
    base_dir = '/home/moe/cpu2017/benchspec/CPU'
    run_base = 'run_peak_refspeed_'

    for name, cases in script.items():
        for tag in tags:
            with open(f'{name}_{tag}_2017_test.sh', 'w') as f:
                f.write('#!/bin/bash\n\n')
                f.write('g++ spectest.c -o spectest\n\n')

                for case in cases:
                    case_path = os.path.join(base_dir, case, 'run')
                    avail = [dir for dir in os.listdir(case_path) if dir.startswith(f'{run_base}{tag}.')]

                    if not avail:
                        print("Not Found", case, tag)
                        continue
                    run_path = os.path.join(case_path, max(avail))

                    f.write(f'cd {run_path}\n')
                    with open(f'{run_path}/speccmds.cmd') as sf:
                        for line in sf.read().splitlines():
                            if line.startswith('-o'):
                                line_split = line.split()
                                line_split = line_split[:line_split.index('>')]
                                while not line_split[0].startswith('../run'):
                                    line_split.pop(0)
                                f.write('/home/moe/camp-experiment/spec/spectest ' + ' '.join(line_split) + '\n')
                    
                    f.write('\n')

def create_spec2006_script():
    script = {
        'all_c': [
            '400.perlbench',
            '401.bzip2',
            '403.gcc',
            '429.mcf',
            '433.milc',
            '445.gobmk',
            '456.hmmer',
            '458.sjeng',
            '462.libquantum',
            '464.h264ref',
            '470.lbm',
            '482.sphinx3',
        ],
        'all_cpp': [
            '444.namd',
            '447.dealII',
            '450.soplex',
            '453.povray',
            '471.omnetpp',
            '473.astar',
            '483.xalancbmk',
        ],
    }

    tags = ['asan', 'camp', 'native']
    base_dir = '/home/moe/cpu2006/benchspec/CPU2006'
    run_base = 'run_base_ref_'

    for name, cases in script.items():
        for tag in tags:
            with open(f'{name}_{tag}_2006_test.sh', 'w') as f:
                f.write('#!/bin/bash\n\n')
                f.write('g++ spectest.c -o spectest\n\n')

                for case in cases:
                    case_path = os.path.join(base_dir, case, 'run')
                    avail = [dir for dir in os.listdir(case_path) if dir.startswith(f'{run_base}{tag}.')]

                    if not avail:
                        print("Not Found", case, tag)
                        continue
                    run_path = os.path.join(case_path, max(avail))

                    f.write(f'cd {run_path}\n')
                    with open(f'{run_path}/speccmds.cmd') as sf:
                        for line in sf.read().splitlines():
                            if line.startswith('-o') or line.startswith('-i'):
                                line_split = line.split()
                                while not line_split[0].startswith('../run'):
                                    line_split.pop(0)
                                f.write('/home/moe/camp-experiment/spec/spectest ' + ' '.join(line_split) + '\n')
                    
                    f.write('\n')


create_spec2017_script()
create_spec2006_script()
os.system('chmod +x *.sh')