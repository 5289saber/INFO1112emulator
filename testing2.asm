// Test JMP, JEQ, JGT with labels
SET 100 5
SET 101 5
SET 102 9

JEQ equal 100 101
JMP notequal

:equal:
PUT 100 N d
JGT bigger 102 100
JMP end

:notequal:
PUT 101 N d

:bigger:
PUT 102 N d

:end:
EXIT 0
