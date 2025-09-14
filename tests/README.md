# List of tests and their checking conditions:

***

## Assembler specific:

    test_1: Simple assembling without error
    test_2: Assembling with comments and extra blank lines without error
    test_3: Malformed Instruction - JGT written as JFT
    test_4: Non existent file. test tries to find test4.asm where actual file is test41.asm
    test_5: Cannot read input file. executes chmod in shell script to remove and give read access independently (failed - ED)
    test_6: Cannot write output file. same as test_5, executes chmod locally for write instead. (failed - ED)
    test_7: Assembling with undefined label
    test_8: Assembling with duplicate label
    test_9: Assembling hex file

***

## Full system:

    test_10: full process of assembling and emulating without error.
    test_11: reading and outputting correctly using exit codes.
    test_12: blank file

        - makes sure that the assembler and emulator can handle a blank file

    test_13: under and overflow

        - tests the ability to handle under and overflowing for add and sub
        
    test_14: caller and callee
    test_15: factorial of 5

        - this test focuses on using loops to find the factorial of a number. The number 5 is hardcoded into the assembly script.
        
        - this test uses loops, mov, add and subs to simulate the multiplication process

    test_16: reversing string input of length 5

        - this test will examine the ability of the program to take stdin and moving characters to print the reverse
        
        - inputs are managed using redirections and the length is set to 5 bytes -> anymore after is not read.

    test_17: max 256 instructions

        - this test is a bit weird by testing the max of 256 instructions executed.

        - the last number should be 84, as the program will use 3 instructions to set variables at positions 0,1,2
        
        - afterwards, each loop consists of 3 instructions, with the remaining limit of 253. Hence 253/3 = 84.33333...
        
        - instructions will end at 84, where 0.3333.. instructions left isn't enough to run the rest.

***

## Emulator specific:

    test_18: executable does not exist
    test_19: executable cannot be read (failed - ED)
    test_20: not valid executable