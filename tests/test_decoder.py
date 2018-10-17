from unittest import mock


@mock.patch('rocknes.cpu.Cpu.memory_read', return_value=0xcc)
def test_decode_and_immediate(mock_memory_read, cpu):
    length, operand = cpu.decoder.decode_and_immediate()

    assert mock_memory_read.call_count == 1
    assert length == 2
    assert operand == 0xcc


@mock.patch('rocknes.cpu.Cpu.memory_read', return_value=0xcc)
def test_decode_and_zero_page(mock_memory_read, cpu):
    length, operand_address = cpu.decoder.decode_and_zero_page()

    assert mock_memory_read.call_count == 1
    assert length == 2
    assert operand_address == 0xcc


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0xcc, 0xdd])
def test_decode_and_absolute(mock_memory_read, cpu):
    length, operand_address = cpu.decoder.decode_and_absolute()

    assert mock_memory_read.call_count == 2
    assert length == 3
    assert operand_address == 0xddcc


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0xad, 0xde])
def test_decode_jmp(mock_memory_read, cpu):
    length, address = cpu.decoder.decode_jmp()

    assert mock_memory_read.call_count == 2
    assert length == 3
    assert address == 0xdead


def test_decode_nop(cpu):
    (length,) = cpu.decoder.decode_nop()

    assert length == 1
