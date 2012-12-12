from array import array
from itertools import repeat

from snoboy import cart

main_ram = array('B',  repeat(0, 0x2000))


def read(loc):
    """Read a location in memory."""
    if loc <= 0x00FF:
        # Restart and Interrupt Vectors
        return cart.cart_data[loc]
    elif loc <= 0x014F:
        # Cartridge Header Area
        return cart.cart_data[loc]
    elif loc <= 0x3FFF:
        # Cartridge ROM Bank 0
        return cart.cart_data[loc]
    elif loc <= 0x7FFF:
        # Cartridge ROM Switchable Bank
        pass
    elif loc <= 0x97FF:
        # Character RAM
        pass
    elif loc <= 0x9BFF:
        # BG Map Data 1
        pass
    elif loc <= 0x9FFF:
        # BG Map Data 2
        pass
    elif loc <= 0xBFFF:
        # Cartridge RAM
        pass
    elif loc <= 0xCFFF:
        # Internal RAM Bank 0
        # 0xD000 = Internal RAM Switchable Bank (CGB only)
        return main_ram[loc - 0xC000]
    elif loc <= 0xFDFF:
        # Echo RAM
        pass
    elif loc <= 0xFE9F:
        # OAM RAM
        pass
    elif loc <= 0xFEFF:
        # Unusable memory
        pass
    elif loc <= 0xFF7F:
        # Hardware I/O Registers
        pass
    elif loc <= 0xFFFE:
        # Zero Page
        pass
    elif loc == 0xFFFF:
        # Interrupt enable flag
        pass
    else:
        raise IndexError


def write(loc, value):
    """Write to a location in memory."""
    if loc <= 0x00FF:
        # Restart and Interrupt Vectors
        pass
    elif loc <= 0x014F:
        # Cartridge Header Area
        pass
    elif loc <= 0x3FFF:
        # Cartridge ROM Bank 0
        pass
    elif loc <= 0x7FFF:
        # Cartridge ROM Switchable Bank
        pass
    elif loc <= 0x97FF:
        # Character RAM
        pass
    elif loc <= 0x9BFF:
        # BG Map Data 1
        pass
    elif loc <= 0x9FFF:
        # BG Map Data 2
        pass
    elif loc <= 0xBFFF:
        # Cartridge RAM
        pass
    elif loc <= 0xCFFF:
        # Internal RAM Bank 0
        # 0xD000 = Internal RAM Switchable Bank (CGB only)
        main_ram[loc - 0xC000] = value
    elif loc <= 0xFDFF:
        # Echo RAM
        pass
    elif loc <= 0xFE9F:
        # OAM RAM
        pass
    elif loc <= 0xFEFF:
        # Unusable memory
        pass
    elif loc <= 0xFF7F:
        # Hardware I/O Registers
        pass
    elif loc <= 0xFFFE:
        # Zero Page
        pass
    elif loc == 0xFFFF:
        # Interrupt enable flag
        pass
    else:
        raise IndexError
