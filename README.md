# INFO1112emulator
# https://github.com/5289saber/INFO1112emulator.git

Personal github link is provided for reference to file hierarchy and version checking purposes.

all old testing files are put into oldCases, please ignore.
all testcases for submission are in tests
# each testcase is summarised in the README.md within the tests folder.

## Submission notes:

> Please make sure that the tests folder is in the same directory as the assembler and emulator.
> You are able to run ./tests/run_tests in the directory where the assembler and emulator is located.

> If the hierarchy is faulty, testcase 14 (call) could fail due to the directory for tests/test_14 not found during execution

### Failure of tests 5 and 6 - reason provided.
Currently, tests 5 and 6 tests the stdout in throwing the correct assembler error message to the terminal.
However, due to the nature of ED not being able to remove permissions of files via chmod, both tests will fail as the in/out file can be read/written

To fully verify the correct testcase behaviour, please (if possible) manually remove permissions for:
1. chmod u-r tests/test_5/test5.asm
2. chmod u-w tests/test_6/test6.bin
(or perhaps there is a possibility that the tests and emulator/assembler can be downloaded locally and tested)

