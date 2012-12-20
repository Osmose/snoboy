from nose.tools import eq_, ok_

from snoboy import cpu, memory

def test_BC():
	cpu.registers.DE = 0xB060
	cpu.registers.BC = 0xC005
	eq_(cpu.registers.BC, 0xC005)
	eq_(cpu.registers.DE, 0xB060)

def test_iHL():
	cpu.registers.HL = 0xC000
	memory.write(0xC000,0x54)
	eq_(cpu.registers.iHL, 0x54)

	cpu.registers.iHL = 0x32
	eq_(memory.read(0xC000), 0x32)
