from nose.tools import eq_

from snoboy import cpu, instructions


def test_set():
    for key,val in instructions.SET_REGISTER_MAP.items():
        bit = 0
        for opcode in range(0xC0+key, 0xFF+1, 8):
            cpu.registers[val] = 0
            instructions.set(opcode)
            yield eq_, cpu.registers[val], 1 << bit
            bit = bit + 1
