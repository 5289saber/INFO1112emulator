SET 0 0x05
SET 1 0x01
SET 4 0x01
SET 5 0x00

:start:
JGT multiply 0 4
JMP done

:multiply:
SET 2 0x00
MOV 3 0

:mult_loop:
JEQ mult_done 3 5
ADD 2 2 1
SUB 3 3 4
JMP mult_loop

:mult_done:
MOV 1 2
SUB 0 0 4
JMP start

:done:
PUT 1 N d
EXIT 1