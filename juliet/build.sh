#!/bin/bash

if [ ! -d "test" ]; then
    wget https://samate.nist.gov/SARD/downloads/test-suites/2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3.zip
    unzip 2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3.zip -d test
fi

# cd test/testcases
# rm -rf !(CWE415_Double_Free|CWE416_Use_After_Free|CWE761_Free_Pointer_Not_at_Start_of_Buffer)
# cd -