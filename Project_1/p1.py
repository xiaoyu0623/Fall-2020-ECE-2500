import sys
import math

# hex to binary converter
def hex_binary(line):
    result = "{0:08b}".format(int(line,16))
    if len(result) < 32:
        n = 32 - len(result)
        for i in range (n):
            result = '0' + result
    return result

# binary to decimal converter
def binary_decimal(line):
    result = int(line, 2)
    return result

# dictonary for register name
def create_dict():
    Dict = {}
    Dict[0] = '$zero'
    Dict[1] = 'at'
    Dict[2] = '$v0'
    Dict[3] = '$v1'
    Dict[4] = '$a0'
    Dict[5] = '$a1'
    Dict[6] = '$a2'
    Dict[7] = '$a3'
    Dict[8] = '$t0'
    Dict[9] = '$t1'
    Dict[10] = '$t2'
    Dict[11] = '$t3'
    Dict[12] = '$t4'
    Dict[13] = '$t5'
    Dict[14] = '$t6'
    Dict[15] = '$t7'
    Dict[16] = '$s0'
    Dict[17] = '$s1'
    Dict[18] = '$s2'
    Dict[19] = '$s3'
    Dict[20] = '$s4'
    Dict[21] = '$s5'
    Dict[22] = '$s6'
    Dict[23] = '$s7'
    Dict[24] = '$t8'
    Dict[25] = '$t9'
    Dict[26] = '$k0'
    Dict[27] = '$k1'
    Dict[28] = '$gp'
    Dict[29] = '$sp'
    Dict[30] = '$fp'
    Dict[31] = '$ra'
    return Dict

# ask input file name
print('Enter file name to open:')
filename = input()

file1 = open(filename,'r')
input_file = [] # save input file as binary
input_file_orig = [] # save input file as hex
goal_address_jump = [] # address jumped
for line in file1:
    #print(line)
    input_file_orig.append(line)
    if (line[0].isdigit() == False) and (line[0]!= 'a') and (line[0] != 'b') and (line[0] != 'c') and (line[0] != 'd') and (line[0] != 'e') and (line[0] != 'f'):
        #print("IN")
        error_index = input_file_orig.index(line)
        op_command = input_file_orig[error_index]
        print("Cannot disassemble " + str(op_command).rstrip() + " at line "+ str(error_index + 1))
    else:
        bin_line = hex_binary(line)
        input_file.append(bin_line)
#print (input_file)

# signed binary to decimal
def signed_binary_decimal(line):
    line_new = ""
    #print ("Befor: "+ line)
    for i in range (len(line)):
        #print(str(i) + "  "+str(line[i]))
        if line[i] == str(0):
            line_new = line_new + "1"
        else:
            line_new = line_new + "0"
    line_new = str(int(line_new) + 1)
    result = int(line_new, 2) * (-1)
    #print(result)
    return result

# Add instruction
def add(line, register_dict):
    #print("ADD")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        add"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Addu instruction
def addu(line, register_dict):
    #print("ADDU")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        addu"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# And instruction
def logic_and(line, register_dict):
    #print("AND")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        and"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Or instruction
def logic_or(line, register_dict):
    #print("OR")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        or"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Nor instruction
def logic_nor(line, register_dict):
    #print("NOR")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        nor"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Slt instruction
def slt(line, register_dict):
    #print("SLT")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        slt"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Sltu instruction
def sltu(line, register_dict):
    #print("SLTU")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        sltu"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Sll instruction
def sll(line, register_dict):
    #print("SLL")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        sll"
    rd = binary_decimal(rd)
    rt = binary_decimal(rt)
    if (shamt[0] == str(0)):
        shamt = binary_decimal(shamt)
    else:
        shamt = signed_binary_decimal(shamt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rt] + ", " + str(shamt)
    print (command)
    return command

# Srl instruction
def srl(line, register_dict):
    #print("SRL")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        srl"
    rd = binary_decimal(rd)
    rt = binary_decimal(rt)
    if (shamt[0] == str(0)):
        shamt = binary_decimal(shamt)
    else:
        shamt = signed_binary_decimal(shamt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rt] + ", " + str(shamt)
    print (command)
    return command

# Sub instruction
def sub(line, register_dict):
    #print("SUB")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        sub"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Subu instruction
def subu(line, register_dict):
    #print("SUBU")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21] 
    shamt = line[21:26]
    funct = line[26:32]
    command = "        subu"
    rd = binary_decimal(rd)
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    command = command + "      " + register_dict[rd] + ", " + register_dict[rs] + ", " + register_dict[rt]
    print (command)
    return command

