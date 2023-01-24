#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2006/benchspec/CPU2006/400.perlbench/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/perlbench_base.camp_ctx -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/perlbench_base.camp_ctx -I./lib diffmail.pl 4 800 10 17 19 300
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/perlbench_base.camp_ctx -I./lib splitmail.pl 1600 12 26 16 4500

cd /home/moe/cpu2006/benchspec/CPU2006/401.bzip2/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx input.source 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx chicken.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx liberty.jpg 30
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx input.program 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx text.html 280
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/bzip2_base.camp_ctx input.combined 200

cd /home/moe/cpu2006/benchspec/CPU2006/403.gcc/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx 166.in -o 166.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx 200.in -o 200.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx c-typeck.in -o c-typeck.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx cp-decl.in -o cp-decl.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx expr.in -o expr.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx expr2.in -o expr2.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx g23.in -o g23.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx s04.in -o s04.s
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gcc_base.camp_ctx scilab.in -o scilab.s

cd /home/moe/cpu2006/benchspec/CPU2006/429.mcf/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/mcf_base.camp_ctx inp.in

cd /home/moe/cpu2006/benchspec/CPU2006/433.milc/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/milc_base.camp_ctx < su3imp.in 

cd /home/moe/cpu2006/benchspec/CPU2006/445.gobmk/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gobmk_base.camp_ctx --quiet --mode gtp < 13x13.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gobmk_base.camp_ctx --quiet --mode gtp < nngs.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gobmk_base.camp_ctx --quiet --mode gtp < score2.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gobmk_base.camp_ctx --quiet --mode gtp < trevorc.tst 
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/gobmk_base.camp_ctx --quiet --mode gtp < trevord.tst 

cd /home/moe/cpu2006/benchspec/CPU2006/456.hmmer/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/hmmer_base.camp_ctx nph3.hmm swiss41
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/hmmer_base.camp_ctx --fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm

cd /home/moe/cpu2006/benchspec/CPU2006/458.sjeng/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/sjeng_base.camp_ctx ref.txt

cd /home/moe/cpu2006/benchspec/CPU2006/462.libquantum/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/libquantum_base.camp_ctx 1397 8

cd /home/moe/cpu2006/benchspec/CPU2006/464.h264ref/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/h264ref_base.camp_ctx -d foreman_ref_encoder_baseline.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/h264ref_base.camp_ctx -d foreman_ref_encoder_main.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/h264ref_base.camp_ctx -d sss_encoder_main.cfg

cd /home/moe/cpu2006/benchspec/CPU2006/470.lbm/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/lbm_base.camp_ctx 3000 reference.dat 0 0 100_100_130_ldc.of

cd /home/moe/cpu2006/benchspec/CPU2006/482.sphinx3/run/run_base_ref_camp_ctx.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_camp_ctx.0000/sphinx_livepretend_base.camp_ctx ctlfile . args.an4

