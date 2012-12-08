import unittest

from snoboy import cpu, instructions


class Set(unittest.TestCase):
    def testSet(self):
        bit = 0
        for opcode in range(0xC0, 0xFF, 8):
            cpu.registers.B = 0
            instructions.set(opcode)
            self.assertEquals(cpu.registers.B, 1 << bit)
            bit = bit + 1
