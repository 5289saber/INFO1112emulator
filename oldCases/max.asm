SET 0 0
SET 1 255
SET 2 1

:loop:
PUT 0 N d
ADD 0 0 2
JGT loop 1 0

//PUT 0 N d
EXIT 0