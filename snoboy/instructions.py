from snoboy import cpu, memory

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


REGISTER_MAP = {
    0x00: 'B',
    0x01: 'C',
    0x02: 'D',
    0x03: 'E',
    0x04: 'H',
    0x05: 'L',
    0x06: 'iHL',
    0x07: 'A'
}


def _bit_op(base_opcode):
    def decorator(op):
        def func(opcode):
            bit = 0
            opcode -= base_opcode
            while (opcode >= 0x08):
                opcode -= 0x08
                bit = bit + 1

            if opcode == 0x06:
                cpu.add_ticks(16)
            else:
                cpu.add_ticks(8)

            register = REGISTER_MAP[opcode]
            cpu.registers[register] = op(cpu.registers[register], bit)
        return func
    return decorator


# 0xCB 0xC0-0xFF
@_bit_op(0xc0)
def set(register_value, bit):
    return register_value | (1 << bit)

# 0xCB 0x80 - 0xBF
@_bit_op(0x80)
def res(register_value, bit):
    return register_value & ~(1 << bit)

# 0x40-0x7F
def ld8(opcode):
    def helper():
        destreg = 0
        opcode -= 0x40
        while(opcode >= 0x08):
            opcode -= 0x08
            destreg += 1

        cpu.add_ticks(4)
        # These access memory, and take longer
        if (opcode == 0x06 or destreg == 0x06):
            cpu.add_ticks(4)

        dest = REGISTER_MAP[destreg]
        cpu.registers[dest] = cpu.registers[REGISTER_MAP[opcode]]
    return helper
for i in range(0x40, 0x80):
    if i == 0x76: continue # HLT instruction
    cpu.operations[i] =ld8(i)

#0x06,0x16,0x26,0x36, 0x0e, 0x1e, 0x2e, 0x3e
_d8regmap = {
    0x06: 'B',
    0x16: 'D',
    0x26: 'H',
    0x36: 'iHL', # indirect memory access
    0x0e: 'C',
    0x1e: 'E',
    0x2e: 'L',
    0x3e: 'A'
}
def ld_d8(opcode):
    def helper():
        cpu.add_ticks(8)

        # memory access costs 4 ticks more
        if opcode == 0x36:
            cpu.add_ticks(4)
        # get the register, and read in the opcode 'argument'
        reg = _d8regmap[opcode]
        cpu.registers[reg] = memory.read(cpu.registers.PC +1)
        cpu.registers.PC += 1
    return helper
cpu.operations[0x06] = ld_d8(0x06)
cpu.operations[0x16] = ld_d8(0x16)
cpu.operations[0x26] = ld_d8(0x26)
cpu.operations[0x36] = ld_d8(0x36)
cpu.operations[0x0E] = ld_d8(0x0E)
cpu.operations[0x1E] = ld_d8(0x1E)
cpu.operations[0x2E] = ld_d8(0x2E)
cpu.operations[0x3E] = ld_d8(0x3E)

#0xe3
def ld_ic_a(): # LD (C), A
    cpu.add_ticks(8)
    memory.write(0xFF00 + cpu.registers.C, cpu.registers.A)
cpu.operations[0xE3] = ld_ic_a
#0xf3
def ld_a_ic(): # ld A,(C)
    cpu.add_ticks(8)
    cpu.registers.A = memory.read(0xFF00 + cpu.registers.C)
cpu.operations[0xf3] = ld_a_ic

#0xe0 LDH (n), A
def ldh_n_a():
    cpu.add_ticks(12)
    n = memory.read(cpu.registers.PC)
    cpu.registers.PC += 1
    memory.write(0xFF00+n, cpu.registers.A)
cpu.operations[0xE0] = ldh_n_a
#0xf0 LDH A,(n)
def ldh_a_n():
    cpu.add_ticks(12)
    n = memory.read(cpu.registers.PC)
    cpu.registers.PC += 1
    cpu.registers.A = memory.read(0xFF00+n)
cpu.operations[0xF0] = ldh_a_n


# 0x00
def nop():
    cpu.add_ticks(4)
    return
cpu.operations[0x00] = nop

# 0xC3 - Absolute jump to 16bit address
def jp_a16():
    cpu.add_ticks(16)
    lower = memory.read(cpu.registers.PC)
    upper = memory.read(cpu.registers.PC+1)
    jaddress = (upper << 8) | (lower & 0xFF)
    cpu.registers.PC = jaddress
    return
cpu.operations[0xC3] = jp_a16