
labels = [
    'perlbench',
    'bzip2',
    'gcc',
    'mcf',
    'milc',
    'gobmk',
    'hmmer',
    'sjeng',
    'libquantum',
    'h264ref',
    'lbm',
    'sphinx3',
    'namd',
    'dealII',
    'soplex',
    'povray',
    'astar',
    'xalancbmk',
]

cpu2006 = {
    'native': [
        '137.24',
        '251.03',
        '159.57',
        '277.95',
        '346.18',
        '221.01',
        '150.74',
        '253.80',
        '161.99',
        '194.27',
        '91.76',
        '219.31',
        '145.434',
        '560.804',
        '124.562',
        '81.905',
        '215.274',
        '275.569',
    ],
    'tcmalloc': [
        '132.89',
        '237.54',
        '108.71',
        '128.16',
        '242.76',
        '224.32',
        '154.68',
        '256.73',
        '162.96',
        '194.86',
        '92.99',
        '226.67',
        '150.34',
        '582.67',
        '135.14',
        '83.54',
        '217.43',
        '260.07',
    ],
    'camp': [
        '546.87',
        '359.23',
        '182.55',
        '166.53',
        '265.19',
        '292.46',
        '345.32',
        '283.31',
        '192.80',
        '455.18',
        '90.92',
        '449.77',
        '286.00',
        '827.30',
        '223.68',
        '175.54',
        '401.35',
        '702.18',
    ],
    'camp-remove': [
        '641.61',
        '388.88',
        '258.75',
        '196.68',
        '313.55',
        '327.94',
        '359.71',
        '306.43',
        '240.09',
        '531.66',
        '142.06',
        '514.60',
        '326.58',
        '1027.54',
        '258.17',
        '234.02',
        '565.59',
        '1115.45',
    ],
    'camp-type': [
        '750.33',
        '442.37',
        '332.30',
        '337.45',
        '427.27',
        '364.47',
        '364.09',
        '311.66',
        '240.72',
        '544.52',
        '105.50',
        '525.06',
        '306.38',
        '1668.68',
        '328.58',
        '341.47',
        '777.30',
        '1316.46',
    ],
    'camp-merge': [
        '541.86',
        '704.51',
        '245.60',
        '252.11',
        '325.68',
        '335.62',
        '1447.59',
        '320.83',
        '355.19',
        '1090.55',
        '117.69',
        '1503.98',
        '615.12',
        '1060.80',
        '327.59',
        '192.67',
        '609.89',
        '1203.03',
    ],
}

import numpy as np
import matplotlib.pyplot as plt

native = np.array([float(x) for x in cpu2006['native']])

for key in cpu2006.keys():
    cpu2006[key] = np.array([float(x) * 100 for x in cpu2006[key]]) / native

size = len(labels)
x = np.arange(size)

total_width, n = 0.8, len(cpu2006.keys())
width = total_width / n
x = x - (total_width - width) / 2

plt.figure(figsize=(11,5))
plt.xticks(x, labels, rotation=75)

for i, key in enumerate(cpu2006.keys()):
    plt.bar(x + i * width, cpu2006[key], width=width, label=key)

plt.subplots_adjust(bottom=0.25)
plt.legend()
plt.ylabel("Runtime Overhead (%)", font = {
    'family' : 'Computer Modern Roamn',
    'weight' : 'normal',
    'size'   : 12,
})


plt.savefig('cpu2006.png')
