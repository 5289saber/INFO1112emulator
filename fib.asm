// First 10 number in the fibonacci sequence
SET 0 1
SET 1 10
SET 2 0
SET 3 1
SET 10 0x0A
:loop:
PUT 2 N d
PUT 10 S 1
ADD 4 2 3
MOV 2 3
MOV 3 4
SUB 1 1 0
JGT loop 1 0
