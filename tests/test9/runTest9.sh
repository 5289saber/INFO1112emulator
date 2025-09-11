#!/bin/bash

DIR="tests/test9/"
TEST="test9"
NUM="9"

echo "====== <Test $NUM: Assembler; normal compilation hex> ======"
echo ""

python3 assembler.py --hex "${DIR}${TEST}.asm" "${DIR}${TEST}.hex" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    diff --color -u "${DIR}${TEST}.hex" "${DIR}${TEST}Exp.hex" >> "${DIR}${TEST}.out"

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
