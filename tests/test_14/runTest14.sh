#!/bin/bash

DIR="tests/test_14/"
TEST="test14"
NUM="14"

echo "====== <Test $NUM: Emulator; Caller & Callee> ======"
echo ""

python3 assembler.py "${DIR}caller.asm" "${DIR}caller.bin" > "${DIR}callerA.out" 2>&1
python3 assembler.py "${DIR}callee.asm" "${DIR}callee.bin" > "${DIR}calleeA.out" 2>&1

diff --color -u "${DIR}callerA.out" "${DIR}callerExpA.txt"

if [ $? = 0 ]; then

    diff --color -u "${DIR}calleeA.out" "${DIR}calleeExpA.txt"

    if [ $? = 0 ]; then

        diff --color -u "${DIR}caller.bin" "${DIR}callerExp.bin" >> "${DIR}callerA.out"

        if [ $? = 0 ]; then
            
            diff --color -u "${DIR}callee.bin" "${DIR}calleeExp.bin" >> "${DIR}calleeA.out"

            if [ $? = 0 ]; then

                python3 emulator.py "${DIR}caller.bin"  > "${DIR}callerE.out" 2>&1
                
                diff --color -u "${DIR}callerE.out" "${DIR}callerExpE.txt"

                if [ $? = 0 ]; then
                    echo -e "\033[1;33mTest $NUM passed\033[0m"
                else
                    echo -e "\033[1;35mTest $NUM failed\033[0m"
                fi

            else
                echo -e "\033[1;35mTest $NUM failed\033[0m"
                cat "${DIR}calleeA.out" | tail -n +2
            fi

        else
            echo -e "\033[1;35mTest $NUM failed\033[0m"
            cat "${DIR}callerA.out" | tail -n +2
        fi
    
    else
        echo -e "\033[1;35mTest $NUM failed\033[0m"
    fi

else
    echo -e "\033[1;35mTest $NUM failed\033[0m"
fi

echo ""