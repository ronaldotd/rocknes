from unittest import mock


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x6c, 0xad, 0xde])
def test_decode_execute_jmp_absolute(mock_memory_read, cpu):
    mock_memory_read.side_effect = [0x4c, 0xad, 0xde]
    length, cycles = cpu.decode_execute()

    assert mock_memory_read.call_count == 3
    assert cpu.reg_pc == 0xdead
    assert length == 3
    assert cycles == 3


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x6c, 0xad, 0xde, 0xcc, 0xaa])
def test_decode_execute_jmp_indirect(mock_memory_read, cpu):
    length, cycles = cpu.decode_execute()

    assert mock_memory_read.call_count == 5
    assert cpu.reg_pc == 0xaacc
    assert length == 3
    assert cycles == 5
