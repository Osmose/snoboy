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


SET_REGISTER_MAP = {
    0x00: 'B',
    0x01: 'C',
    0x02: 'D',
    0x03: 'E',
    0x04: 'H',
    0x05: 'L',
    0x07: 'A'
}


def set(opcode):
    bit = 0
    opcode -= 0xc0
    while (opcode >= 0x08):
        opcode -= 0x08
        bit = bit + 1

    if opcode == 0x06:
        raise NotImplementedError("set n,(HL) not implemented yet")
    else:
        register_name = SET_REGISTER_MAP[opcode]
        cpu.registers[register_name] = cpu.registers[register_name] | (1 << bit)
