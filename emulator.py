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


def main(args: list[str]):
    fileName = sys.argv[1]

    pc = 0
    memory = [0]*256 # 256 memory bytes

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

    while True:
        if instNum > 256:
            break

        MacInst = memory[pc:pc+4]
        opcode = MacInst[0]
        

        match opcodes.get(opcode):
            case "SET":
                print(f"instruction {instNum}: set")
            case "MOV":
                print(f"instruction {instNum}: move")
            case "ADD":
                print(f"instruction {instNum}: add")
            case "SUB":
                print(f"instruction {instNum}: sub")
            case "READ":
                print(f"instruction {instNum}: read")
            case "PUT":
                print(f"instruction {instNum}: put")
            case "JMP":
                print(f"instruction {instNum}: jump")
            case "JEQ":
                print(f"instruction {instNum}: jump eq")
            case "JGT":
                print(f"instruction {instNum}: jump gt")
            case "CALL":
                print(f"instruction {instNum}: call")
            case "EXIT":
                print(f"instruction {instNum}: exit")
            case _:
                print(f"no instructions left")
                break
            
        pc += 4
        instNum += 1


if __name__ == "__main__":
    main(sys.argv[1:])


        