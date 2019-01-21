def address_from_little_endian(lsb, msb):
    return (msb << 8) | lsb


def addresses_on_same_page(address_1, address_2):
    return address_1 & 0xff00 == address_2 & 0xff00
