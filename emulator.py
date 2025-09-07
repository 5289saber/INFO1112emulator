import sys
import os

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
        return ord(value)
    elif header == "0" and len(value) > 1:
        # bin, hex, oct
        numType = value[0:2]
        match numType:
            case "0b":
                return int(value[2:],2)
            case "0x":
                return int(value[2:],16)
            case "0o":
                return int(value[2:],8)
    else:
        # decimal
        return int(value)

def main(fileName=sys.argv[1],memory=[0]*256,inst=[0]*256):
    #fileName = sys.argv[1]
    #print(memory)
    pc = 0
    #memory = [0]*256 # 256 memory bytes

    try:

        with open(fileName, 'rb') as openFile:
            fileContents = openFile.read()

            for i in range(4, len(fileContents)):
                #print(f"{[b for b in fileContents[i:i+4]]}")
                inst[i-4] = fileContents[i]

                #pc += 4
            header = [hex(b) for b in fileContents[0:4]]

            if header != [hex(0xf2), hex(0xc3), hex(0x38), hex(0x1)]:
                print(f"emulator.py: File {fileName} is not a valid StdChip executable.", file=sys.stderr)
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

    #print(f"{fileName} memory -----------------------------")
    #print(inst)
    while True:
        if instNum > 256:
            break
        
        #print(memory)
        MacInst = inst[pc:pc+4]
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
                memory[MacInst[1]] = (memory[MacInst[2]] + memory[MacInst[3]])%256

            case "SUB":
                #print(f"instruction {instNum}: sub")
                memory[MacInst[1]] = (memory[MacInst[2]] - memory[MacInst[3]])%256
                
            case "READ":
                #print(f"instruction {instNum}: read")
                if bin(MacInst[2]) == "0b1":
                    #print("read number")
                    number = valueConversion(input())

                    memory[MacInst[1]] = number

                elif bin(MacInst[2]) == "0b10":
                    #print("read string")
                    end = MacInst[1] + MacInst[3]
                    start = MacInst[1]
                    string = input()
                    index = 0

                    for i in range(start, end, 1):
                        if index > len(string):
                            break
                        if (string[index] == "\\" and string[index+1] == "n") or (string[index] == "\\" and string[index+1] == "0"):
                            break
                        memory[i] = ord(string[index])
                        index+=1

            case "PUT":
                #print(f"instruction {instNum}: put")
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
                pc = int(MacInst[1]) * 4
                continue
            case "JEQ":
                #print(f"instruction {instNum}: jump eq")
                if memory[MacInst[2]] == memory[MacInst[3]]:
                    pc = int(MacInst[1]) * 4
                    continue
            case "JGT":
                #print(f"instruction {instNum}: jump gt")
                if memory[MacInst[2]] > memory[MacInst[3]]:
                    #print(MacInst[1])
                    pc = int(MacInst[1]) * 4
                    # print(pc)
                    continue
            case "CALL":
                #print(f"instruction {instNum}: call")
                #print(memory)
                index = MacInst[2]

                childFileName = ""

                while (memory[index] != 0):
                    #print(memory[index])
                    childFileName += chr(memory[index])
                    index += 1
                #print(fileName)

                pid = os.fork()
                
                if pid == 0: #child
                    #os.execvp("python3", ["python3", "emulator.py", f"{fileName}"])
                    print("mmmm child")
                    main(childFileName,memory=memory)
                elif pid == 1: #error in child
                    print(f"(child) emulator.py: child {pid} encountered error.", file=sys.stderr)
                    sys.exit(1)
                else: #parent
                    childPID, status = os.waitpid(pid, 0)
                    exitCode = (status >> 8) & 0xFF

                #print(f"{childPID}, {exitCode}")
                memory[MacInst[1]] = exitCode #exit code

            case "EXIT":
                #print(f"instruction {instNum}: exit with code {memory[MacInst[1]]}")
                #print(memory) #testing output!
                sys.exit(memory[MacInst[1]])
                break
            case _:
                #print("no instructions left")
                #print(memory)
                sys.exit(0)
                break
            
        pc += 4
        instNum += 1
    
    #print(memory)
    


if __name__ == "__main__":
    main()