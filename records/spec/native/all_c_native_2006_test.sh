#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2006/benchspec/CPU2006/400.perlbench/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/perlbench_base.native -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/perlbench_base.native -I./lib diffmail.pl 4 800 10 17 19 300
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/perlbench_base.native -I./lib splitmail.pl 1600 12 26 16 4500

cd /home/moe/cpu2006/benchspec/CPU2006/401.bzip2/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native input.source 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native chicken.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native liberty.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native input.program 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native text.html 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/bzip2_base.native input.combined 200

cd /home/moe/cpu2006/benchspec/CPU2006/403.gcc/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native 166.in -o 166.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native 200.in -o 200.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native c-typeck.in -o c-typeck.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native cp-decl.in -o cp-decl.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native expr.in -o expr.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native expr2.in -o expr2.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native g23.in -o g23.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native s04.in -o s04.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gcc_base.native scilab.in -o scilab.s

cd /home/moe/cpu2006/benchspec/CPU2006/429.mcf/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/mcf_base.native inp.in

cd /home/moe/cpu2006/benchspec/CPU2006/433.milc/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/milc_base.native < su3imp.in 

cd /home/moe/cpu2006/benchspec/CPU2006/445.gobmk/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gobmk_base.native --quiet --mode gtp < 13x13.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gobmk_base.native --quiet --mode gtp < nngs.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gobmk_base.native --quiet --mode gtp < score2.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gobmk_base.native --quiet --mode gtp < trevorc.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/gobmk_base.native --quiet --mode gtp < trevord.tst 

cd /home/moe/cpu2006/benchspec/CPU2006/456.hmmer/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/hmmer_base.native nph3.hmm swiss41
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/hmmer_base.native --fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm

cd /home/moe/cpu2006/benchspec/CPU2006/458.sjeng/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/sjeng_base.native ref.txt

cd /home/moe/cpu2006/benchspec/CPU2006/462.libquantum/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/libquantum_base.native 1397 8

cd /home/moe/cpu2006/benchspec/CPU2006/464.h264ref/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/h264ref_base.native -d foreman_ref_encoder_baseline.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/h264ref_base.native -d foreman_ref_encoder_main.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/h264ref_base.native -d sss_encoder_main.cfg

cd /home/moe/cpu2006/benchspec/CPU2006/470.lbm/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/lbm_base.native 3000 reference.dat 0 0 100_100_130_ldc.of

cd /home/moe/cpu2006/benchspec/CPU2006/482.sphinx3/run/run_base_ref_native.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_native.0000/sphinx_livepretend_base.native ctlfile . args.an4

