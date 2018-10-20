from unittest import mock


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x29, 0x0c])
def test_execute_and_immediate(mock_memory_read, cpu):
    cpu.reg_a = 0x08
    length, cycles = cpu.decode_execute()

    assert cpu.reg_a == 0x08
    assert cpu.status_z is False
    assert cpu.status_n is False
    assert length == 2
    assert cycles == 2
    assert mock_memory_read.call_count == 2


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x29, 0xff])
def test_execute_and_immediate_zero(mock_memory_read, cpu):
    length, cycles = cpu.decode_execute()

    assert cpu.reg_a == 0x00
    assert cpu.status_z is True
    assert cpu.status_n is False


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x29, 0xff])
def test_execute_and_immediate_negative(mock_memory_read, cpu):
    cpu.reg_a = 0xf0
    length, cycles = cpu.decode_execute()

    assert cpu.reg_a == 0xf0
    assert cpu.status_z is False
    assert cpu.status_n is True


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x4c, 0xad, 0xde])
def test_execute_jmp_absolute(mock_memory_read, cpu):
    length, cycles = cpu.decode_execute()

    assert cpu.reg_pc == 0xdead
    assert length == 3
    assert cycles == 3
    assert mock_memory_read.call_count == 3


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0x6c, 0xad, 0xde, 0x11, 0x22])
def test_execute_jmp_relative(mock_memory_read, cpu):
    length, cycles = cpu.decode_execute()

    assert cpu.reg_pc == 0x2211
    assert length == 3
    assert cycles == 5
    assert mock_memory_read.call_count == 5


@mock.patch('rocknes.cpu.Cpu.memory_read', return_value=0xea)
def test_execute_nop(mock_memory_read, cpu):
    length, cycles = cpu.decode_execute()

    assert length == 1
    assert cycles == 2
    assert mock_memory_read.call_count == 1
