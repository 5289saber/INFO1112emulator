#!/bin/bash

DIR="tests/test_16/"
TEST="test16"
NUM="16"

echo "====== <Test $NUM: Full system; Reverse string input len 5> ======"
echo ""

python3 assembler.py "${DIR}${TEST}.asm" "${DIR}${TEST}.bin" > "${DIR}${TEST}A.out" 2>&1

diff --color -u "${DIR}${TEST}A.out" "${DIR}${TEST}ExpA.txt"

if [ $? = 0 ]; then

    diff --color -u "${DIR}${TEST}.bin" "${DIR}${TEST}Exp.bin" >> "${DIR}${TEST}A.out"

    if [ $? = 0 ]; then
        
        python3 emulator.py "${DIR}${TEST}.bin" < "${DIR}${TEST}.in"  > "${DIR}${TEST}E.out" 2>&1

        diff --color -u "${DIR}${TEST}E.out" "${DIR}${TEST}ExpE.txt"

        if [ $? = 0 ]; then
            echo -e "\033[1;33mTest $NUM passed\033[0m"
        else
            echo -e "\033[1;35mTest $NUM failed\033[0m"
        fi

    else
        echo -e "\033[1;35mTest $NUM failed\033[0m"
        cat "${DIR}${TEST}A.out" | tail -n +2
    fi

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

echo ""