from nose.tools import eq_, ok_

from snoboy import cpu, instructions


def test_set():
    cpu.registers.HL = 0xC000
    for key, val in instructions.REGISTER_MAP.items():
        bit = 0
        for opcode in range(0xC0 + key, 0xFF + 1, 8):
            print "testing set %s %x %x\n" %(val, opcode, cpu.registers[val])
            cpu.registers[val] = 0
            instructions.set(opcode)
            yield eq_, cpu.registers[val], 1 << bit
            bit = bit + 1


def test_res():
    for key, val in instructions.REGISTER_MAP.items():
        bit = 0
        for opcode in range(0x80 + key, 0xBF + 1, 8):
            cpu.registers[val] = 0xFF
            instructions.res(opcode)
            yield ok_, not (cpu.registers[val] & (1 << bit))
            bit = bit + 1