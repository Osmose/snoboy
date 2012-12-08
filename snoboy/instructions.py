from snoboy import cpu

"""
Set a bit in a register
"""

# 0xc0 is SET 0,B
# 0xc1 is SET 0,C
# followed by D,E,H,L,HL,A

# 0xc8 is SET 1,B
# ...

# 0xD0 is SET 2, B
# 0xD8 is SET 3, B
# 0xE0 is SET 4, B
# 0xE8 is SET 4, B
# 0xF0 is SET 6, B
# 0xF8 is SET 7, B


def set(opcode):
    bit = 0
    reg = 0
    opcode -= 0xc0
    while (opcode >= 0x08):
        opcode -= 0x08
        bit = bit + 1

    if (opcode == 0x00):
        cpu.registers.B = cpu.registers.B | (1<<bit)
    elif (opcode == 0x01):
        cpu.registers.C = cpu.registers.C | (1<<bit)
    elif (opcode == 0x02):
        cpu.registers.D = cpu.registers.D | (1<<bit)
    elif (opcode == 0x03):
        cpu.registers.E = cpu.registers.E | (1<<bit)
    elif (opcode == 0x04):
        cpu.registers.H = cpu.registers.H | (1<<bit)
    elif (opcode == 0x05):
        cpu.registers.L = cpu.registers.L | (1<<bit)
    elif (opcode == 0x06):
        cpu.registers.HL = cpu.registers.HL | (1<<bit)
    elif (opcode == 0x07):
        cpu.registers.A = cpu.registers.A | (1<<bit)
