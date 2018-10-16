from unittest import mock


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0xad, 0xde])
def test_decode_jmp(mock_memory_read, cpu):
    length, address = cpu.decoder.decode_jmp()

    assert mock_memory_read.call_count == 2
    assert length == 3
    assert address == 0xdead
