from nose.tools import eq_, ok_

from snoboy import memory, cart

def test_cart():
    cart.loadCart('sml.gb')

    # All carts should have this in their header(amongst other things)
    eq_(memory.read(0x100), 0x00)
    eq_(memory.read(0x101), 0xC3)
    eq_(memory.read(0x102), 0x50)
    eq_(memory.read(0x103), 0x01)