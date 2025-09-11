SET 0 0x0A
SET 1 0x05
SUB 2 0 1
JGT greater 2 1
SET 3 0x01
JMP end
:great:
SET 3 0x02
:end:
PUT 3 N d
EXIT 3