#!/bin/bash

#to run: ./tests/run_tests.sh

echo ""

for dir in tests/*/; do
    for test in "$dir"/*.sh; do
        ./$test
    done
done