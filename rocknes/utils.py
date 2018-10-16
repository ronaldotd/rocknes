def address_from_little_endian(lsb, msb):
    return (msb << 8) | lsb
