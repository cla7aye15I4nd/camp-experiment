
labels = [
    'perlbench',
    'gcc',
    'mcf',
    # 'omnetpp',
    'xalancbmk',
    'x264',
    'deepsjeng',
    'leela',
    'xz',
    'lbm',
    'imagick',
    'nab',
]

cpu2017 = {
    'native': [
        '187.54',
        '367.401',
        '443.741',
        # '552.02',
        '315.82',
        '282.89',
        '258.20',
        '792.70',
        '2069.44',
        '599.38',
        '4647.93',
        '1007.93',
    ],
    'tcmalloc': [
        '196.10',
        '384.51',
        '452.39',
        # '579.82',
        '301.65',
        '275.48',
        '260.50',
        '779.18',
        '2149.82',
        '601.15',
        '4743.50',
        '1010.51',
    ],
    'camp oob': [
        '392.69',
        '424.33',
        '470.49',
        # '548.87',
        '429.60',
        '480.95',
        '262.68',
        '799.24',
        '2311.17',
        '604.36',
        '6910.77',
        '1640.14',
    ],
    'camp uaf': [
        '470.524',
        '650.506',
        '489.271',
        # '516.166',
        '650.841',
        '276.734',
        '259.274',
        '801.116',
        '2065.122',
        '600.102',
        '4725.595',
        '999.76',
    ],
    'camp': [
        '662.716',
        '686.577',
        '518.548',
        # '558.386',
        '720.776',
        '482.289',
        '264.096',
        '802.694',
        '2317.242',
        '605.15',
        '6900.566',
        '1642.568',
    ],
    'redundant-opt': [
        '935.03',
        '903.41',
        '607.47',
        # '587.13',
        '797.67',
        '584.18',
        '308.60',
        '864.32',
        '3138.59',
        '914.55',
        '7128.84',
        '1871.09',
    ],
    'struct-opt': [
        '1335.65',
        '1645.85',
        '1000.74',
        # '840.21',
        '1321.17',
        '555.81',
        '448.49',
        '1154.99',
        '3469.48',
        '815.37',
        '7876.44',
        '1865.19',
    ],
    'merge-opt': [
        '675.75',
        '840.66',
        '689.88',
        # '548.63',
        '1231.26',
        '1386.77',
        '313.35',
        '867.02',
        '3833.13',
        '835.37',
        '20568.345',
        '2295.545',
    ],
    'no-opt': [
        '1421.34',
        '1760.97',
        '1059.33',
        # '723.03',
        '1470.62',
        '1482.30',
        '542.93',
        '1217.26',
        '3956.78',
        '1566.02',
        '21760.75',
        '2510.21',
    ]
}

import math
import numpy as np
import matplotlib.pyplot as plt

native = np.array([float(x) for x in cpu2017['native']])
cpu2017.pop('native')
# cpu2017.pop('tcmalloc')

cpu2017.pop('camp oob')
cpu2017.pop('camp uaf')


for key in cpu2017.keys():
    for i in range(len(cpu2017[key])):
        v = float(cpu2017[key][i]) / native[i]
        cpu2017[key][i] = v


# cpu2017.pop('tcmalloc')
size = len(labels)
x = np.arange(size)

total_width, n = 0.8, len(cpu2017.keys())
width = total_width / n
x = x - (total_width - width) / 2

plt.figure(figsize=(12,5))
plt.xticks(x, labels, fontsize=12)

for i, key in enumerate(cpu2017.keys()):
    plt.bar(x + i * width - width * ((n-1)/2), cpu2017[key], width=width, label=key)

plt.subplots_adjust(bottom=0.20, left=0.08, right=0.95)
plt.legend()
plt.ylabel("Normalized Time", fontsize=12)

plt.savefig('cpu2017.png', dpi=300)
plt.savefig('cpu2017.pdf', dpi=300)
