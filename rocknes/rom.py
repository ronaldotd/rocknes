from array import array

from .exceptions import InvalidRom

ROM_BANK_SIZE = 16 * 1024
VROM_BANK_SIZE = 8 * 1024


class Rom:
    def __init__(self, rom_file_path):
        self._load_rom_file(rom_file_path)

    def _decode_header(self, header):
        conditions = (
            len(header) == 16,
            header[:4] == array('B', b'NES\x1a'),
            header[11:] == array('B', bytes(5))
        )

        if not all(conditions):
            raise InvalidRom('invalid header')

        self.number_rom_banks = header[4]
        self.number_vrom_banks = header[5]

    def _load_rom_banks(self, rom_file):
        rom_data_len = self.number_rom_banks * ROM_BANK_SIZE
        rom_data = array('B')

        try:
            rom_data.fromfile(rom_file, rom_data_len)
        except EOFError:
            raise InvalidRom('missing ROM data')

        self.rom_data = rom_data

    def _load_rom_file(self, rom_file_path):
        with open(rom_file_path, 'rb') as rom_file:
            header = array('B')
            header.fromfile(rom_file, 16)
            self._decode_header(header)
            self._load_rom_banks(rom_file)
            self._load_vrom_banks(rom_file)

    def _load_vrom_banks(self, rom_file):
        vrom_data_len = self.number_vrom_banks * VROM_BANK_SIZE
        vrom_data = array('B')

        try:
            vrom_data.fromfile(rom_file, vrom_data_len)
        except EOFError:
            raise InvalidRom('missing VROM data')

        self.vrom_data = vrom_data
