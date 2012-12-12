from nose.tools import eq_, ok_

from snoboy import cpu, instructions, memory

def test_jmp():
    # write address 0xC005
    memory.write(0xC000, 0x05)
    memory.write(0xC001, 0xC0)

    eq_(memory.read(0xC000), 0x05)
    eq_(memory.read(0xC001), 0xC0)


    cpu.registers.PC = 0xC000
    instructions.jp_a16()
    eq_(cpu.registers.PC, 0xC005)