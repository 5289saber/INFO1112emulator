#!/bin/bash

DIR="tests/test2/"
TEST="test2"
NUM="2"

echo "====== <Test $NUM: normal compilation> ======"
echo ""

python3 assembler.py "${DIR}${TEST}.asm" "${DIR}${TEST}.bin" > "${DIR}${TEST}.out" 2>&1

if [ "$(cat "${DIR}${TEST}.out")" = "Finished compiling. File ${DIR}${TEST}.bin has been created." ]; then

    diff --color -u "${DIR}${TEST}.bin" "${DIR}${TEST}Exp.bin" >> "${DIR}${TEST}.out"

    if [ $? = 0 ]; then
        echo "Test $NUM passed:"
        cat "${DIR}${TEST}.out"
    else
        echo "Test $NUM failed:"
        cat "${DIR}${TEST}.out" | tail -n +2
    fi

else
    echo "Test $NUM failed:"
    cat "${DIR}${TEST}.out"
fi

echo ""
