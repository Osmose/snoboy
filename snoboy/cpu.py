from ctypes import c_ubyte


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
        upper = value >> 8
        lower = value

    return property(get, set)


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
registers = Registers()
