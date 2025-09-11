#!/bin/bash

DIR="tests/test5/"
TEST="test5"
NUM="5"

chmod u-r "${DIR}${TEST}.asm" # manually removes the right to read the asm file for testing

echo "====== <Test $NUM: Assembler; Cannot read in file > ======"
echo ""

python3 assembler.py "${DIR}${TEST}.asm" "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

diff --color -u "${DIR}${TEST}.out" "${DIR}${TEST}Exp.txt"

if [ $? = 0 ]; then

    echo -e "\033[1;33mTest $NUM passed\033[0m"

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

chmod u+r tests/test5/test5.asm # resets the state so I can access the file

echo ""