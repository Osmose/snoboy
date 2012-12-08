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
    while (opcode > 0x07):
        opcode -= 0x07
        bit = bit + 1

    if (opcode == 0x00):
        reg = cpu.registers.B
    elif (opcode == 0x01):
        reg = cpu.registers.C
    elif (opcode == 0x02):
        reg = cpu.registers.D
    elif (opcode == 0x03):
        reg = cpu.registers.E
    elif (opcode == 0x04):
        reg = cpu.registers.H
    elif (opcode == 0x05):
        reg = cpu.registers.L
    elif (opcode == 0x06):
        reg = cpu.registers.HL
    elif (opcode == 0x07):
        reg = cpu.registers.A

    reg = reg | (1 >> bit)
