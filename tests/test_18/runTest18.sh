#!/bin/bash

DIR="tests/test_18/"
TEST="test18"
NUM="18"

echo "====== <Test $NUM: Emulator; Nonexistent file> ======"
echo ""

python3 emulator.py "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    echo -e "\033[1;33mTest $NUM passed\033[0m"

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

echo ""