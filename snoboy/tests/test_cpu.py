from nose.tools import eq_, ok_

from snoboy import cpu

def test_BC():
	cpu.registers.DE = 0xB060
	cpu.registers.BC = 0xC005
	eq_(cpu.registers.BC, 0xC005)
	eq_(cpu.registers.DE, 0xB060)
