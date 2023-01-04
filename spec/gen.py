import os

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
        with open(f'{name}_{tag}_test.sh', 'w') as f:
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
                            f.write('/home/moe/camp-experiment/spec2017/spectest ' + ' '.join(line.split()[4:line.split().index('>')]) + '\n')
                
                f.write('\n')
