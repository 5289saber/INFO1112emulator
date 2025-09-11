#!/bin/bash

DIR="tests/test_2/"
TEST="test2"
NUM="2"

echo "====== <Test $NUM: Assembler; normal compilation cont.> ======"
echo ""

python3 assembler.py "${DIR}${TEST}.asm" "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    diff --color -u "${DIR}${TEST}.bin" "${DIR}${TEST}Exp.bin" >> "${DIR}${TEST}.out"

    if [ $? = 0 ]; then
        echo -e "\033[1;33mTest $NUM passed\033[0m"
    else
        echo -e "\033[1;35mTest $NUM failed\033[0m"
        cat "${DIR}${TEST}.out" | tail -n +2
    fi

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

echo ""
