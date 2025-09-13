List of tests and their checking conditions:

Assembler specific:

    test_1: Simple assembling without error
    test_2: Assembling with comments and extra blank lines without error

    test_3: Malformed Instruction - JGT written as JFT
    test_4: Non existent file. test tries to find test4.asm where actual file is test41.asm
    test_5: Cannot read input file. executes chmod in shell script to remove and give read access independently
    test_6: Cannot write output file. same as test_5, executes chmod locally for write instead.
    test_7: Assembling with undefined label
    test_8: Assembling with duplicate label
    test_9: Assembling hex file

Entire system:

    test_10: full process of assembling and emulating without error.
    test_11: reading and outputting correctly using exit codes.
    test_12: blank file
    test_13: under and overflow
    test_14: caller and callee
    test_15: factorial of 5
    test_16: reversing string input of length 5