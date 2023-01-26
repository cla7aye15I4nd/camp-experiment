#!/bin/bash

g++ spectest.c -o spectest

cd /home/moe/cpu2006/benchspec/CPU2006/444.namd/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/namd_base.markus --input namd.input --iterations 38 --output namd.out

cd /home/moe/cpu2006/benchspec/CPU2006/447.dealII/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/dealII_base.markus 23

cd /home/moe/cpu2006/benchspec/CPU2006/450.soplex/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/soplex_base.markus -s1 -e -m45000 pds-50.mps
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/soplex_base.markus -m3500 ref.mps

cd /home/moe/cpu2006/benchspec/CPU2006/453.povray/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/povray_base.markus SPEC-benchmark-ref.ini

cd /home/moe/cpu2006/benchspec/CPU2006/473.astar/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/astar_base.markus BigLakes2048.cfg
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/astar_base.markus rivers.cfg

cd /home/moe/cpu2006/benchspec/CPU2006/483.xalancbmk/run/run_base_ref_markus.0000
/home/moe/camp-experiment/spec/spectest ../run_base_ref_markus.0000/Xalan_base.markus -v t5.xml xalanc.xsl

