from ctypes import c_ubyte, c_ushort
from snoboy import memory

# how many cycles we've executed
ticks = 0

operations = {}

def doInstruction():
    opcode = memory.read(registers.PC)
    registers.PC += 1

    if opcode in operations:
        print "Instruction: %s (%x)" % (operations[opcode].__name__, opcode)
        operations[opcode]()
    else:
        raise NotImplementedError("Instruction 0x%x not implemented"%opcode)

def add_ticks(t):
    global ticks
    ticks = ticks + t


def _register16(default=0):
    """Create a property around a c_ushort"""
    _value = c_ushort(default)

    def get(self):
        return _value.value

    def set(self, value):
        _value.value = value

    return property(get, set)


def _register(default=0):
    """Create a property around a c_ubyte."""
    _value = c_ubyte(default)

    def get(self):
        return _value.value

    def set(self, value):
        _value.value = value

    return property(get, set)


def _compound_register(upper, lower):
    """Return a property that provides 16-bit access to two registers."""
    def get(self):
        return (upper.fget(None) << 8) | lower.fget(None)

    def set(self, value):
        upper.fset(None, value >> 8)
        lower.fset(None, value)

    return property(get, set)

def _indirect_register(reg):
    """Return a property that provides 8-bit access to the memory location pointed to by reg"""
    def get(self):
        return memory.read(reg.fget(None))
    def set(self, value):
        memory.write(reg.fget(None), value)
    return property(get,set)

class Registers(object):
    A = _register()
    F = _register()
    B = _register()
    C = _register()
    D = _register()
    E = _register()
    H = _register()
    L = _register()
    BC = _compound_register(B, C)
    DE = _compound_register(D, E)
    HL = _compound_register(H, L)

    iHL = _indirect_register(HL)

    SP = _register16()
    PC = _register16()

    def __getitem__(self, index):
        return getattr(self, index)

    def __setitem__(self, index, value):
        setattr(self, index, value)
registers = Registers()

def reset():
    #initialize to default value
    registers.PC = 0x0100
    registers.SP = 0xFFFE
    registers.A = 0
    registers.F = 0
    registers.B = 0
    registers.C = 0
    registers.D = 0
    registers.E = 0
    registers.H = 0
    registers.L = 0