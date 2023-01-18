#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2017/benchspec/CPU/600.perlbench_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/perlbench_s_peak.native -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/perlbench_s_peak.native -I./lib diffmail.pl 4 800 10 17 19 300
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/perlbench_s_peak.native -I./lib splitmail.pl 6400 12 26 16 100 0

cd /home/moe/cpu2017/benchspec/CPU/602.gcc_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/sgcc_peak.native gcc-pp.c -O5 -fipa-pta -o gcc-pp.opts-O5_-fipa-pta.s
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/sgcc_peak.native gcc-pp.c -O5 -finline-limit=1000 -fselective-scheduling -fselective-scheduling2 -o gcc-pp.opts-O5_-finline-limit_1000_-fselective-scheduling_-fselective-scheduling2.s
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/sgcc_peak.native gcc-pp.c -O5 -finline-limit=24000 -fgcse -fgcse-las -fgcse-lm -fgcse-sm -o gcc-pp.opts-O5_-finline-limit_24000_-fgcse_-fgcse-las_-fgcse-lm_-fgcse-sm.s

cd /home/moe/cpu2017/benchspec/CPU/605.mcf_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/mcf_s_peak.native inp.in

cd /home/moe/cpu2017/benchspec/CPU/620.omnetpp_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/omnetpp_s_peak.native -c General -r 0

cd /home/moe/cpu2017/benchspec/CPU/623.xalancbmk_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/xalancbmk_s_peak.native -v t5.xml xalanc.xsl

cd /home/moe/cpu2017/benchspec/CPU/625.x264_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/x264_s_peak.native --pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/x264_s_peak.native --pass 2 --stats x264_stats.log --bitrate 1000 --dumpyuv 200 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/x264_s_peak.native --seek 500 --dumpyuv 200 --frames 1250 -o BuckBunny_New.264 BuckBunny.yuv 1280x720

cd /home/moe/cpu2017/benchspec/CPU/631.deepsjeng_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/deepsjeng_s_peak.native ref.txt

cd /home/moe/cpu2017/benchspec/CPU/641.leela_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/leela_s_peak.native ref.sgf

cd /home/moe/cpu2017/benchspec/CPU/657.xz_s/run/run_peak_refspeed_native.0000
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/xz_s_peak.native cpu2006docs.tar.xz 6643 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1036078272 1111795472 4
/home/moe/camp-experiment/spec/spectest ../run_peak_refspeed_native.0000/xz_s_peak.native cld.tar.xz 1400 19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474 536995164 539938872 8

