import sys

programFile = sys.argv[1]
returnFile = programFile.split('.')[0] + ".bin"

def valueConversion(value: str):
    header = value[0]
    if header.isalpha():
        # ASCII
        #print("The value is ASCII")
        return bin(ord(value))
    elif header == "0":
        # bin, hex, oct
        numType = value[0:2]
        match numType:
            case "0b":
                #print("number is binary")
                return bin(int(value[2:],2))
            case "0x":
                #print("number is hexadecimal")
                return bin(int(value[2:],16))
            case "0o":
                #print("number is octal")
                return bin(int(value[2:],8))
    else:
        #print("The number is decimal")
        return bin(int(value))
    

def assembler(instructions, allLines):
    """
    opcodes:
    1. SET <d> <v>
    2. MOV <d> <s>
    3. ADD <d> <a> <b>
    4. SUB <d> <a> <b>
    8. READ <d> N
    8. READ <d> S <c>
    9. PUT <s> N <f>
    9. PUT <s> S <c>
    16. JMP <label>
    17. JEQ <label> <a> <b>
    18. JGT <label> <a> <b>
    32. CALL <d> <p>
    33. EXIT <v>
    """
    bytes: [str] = instructions.split(" ") # split the instruction into operands and opcode
    opcode = bytes[0] # opcode is 1st position
    encodedCommand = [0,0,0,0] # mach. instr.'s are 4 bytes

    match opcode: # sets the command for the inputted instruction
        case "SET":
            encodedCommand[0] = bin(0b000000001)
            encodedCommand[1] = valueConversion(bytes[1]) #mem address
            encodedCommand[2] = valueConversion(bytes[2]) #value
            encodedCommand[3] = bin(0)

        case "MOV":
            encodedCommand[0] = bin(0b000000010)
            encodedCommand[1] = bin(int(bytes[1])) #mem address 1
            encodedCommand[2] = bin(int(bytes[2])) #mem address 1
            encodedCommand[3] = bin(0)

        case "ADD":
            encodedCommand[0] = bin(0b000000011)
            encodedCommand[1] = bin(int(bytes[1])) #mem address 1
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2

        case "SUB":
            encodedCommand[0] = bin(0b000000100)
            encodedCommand[1] = bin(int(bytes[1])) #mem address 1
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2

        case "READ": #storing command
            encodedCommand[0] = bin(0b000001000)
            encodedCommand[1] = bin(int(bytes[1])) #mem address 1
            if bytes[2] == "N": #read number of bytes
                encodedCommand[2] = bin(0b000000001) #num of bytes
                encodedCommand[3] = bin(0) #value2
            elif bytes[2] == "S": # read <value2> bytes from stdin
                encodedCommand[2] = bin(0b000000010) #string
                encodedCommand[3] = bin(int(bytes[3])) #value2

        case "PUT": #output command
            encodedCommand[0] = bin(0b000001001)
            encodedCommand[1] = bin(int(bytes[1])) #mem address 1
            if bytes[2] == "N": #output value @ address see p7 of docs
                encodedCommand[2] = valueConversion(bytes[3]) #format
                encodedCommand[3] = bin(0)
            elif bytes[2] == "S": #put bytes and print value
                encodedCommand[2] = bin(0b10000000) #string
                encodedCommand[3] = bin(int(bytes[3])) #value2

        case "JMP": # dont know how yet
            encodedCommand[0] = bin(0b00010000) 

            label = bytes[1] #label name
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    encodedCommand[1] = valueConversion(str(allLines.index(line))) #stores the line of the command.

            encodedCommand[2] = bin(0b0)
            encodedCommand[3] = bin(0b0)

        case "JEQ": # dont know how yet -> might be the same as JMP but will have to test if JMP works first.
            encodedCommand[0] = bin(0b00010001) 

            label = bytes[1] #label name
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    encodedCommand[1] = valueConversion(str(allLines.index(line))) #stores the line of the command.
                
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2

        case "JGT": # dont know how yet
            encodedCommand[0] = bin(0b00010010) 
            
            label = bytes[1] #label name
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    encodedCommand[1] = valueConversion(str(allLines.index(line))) #stores the line of the command.
                
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2
            
        case "CALL": # dont know how yet -> use os.fork()
            encodedCommand[0] = bin(0b00100000)
            encodedCommand[1] = bin(0b0) #storage for child process exit code
            encodedCommand[2] = bin(0b0) #string for child process name??????
            encodedCommand[3] = bin(0b0)
        case "EXIT":
            encodedCommand[0] = bin(0b00100001)
            encodedCommand[1] = bin(int(bytes[1])) #exit code
            encodedCommand[2] = bin(0b0)
            encodedCommand[3] = bin(0b0)

    return encodedCommand


def main():
    """
    quit = False
    while quit == False:
        value = str(input("Enter value: "))

        if value.lower() == "stop":
            quit = True
            continue

        valueConversion(value)
"""
    pc = 0 #program counter
    memory = [0]*20 #265 bytes of mem

    memory[0] = valueConversion('0xF2')
    memory[1] = valueConversion('0xC3')
    memory[2] = valueConversion('0x38')
    memory[3] = valueConversion('0x01')

    pc += 4 # the start of the executable file. used for checking if the file is stdchip executable

    with open(programFile, 'r') as openFile:
        allLines = openFile.readlines()
        #print(allLines)

        for line in allLines: #comment clearing loop
            if line[0:2] == "//":
                allLines.remove(line);    

        for line in allLines:
            if line.strip()[0] == ":" and line.strip()[-1] == ":": # finds labels and ignores (does not encode into memory.)
                #print("This is a label")
                continue
            else:
                #print("Encoding line: " + line)
                #print("first " + line.strip()[0] + " second " + line.strip()[-1])
                tempCode = assembler(line.strip(),allLines) #shoves line into assembler and returns a list[4] of the converted instr.
                for i in range(len(tempCode)):
                    memory[pc+i] = tempCode[i] # appends the binary instr. into the memory

                pc += 4 # has 4 bytes per instr. so add 4 smartass.

    print(memory)

if __name__ == "__main__":
    main()