# Addi instruction
def addi(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        addi"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Addiu instruction
def addiu(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        addiu"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command
    
# Andi instruction    
def andi(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        andi"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Beq instruction
def beq(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        beq"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    #print("Imm: " + str(imm[0]))
    if (imm[0] == str(0)):
        imm = binary_decimal(imm)
    else:
        imm = signed_binary_decimal(imm)
    #print("Imm: " + str(imm))
    index = input_file.index(line) + 1
    goal_adress = hex(4 *(index + imm))[2:]
    #print ("Goal: " + str(goal_adress))
    if len(goal_adress) < 4:
        n = 4 - len(goal_adress)
        for i in range (n):
            goal_adress = '0' + goal_adress
    goal_address_jump.append(goal_adress)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", Addr_" + str(goal_adress)
    print(command)
    return command

# Bne instruction
def bne(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        bne"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    #print (imm)
    if (imm[0] == 0):
        imm = binary_decimal(imm)
    else:
        imm = signed_binary_decimal(imm)
    #print("Imm: " + str(imm))
    index = input_file.index(line) + 1
    goal_adress = hex(4 *(index + imm))[2:]
    #print ("Goal: " + str(goal_adress))
    if len(goal_adress) < 4:
        n = 4 - len(goal_adress)
        for i in range (n):
            goal_adress = '0' + goal_adress
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", Addr_" + str(goal_adress)
    print(command)
    return command

# Lbu instruction
def lbu(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        lbu"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Lhu instruction
def lhu(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        lhu"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# LL instruction
def ll(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        ll"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Lui instruction
def lui(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        lui"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + str(imm)
    print(command)
    return command

# Lw instruction
def lw(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        lw"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + str(imm) + "(" + register_dict[rs] + ")"
    print(command)
    return command

# ori instruction
def ori(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        ori"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# slti instruction
def slti(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        slti"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# sltiu instruction
def sltiu(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        sltiu"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Sb instruction
def sb(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        sb"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Sc instruction
def sc(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        sc"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Sh instruction
def sh(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        sh"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + register_dict[rs] + ", " + str(imm)
    print(command)
    return command

# Sw instruction
def sw(line, register_dict):
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    imm = line[16:32]
    command = "        sw"
    rs = binary_decimal(rs)
    rt = binary_decimal(rt)
    imm = binary_decimal(imm)
    command = command + "     " + register_dict[rt] + ", " + str(imm) + "(" + register_dict[rs] + ")"
    print(command)
    return command

# R_type instructions
def R_Format(line, register_dict):
    #print("R")
    opcode = line[0:6]
    rs = line[6:11]
    rt = line[11:16]
    rd = line[16:21]
    shamt = line[21:26]
    funct = line[26:32]
    if funct == "100000":
        command = add(line, register_dict)
    elif funct == "100001":
        command = addu(line, register_dict)
    elif funct == "100100":
        command = logic_and(line, register_dict)
    elif funct == "100101":
        command = logic_or(line, register_dict)
    elif funct == "100111":
        command = logic_nor(line, register_dict)
    elif funct == "101010":
        command = slt(line, register_dict)
    elif funct == "101011":
        command = sltu(line, register_dict)
    elif funct == "000000":
        command = sll(line, register_dict)
    elif funct == "000010":
        command = srl(line, register_dict)
    elif funct == "100010":
        command = sub(line, register_dict)
    elif funct == "100011":
        command = subu(line, register_dict)
    else:
        error_index = input_file.index(line)
        op_command = input_file_orig[error_index]
        print("Cannot disassemble " + str(op_command) + " at line "+ str(error_index + 1))
        return 0
    return command

# I_type instructions
def I_Format(line, register_dict):
    #print("I")
    opcode = line[0:6]
    if opcode == "001000":
        command = addi(line, register_dict)
    elif opcode == "001001":
        command = addiu(line, register_dict)
    elif opcode == "001100":
        command = andi(line, register_dict)
    elif opcode == "000100":
        command = beq(line, register_dict)
    elif opcode == "000101":
        command = bne(line, register_dict)
    elif opcode == "100100":
        command = lbu(line, register_dict)
    elif opcode == "100101":
        command = lhu(line, register_dict)
    elif opcode == "110000":
        command = ll(line, register_dict)
    elif opcode == "001111":
        command = lui(line, register_dict)
    elif opcode == "100011":
        command = lw(line, register_dict)
    elif opcode == "001101":
        command = ori(line,register_dict)
    elif opcode == "001010":
        command = slti(line,register_dict)
    elif opcode == "001011":
        command = sltiu(line, register_dict)
    elif opcode == "101000":
        command = sb(line, register_dict)
    elif opcode == "111000":
        command = sc(line, register_dict)
    elif opcode == "101001":
        command = sh(line,register_dict)
    elif opcode == "101011":
        command = sw(line,register_dict)
    else:
        error_index = input_file.index(line)
        op_command = input_file_orig[error_index]
        print("Cannot disassemble " + str(op_command).rstrip() + " at line "+ str(error_index + 1))
        return 0
    return command


# Create dictionary for register name
register_dict = create_dict()
add_address = False # check if need print address
file1 = open(filename,'r')
output_file = []
for line in file1:
    #print(line)
    if (line[0].isdigit() == True) or (line[0] == 'a') or (line[0] == 'b') or (line[0] == 'c') or (line[0] == 'd') or (line[0] == 'e') or (line[0] == 'f'):
        bin_line = hex_binary(line)
    #print(bin_line)
    if bin_line[0:6] == "000000":
        result = R_Format(bin_line, register_dict)
        output_file.append(result)
    else:
        result = I_Format(bin_line, register_dict)
        if (bin_line[0:6] == "000100") or ( bin_line[0:6] == "000101"):
            add_address = True
        output_file.append(result)

# Need print address
if add_address == True:
    #print(goal_address_jump)
    for address in goal_address_jump:
        goal_index = int((int(address, 16))/4)
        #print(goal_index)
        output_file.insert(goal_index, str('Addr_' + address))


# Save to file
print('Enter file name to save:')
file_save = input()
with open(file_save, 'w') as filehandle:
    for listitem in output_file:
        filehandle.write(listitem + '\n')









        
        
    