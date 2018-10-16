from unittest import mock


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x4c])
def test_execute_jmp_absolute(mock_memory_read, cpu):
    exe_cycles = cpu.executor.execute_jmp(0x1000)

    assert mock_memory_read.call_count == 1
    assert cpu.reg_pc == 0x1000
    assert exe_cycles == 3


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x6c, 0xad, 0xde])
def test_execute_jmp_indirect(mock_memory_read, cpu):
    exe_cycles = cpu.executor.execute_jmp(0x1000)

    assert mock_memory_read.call_count == 3
    assert cpu.reg_pc == 0xdead
    assert exe_cycles == 5
