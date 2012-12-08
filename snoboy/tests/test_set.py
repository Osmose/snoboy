from snoboy.instructions import set
import unittest

class Set(unittest.TestCase):
	def testSet(self):
		bit = 0
		for val in range(0xC0, 0xFF, 8):
			cpu.registers.b = 0
			set(opcode)
			self.assertEquals(cpu.registers.b, 1<<bit)
			bit = bit + 1

if __name__ == "__main__":
	unittest.main();