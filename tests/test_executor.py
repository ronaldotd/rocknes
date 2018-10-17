from unittest import mock


def test_execute_and_immediate(cpu):
    cpu.reg_a = 0x00
    exe_cycles = cpu.executor.execute_and_immediate(0x55)

    assert exe_cycles == 2
    assert cpu.reg_a == 0x00
    assert cpu.flag_n == 0
    assert cpu.flag_z == 1


def test_execute_jmp_absolute(cpu):
    exe_cycles = cpu.executor.execute_jmp_absolute(0x1000)

    assert cpu.reg_pc == 0x1000
    assert exe_cycles == 3


@mock.patch('rocknes.cpu.Cpu.memory_read', side_effect=[0xad, 0xde])
def test_execute_jmp_indirect(mock_memory_read, cpu):
    exe_cycles = cpu.executor.execute_jmp_indirect(0x1000)

    assert mock_memory_read.call_count == 2
    assert cpu.reg_pc == 0xdead
    assert exe_cycles == 5


def test_execute_nop(cpu):
    cpu.reg_pc = 0x1000
    exe_cycles = cpu.executor.execute_nop()

    assert cpu.reg_pc == 0x1001
    assert exe_cycles == 2
