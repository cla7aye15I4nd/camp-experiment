#!/bin/bash

if [ ! -d "dataset" ]; then
    if [ ! -f "2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3.zip" ]; then
        wget https://samate.nist.gov/SARD/downloads/test-suites/2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3.zip
    fi
    unzip 2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3.zip
    mv C dataset
    cd dataset/testcases
    ls \
    | grep -v CWE122_Heap_Based_Buffer_Overflow \
    | grep -v CWE124_Buffer_Underwrite \
    | grep -v CWE126_Buffer_Overread \
    | grep -v CWE127_Buffer_Underread \
    | grep -v CWE415_Double_Free \
    | grep -v CWE416_Use_After_Free \
    | grep -v CWE476_NULL_Pointer_Dereference \
    | grep -v CWE761_Free_Pointer_Not_at_Start_of_Buffer \
    | xargs rm -rf
    cd -
fi
