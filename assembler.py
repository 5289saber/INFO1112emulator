import sys

def valueConversion(value: str):
    """
    takes value:str

    the value inputted can be binary, decimal, hexadecimal, octal and ASCII
    """
    header = value[0]
    if header.isalpha():
        # ASCII
        return bin(ord(value))
    elif header == "0":
        # bin, hex, oct
        numType = value[0:2]
        match numType:
            case "0b":
                return bin(int(value[2:],2))
            case "0x":
                return bin(int(value[2:],16))
            case "0o":
                return bin(int(value[2:],8))
    else:
        # decimal
        return bin(int(value))
    

def assembler(instructions, allLines, lineNum):
    """
    takes instructions:string, allLines:[list] and lineNum:int\n
    instructions are parsed into binary values before passing back to the main() to encode into memory\n
    allLines is used for label searching for JMP and extensions\n
    lineNum is used for error feedback\n

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
            encodedCommand[1] = bin(int(bytes[1])) #mem address
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
            found:bool = False
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    if found:
                        print(f"Duplicate label name: {label}")
                        return
                    encodedCommand[1] = valueConversion(allLines.index(line)) #stores the line of the command.
                    found = True
                
            if found == False:
                print(f"Undefined label name: {label}")
                return
            
            encodedCommand[2] = bin(0b0)
            encodedCommand[3] = bin(0b0)

        case "JEQ": # dont know how yet -> might be the same as JMP but will have to test if JMP works first.
            encodedCommand[0] = bin(0b00010001) 

            label = bytes[1] #label name
            found:bool = False
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    if found:
                        print(f"Duplicate label name: {label}")
                        return
                    encodedCommand[1] = valueConversion(allLines.index(line)) #stores the line of the command.
                    found = True
                
            if found == False:
                print(f"Undefined label name: {label}")
                return
            
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2

        case "JGT": # dont know how yet
            encodedCommand[0] = bin(0b00010010) 
            
            label = bytes[1] #label name
            found:bool = False
            #print(label)
            for line in allLines: # loops through all lines
                #print(line.strip()[1:-1])
                if label == line.strip()[1:-1]: # finds :[label]:
                    if found:
                        print(f"assembler.py: Duplicate label name: {label}", file=sys.stderr)
                        sys.exit(1)
                        return
                    encodedCommand[1] = valueConversion(allLines.index(line)) #stores the line of the command.
                    found = True
                
            if found == False:
                print(f"assembler.py: Undefined label name: {label}", file=sys.stderr)
                sys.exit(1)
                return
            
            encodedCommand[2] = bin(int(bytes[2])) #value1
            encodedCommand[3] = bin(int(bytes[3])) #value2
            
        case "CALL": # dont know how yet -> use os.fork()
            encodedCommand[0] = bin(0b00100000)
            encodedCommand[1] = bin(0b0) #storage for child process exit code
            encodedCommand[2] = bin(0b0) #string for child process name??????
            encodedCommand[3] = bin(0b0)

        case "EXIT":
            encodedCommand[0] = bin(0b00100001)
            encodedCommand[1] = valueConversion(bytes[1]) #exit code
            encodedCommand[2] = bin(0b0)
            encodedCommand[3] = bin(0b0)

        case _:
            print("assembler.py: Malformed instruction on line {lineNum}", file=sys.stderr)
            sys.exit(1)

    return encodedCommand

def main():
    
    """
    python3 assembler.py --hex testing.prog testing.hex
    python3 assembler.py testing.prog testing.bin
    """

    instCount = 0 #instructionCount
    memory = [] # saved instructions

    if sys.argv[1] == "--hex": # sets the file names for read and returns depending if --hex label exists
        programFile = sys.argv[2]
        returnFile = sys.argv[3]
    else:
        programFile = sys.argv[1]
        returnFile = sys.argv[2]

    # the start of the executable file. used for checking if the file is stdchip executable
    memory.append(valueConversion('0xF2'))
    memory.append(valueConversion('0xC3'))
    memory.append(valueConversion('0x38'))
    memory.append(valueConversion('0x01'))

    try:
        with open(programFile, 'r') as openFile:
            allLines = openFile.readlines()

            for line in allLines: #comment clearing loop to return lines without comments
                if line[0:2] == "//":
                    allLines.remove(line);   

            for line in allLines:

                if line.strip()[0] == ":" and line.strip()[-1] == ":": # finds labels and ignores (does not encode into memory.)
                    continue

                else:
                    binCode = assembler(line.strip(),allLines, instCount) #shoves line into assembler and returns a list[4] of the converted instr.
                    for i in range(len(binCode)):
                        memory.append(binCode[i]) # appends the binary instr. into the memory

                    instCount += 1 # indexes instruction count

        #print(memory)
        
        if sys.argv[1] == "--hex":
            try:
                with open(returnFile, "w") as openFile:

                    byteCount = 4 #ignore first 4 bytes (magic bytes and stuff)

                    for line in allLines:

                        if line.strip()[0] == ":" and line.strip()[-1] == ":": # finds labels and ignores (does not encode into memory.)
                            continue

                        hexValues = [f"{int(b, 2):02X}" for b in memory[byteCount:byteCount+4]] # formats hex values by counting bytes from memory (4-7, 8-11 etc)
                        hexString = "".join(hex for hex in hexValues) # joins hex values into a string

                        openFile.write(f"{line.strip()}: {hexString}\n") # writes line to file

                        byteCount+=4 # indexes the next 4 bytes of memory

                print(f'Finished compiling. File {returnFile} has been created.')

            except PermissionError: # inside try -> cannot edit existing file
                print(f"assembler.py: File {returnFile} cannot be written to.", file=sys.stderr)
                sys.exit(1)

        else:

            try:
                with open(returnFile, "wb") as openFile:

                    openFile.write(bytearray(int(b, 2) for b in memory)) # writes all bytes into file from memory
                
                print(f'Finished compiling. File {returnFile} has been created.')

            except PermissionError: # inside try -> cannot edit existing bin file
                print(f"assembler.py: File {returnFile} cannot be written to.", file=sys.stderr)
                sys.exit(1)

    except FileNotFoundError:
        print(f"assembler.py: File {programFile} does not exist.", file=sys.stderr)
        sys.exit(1)

    except PermissionError: # outside try -> reading file
        print(f"assembler.py: File {programFile} cannot be read.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()