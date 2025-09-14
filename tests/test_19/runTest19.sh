#!/bin/bash

DIR="tests/test_19/"
TEST="test19"
NUM="19"

chmod u-r "${DIR}${TEST}.bin" # manually removes the right to read the asm file for testing

echo "====== <Test $NUM: Emulator; Cannot read bin file> ======"
echo ""

python3 emulator.py "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    echo -e "\033[1;33mTest $NUM passed\033[0m"

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

chmod u+r tests/test_19/test19.bin # resets the state so I can access the file

echo ""