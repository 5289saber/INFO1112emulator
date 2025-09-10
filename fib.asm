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

//step by step explanation:
//sets memory @ position 2 to be 0
//sets memory @ position 3 to be 1
//sets memory @ position 10 to be hex(0A) fyi thats 10
//:loop: this is the label if we have a jump function (JMP,JGT,JEQ) where it'll jump here
//outputs value @ position 2 in decimal format
//outputs 1 value starting from position 10
//adds values @ positions 2 and 3 and setting the result into 4
//moving value @ position 3 to position 2
//moving value @ position 4 to position 3
//subtracting value @ position 1 to position 0 then setting the result into position 1
//jumps to label :loop: if value @ position 1 is greater than position 0