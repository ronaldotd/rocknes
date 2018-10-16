from rocknes.utils import address_from_little_endian


def test_address_from_little_endian():
    assert address_from_little_endian(0xee, 0xff) == 0xffee
