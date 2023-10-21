#!/bin/bash

g++ spectest.c -o spectest

cd /root/cpu2006/benchspec/CPU2006/444.namd/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/namd_base.native --input namd.input --iterations 38 --output namd.out

cd /root/cpu2006/benchspec/CPU2006/447.dealII/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/dealII_base.native 23

cd /root/cpu2006/benchspec/CPU2006/450.soplex/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/soplex_base.native -s1 -e -m45000 pds-50.mps
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/soplex_base.native -m3500 ref.mps

cd /root/cpu2006/benchspec/CPU2006/453.povray/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/povray_base.native SPEC-benchmark-ref.ini

cd /root/cpu2006/benchspec/CPU2006/473.astar/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/astar_base.native BigLakes2048.cfg
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/astar_base.native rivers.cfg

cd /root/cpu2006/benchspec/CPU2006/483.xalancbmk/run/run_base_ref_native.0000
/root/camp-experiment/spec/spectest ../run_base_ref_native.0000/Xalan_base.native -v t5.xml xalanc.xsl

