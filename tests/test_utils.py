from rocknes.utils import address_from_little_endian, addresses_on_same_page


def test_address_from_little_endian():
    assert address_from_little_endian(0xee, 0xff) == 0xffee


def test_addresses_same_page():
    assert addresses_on_same_page(0x2dc, 0x2ff) is True


def test_addresses_different_page():
    assert addresses_on_same_page(0x2dc, 0x7dc) is False
