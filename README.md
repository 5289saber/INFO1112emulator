# INFO1112emulator
# https://github.com/5289saber/INFO1112emulator.git

Personal github link is provided for reference to file hierarchy and version checking purposes.

all old testing files are put into oldCases, please ignore.
all testcases for submission are in tests
# each testcase is summarised in the README.md withint the tests folder.

Submission notes:
please make sure that the tests folder is in the same directory as the assembler and emulator.
you are able to run ./tests/run_tests in the directory where the assembler and emulator is located.

if the hierarchy is faulty, testcase 14 (call) could fail due to the directory for tests/test_14 not found during execution

if not possible to resolve chmod issue, please manually remove permissions for:
1. chmod u-r tests/test_5/test5.asm
2. chmod u-w tests/test_6/test6.bin
or there is a possibility that the tests and emulator/assembler can be downloaded locally and tested - would be fastest?