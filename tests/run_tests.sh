#!/bin/bash

#to run: ./tests/run_tests.sh

echo ""

for dir in $(ls -1d tests/test_*/ | sort -V); do
    for test in "$dir"/*.sh; do
        ./$test
    done
done