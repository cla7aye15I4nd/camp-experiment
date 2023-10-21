#!/bin/bash

g++ spectest.c -o spectest

cd /root/cpu2017/benchspec/CPU/600.perlbench_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/perlbench_s_peak.lowfat -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/perlbench_s_peak.lowfat -I./lib diffmail.pl 4 800 10 17 19 300
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/perlbench_s_peak.lowfat -I./lib splitmail.pl 6400 12 26 16 100 0

cd /root/cpu2017/benchspec/CPU/602.gcc_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/sgcc_peak.lowfat gcc-pp.c -O5 -fipa-pta -o gcc-pp.opts-O5_-fipa-pta.s
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/sgcc_peak.lowfat gcc-pp.c -O5 -finline-limit=1000 -fselective-scheduling -fselective-scheduling2 -o gcc-pp.opts-O5_-finline-limit_1000_-fselective-scheduling_-fselective-scheduling2.s
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/sgcc_peak.lowfat gcc-pp.c -O5 -finline-limit=24000 -fgcse -fgcse-las -fgcse-lm -fgcse-sm -o gcc-pp.opts-O5_-finline-limit_24000_-fgcse_-fgcse-las_-fgcse-lm_-fgcse-sm.s

cd /root/cpu2017/benchspec/CPU/605.mcf_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/mcf_s_peak.lowfat inp.in

cd /root/cpu2017/benchspec/CPU/620.omnetpp_s/run/run_peak_refspeed_lowfat.0000
/root//spectest ../run_peak_refspeed_lowfat.0000/omnetpp_s_peak.lowfat -c General -r 0

cd /root/cpu2017/benchspec/CPU/623.xalancbmk_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/xalancbmk_s_peak.lowfat -v t5.xml xalanc.xsl

cd /root/cpu2017/benchspec/CPU/631.deepsjeng_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/deepsjeng_s_peak.lowfat ref.txt

cd /root/cpu2017/benchspec/CPU/641.leela_s/run/run_peak_refspeed_lowfat.0000
/root/camp-experiment/spec/spectest ../run_peak_refspeed_lowfat.0000/leela_s_peak.lowfat ref.sgf

