from nose.tools import eq_

from snoboy import cpu, instructions


def test_set():
    bit = 0
    for opcode in range(0xC0, 0xFF, 8):
        cpu.registers.B = 0
        instructions.set(opcode)
        yield eq_, cpu.registers.B, 1 << bit
        bit = bit + 1
