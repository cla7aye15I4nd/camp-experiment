#!/bin/bash

g++ spectest.c -o spectest

cd /root/cpu2006/benchspec/CPU2006/400.perlbench/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/perlbench_base.ffmalloc_st -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/perlbench_base.ffmalloc_st -I./lib diffmail.pl 4 800 10 17 19 300
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/perlbench_base.ffmalloc_st -I./lib splitmail.pl 1600 12 26 16 4500

cd /root/cpu2006/benchspec/CPU2006/401.bzip2/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st input.source 280
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st chicken.jpg 30
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st liberty.jpg 30
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st input.program 280
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st text.html 280
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/bzip2_base.ffmalloc_st input.combined 200

cd /root/cpu2006/benchspec/CPU2006/403.gcc/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st 166.in -o 166.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st 200.in -o 200.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st c-typeck.in -o c-typeck.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st cp-decl.in -o cp-decl.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st expr.in -o expr.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st expr2.in -o expr2.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st g23.in -o g23.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st s04.in -o s04.s
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gcc_base.ffmalloc_st scilab.in -o scilab.s

cd /root/cpu2006/benchspec/CPU2006/429.mcf/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/mcf_base.ffmalloc_st inp.in

cd /root/cpu2006/benchspec/CPU2006/433.milc/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/milc_base.ffmalloc_st < su3imp.in 

cd /root/cpu2006/benchspec/CPU2006/445.gobmk/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gobmk_base.ffmalloc_st --quiet --mode gtp < 13x13.tst 
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gobmk_base.ffmalloc_st --quiet --mode gtp < nngs.tst 
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gobmk_base.ffmalloc_st --quiet --mode gtp < score2.tst 
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gobmk_base.ffmalloc_st --quiet --mode gtp < trevorc.tst 
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/gobmk_base.ffmalloc_st --quiet --mode gtp < trevord.tst 

cd /root/cpu2006/benchspec/CPU2006/456.hmmer/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/hmmer_base.ffmalloc_st nph3.hmm swiss41
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/hmmer_base.ffmalloc_st --fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm

cd /root/cpu2006/benchspec/CPU2006/458.sjeng/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/sjeng_base.ffmalloc_st ref.txt

cd /root/cpu2006/benchspec/CPU2006/462.libquantum/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/libquantum_base.ffmalloc_st 1397 8

cd /root/cpu2006/benchspec/CPU2006/464.h264ref/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/h264ref_base.ffmalloc_st -d foreman_ref_encoder_baseline.cfg
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/h264ref_base.ffmalloc_st -d foreman_ref_encoder_main.cfg
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/h264ref_base.ffmalloc_st -d sss_encoder_main.cfg

cd /root/cpu2006/benchspec/CPU2006/470.lbm/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/lbm_base.ffmalloc_st 3000 reference.dat 0 0 100_100_130_ldc.of

cd /root/cpu2006/benchspec/CPU2006/482.sphinx3/run/run_base_ref_ffmalloc_st.0000
/root/camp-experiment/spec/spectest ../run_base_ref_ffmalloc_st.0000/sphinx_livepretend_base.ffmalloc_st ctlfile . args.an4

