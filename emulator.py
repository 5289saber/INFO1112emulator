import sys

"""
OPCODES
"""
opcodes = {
    1:  "SET",
    2:  "MOV",
    3:  "ADD",
    4:  "SUB",
    8:  "READ",
    9:  "PUT",
    16: "JMP",
    17: "JEQ",
    18: "JGT",
    32: "CALL",
    33: "EXIT",
}

def valueConversion(value: str):
    """
    takes value:str\n
    the value inputted can be binary, decimal, hexadecimal, octal and ASCII
    """
    header = value[0]
    if header.isalpha():
        # ASCII
        return bin(ord(value))
    elif header == "0" and len(value) > 1:
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

def main(args: list[str]):
    fileName = sys.argv[1]

    pc = 0
    memory = [0]*256 # 256 memory bytes

    try:

        with open(fileName, 'rb') as openFile:
            fileContents = openFile.read()

            for i in range(4, len(fileContents)):
                #print(f"{[b for b in fileContents[i:i+4]]}")
                memory[i-4] = fileContents[i]

                #pc += 4
            header = [hex(b) for b in fileContents[0:4]]

            if header != [hex(0xf2), hex(0xc3), hex(0x38), hex(0x1)]:
                print("this is not StdChip executable file")
                sys.exit(1)
                return
            
            """for i in range(0, len(memory), 4):
                print(memory[i:i+4])"""
            
            instNum = 0 # instruction count

    except FileNotFoundError:
        print(f"emulator.py: File {fileName} does not exist.", file=sys.stderr)
        sys.exit(1)
        return
    
    except PermissionError:
        print(f"emulator.py: File {fileName} cannot be read.", file=sys.stderr)
        sys.exit(1)
        return

    
    while True:
        if instNum > 256:
            break

        MacInst = memory[pc:pc+4]
        opcode = MacInst[0]
        #print(MacInst)
        #print(memory[5:9])
        

        match opcodes.get(opcode):
            case "SET":
                #print(f"instruction {instNum}: set")
                memory[MacInst[1]] = MacInst[2]

            case "MOV":
                #print(f"instruction {instNum}: move")
                memory[MacInst[1]] = memory[MacInst[2]]

            case "ADD":
                #print(f"instruction {instNum}: add")
                memory[MacInst[1]] = memory[MacInst[2]] + memory[MacInst[3]]

            case "SUB":
                #print(f"instruction {instNum}: sub")
                memory[MacInst[1]] = memory[MacInst[2]] - memory[MacInst[3]]
                
            case "READ":
                #print(f"instruction {instNum}: read")
                if MacInst[2] == "0b1":
                    #print("read number")
                    number = valueConversion(input())

                    memory[MacInst[1]] = number

                elif MacInst[2] == "0b10":
                    #print("read string")
                    end = MacInst[1] + MacInst[3]
                    start = MacInst[1]
                    string = input()
                    index = 0

                    for i in range(start, end, 1):
                        if string[index] == "\n" or string[index] == "\0":
                            break
                        memory[i] = int(ord(string[index]),2)

            case "PUT":
               # print(f"instruction {instNum}: put")
                if bin(MacInst[2]) == "0b10000000":
                    #print("text at address")
                    start = MacInst[1]
                    end = MacInst[3] + MacInst[1]

                    for i in range(start, end, 1):
                        print(chr(memory[i]),end="")

                else:
                    #print("value at address")
                    match chr(MacInst[2]):
                        case "b":
                            #print("binary num")
                            print(memory[MacInst[1]],end="")
                        case "o":
                            #print("octal num")
                            print(oct(memory[MacInst[1]]),end="")
                        case "d":
                            #print("decimal num")
                            print(int(memory[MacInst[1]]),end="")
                        case "h":
                            #print("hexadecmial num")
                            print(hex(memory[MacInst[1]]),end="")

            case "JMP":
                #print(f"instruction {instNum}: jump")
                pc = int(MacInst[1])
                continue
            case "JEQ":
                #print(f"instruction {instNum}: jump eq")
                if memory[MacInst[2]] == memory[MacInst[3]]:
                    pc = int(MacInst[1])
                    continue
            case "JGT":
                #print(f"instruction {instNum}: jump gt")
                if memory[MacInst[2]] > memory[MacInst[3]]:
                    #print(MacInst[1])
                    pc = int(MacInst[1]) * 4
                   # print(pc)
                    continue
            case "CALL":
                print(f"instruction {instNum}: call")
            case "EXIT":
                #print(f"instruction {instNum}: exit")
                sys.exit(MacInst[1])
                break
            case _:
                #print("no instructions left")
                break
            
        pc += 4
        instNum += 1
    print(memory)


if __name__ == "__main__":
    main(sys.argv[1:])


        