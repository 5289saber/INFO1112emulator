#!/bin/bash

DIR="tests/test_4/"
TEST="test4"
NUM="4"

echo "====== <Test $NUM: Assembler; Nonexistent file > ======"
echo ""

python3 assembler.py "${DIR}${TEST}.asm" "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    echo -e "\033[1;33mTest $NUM passed\033[0m"

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

echo ""