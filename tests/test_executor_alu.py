import pytest

from rocknes.executor import InstructionExecutor


def test_execute_adc_immediate_cycles(cpu):
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_adc_immediate(0xa)

    assert cycles == 2


def test_execute_adc_immediate_pc(cpu):
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(0xa)

    assert cpu.reg_pc == 0x2


@pytest.mark.parametrize('reg_a, operand, expected', [
    (0x0, 0x0, 0x0),
    (0xa, 0xa, 0x14),
    (0x1, 0xff, 0x0),
])
def test_execute_adc_immediate(reg_a, operand, expected, cpu):
    cpu.reg_a = reg_a
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(operand)

    assert cpu.reg_a == expected


@pytest.mark.parametrize('operand, expected', [
    (0x1, False),
    (0xc0, True),
])
def test_execute_adc_immediate_carry(operand, expected, cpu):
    cpu.reg_a = 0xc0
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(operand)

    assert cpu.status_c is expected


@pytest.mark.parametrize('reg_a, operand, expected', [
    (0x0, 0x0, True),
    (0x0, 0x1, False),
    (0xff, 0x1, True),
    (0x7f, 0x81, True),
])
def test_execute_adc_immediate_zero(reg_a, operand, expected, cpu):
    cpu.reg_a = reg_a
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(operand)

    assert cpu.status_z is expected


@pytest.mark.parametrize('operand, expected', [
    (0x0, False),
    (0x1, False),
    (0xff, True),
])
def test_execute_adc_immediate_negative(operand, expected, cpu):
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(operand)

    assert cpu.status_n is expected


@pytest.mark.parametrize('reg_a, operand, expected', [
    (0x50, 0x10, False),
    (0x50, 0x50, True),
    (0x50, 0x90, False),
    (0x50, 0xd0, False),
    (0xd0, 0x10, False),
    (0xd0, 0x50, False),
    (0xd0, 0x90, True),
    (0xd0, 0xd0, False),
])
def test_execute_adc_immediate_overflow(reg_a, operand, expected, cpu):
    cpu.reg_a = reg_a
    executor = InstructionExecutor(cpu)

    executor.execute_adc_immediate(operand)

    assert cpu.status_v is expected
