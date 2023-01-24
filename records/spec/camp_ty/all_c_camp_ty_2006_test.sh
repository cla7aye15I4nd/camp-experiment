#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2006/benchspec/CPU2006/400.perlbench/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/perlbench_base.camp_ty -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/perlbench_base.camp_ty -I./lib diffmail.pl 4 800 10 17 19 300
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/perlbench_base.camp_ty -I./lib splitmail.pl 1600 12 26 16 4500

cd /home/moe/cpu2006/benchspec/CPU2006/401.bzip2/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty input.source 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty chicken.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty liberty.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty input.program 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty text.html 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/bzip2_base.camp_ty input.combined 200

cd /home/moe/cpu2006/benchspec/CPU2006/403.gcc/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty 166.in -o 166.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty 200.in -o 200.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty c-typeck.in -o c-typeck.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty cp-decl.in -o cp-decl.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty expr.in -o expr.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty expr2.in -o expr2.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty g23.in -o g23.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty s04.in -o s04.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gcc_base.camp_ty scilab.in -o scilab.s

cd /home/moe/cpu2006/benchspec/CPU2006/429.mcf/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/mcf_base.camp_ty inp.in

cd /home/moe/cpu2006/benchspec/CPU2006/433.milc/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/milc_base.camp_ty < su3imp.in 

cd /home/moe/cpu2006/benchspec/CPU2006/445.gobmk/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gobmk_base.camp_ty --quiet --mode gtp < 13x13.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gobmk_base.camp_ty --quiet --mode gtp < nngs.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gobmk_base.camp_ty --quiet --mode gtp < score2.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gobmk_base.camp_ty --quiet --mode gtp < trevorc.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/gobmk_base.camp_ty --quiet --mode gtp < trevord.tst 

cd /home/moe/cpu2006/benchspec/CPU2006/456.hmmer/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/hmmer_base.camp_ty nph3.hmm swiss41
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/hmmer_base.camp_ty --fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm

cd /home/moe/cpu2006/benchspec/CPU2006/458.sjeng/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/sjeng_base.camp_ty ref.txt

cd /home/moe/cpu2006/benchspec/CPU2006/462.libquantum/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/libquantum_base.camp_ty 1397 8

cd /home/moe/cpu2006/benchspec/CPU2006/464.h264ref/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/h264ref_base.camp_ty -d foreman_ref_encoder_baseline.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/h264ref_base.camp_ty -d foreman_ref_encoder_main.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/h264ref_base.camp_ty -d sss_encoder_main.cfg

cd /home/moe/cpu2006/benchspec/CPU2006/470.lbm/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/lbm_base.camp_ty 3000 reference.dat 0 0 100_100_130_ldc.of

cd /home/moe/cpu2006/benchspec/CPU2006/482.sphinx3/run/run_base_ref_camp_ty.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ty.0000/sphinx_livepretend_base.camp_ty ctlfile . args.an4
