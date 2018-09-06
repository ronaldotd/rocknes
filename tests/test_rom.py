from io import BytesIO
from unittest import mock

import pytest

from rocknes.exceptions import InvalidRom
from rocknes.rom import Rom, ROM_BANK_SIZE, VROM_BANK_SIZE


@pytest.fixture
def valid_header():
    header = bytearray(16)
    header[:6] = bytes((0x4e, 0x45, 0x53, 0x1a, 0x01, 0x01))
    return header


@pytest.fixture
def rom_file_valid(valid_header):
    rom = bytearray(valid_header)
    rom.extend(bytes(valid_header[4] * ROM_BANK_SIZE))
    rom.extend(bytes(valid_header[5] * VROM_BANK_SIZE))
    return BytesIO(rom)


@pytest.fixture
def rom_file_missing_rom_data(rom_file_valid):
    view = rom_file_valid.getbuffer()
    view[4] = 2
    return rom_file_valid


@pytest.fixture
def rom_file_missing_vrom_data(rom_file_valid):
    view = rom_file_valid.getbuffer()
    view[5] = 2
    return rom_file_valid


@pytest.fixture
def rom_file_invalid_header(rom_file_valid):
    view = rom_file_valid.getbuffer()
    view[0] = 0x4d
    return rom_file_valid


@mock.patch('rocknes.rom.open')
def test_load_rom_valid(mock_open, rom_file_valid):
    mock_open.return_value = rom_file_valid
    rom = Rom('path_to_rom')

    assert rom.number_rom_banks == 1
    assert rom.number_vrom_banks == 1


@mock.patch('rocknes.rom.open')
def test_load_rom_invalid_magic_number(mock_open, rom_file_invalid_header):
    mock_open.return_value = rom_file_invalid_header
    with pytest.raises(InvalidRom):
        Rom('path_to_rom')


@mock.patch('rocknes.rom.open')
def test_load_rom_missing_rom_data(mock_open, rom_file_missing_rom_data):
    mock_open.return_value = rom_file_missing_rom_data
    with pytest.raises(InvalidRom):
        Rom('path_to_rom')


@mock.patch('rocknes.rom.open')
def test_load_rom_missing_vrom_data(mock_open, rom_file_missing_vrom_data):
    mock_open.return_value = rom_file_missing_vrom_data
    with pytest.raises(InvalidRom):
        Rom('path_to_rom')


@mock.patch('rocknes.rom.open')
def test_load_rom_file_not_found(mock_open):
    mock_open.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        Rom('path_to_rom')
