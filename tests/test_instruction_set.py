import pytest

from rocknes.exceptions import MemorySpaceExceeded


def test_jmp(cpu):
    address = 0x1000
    cpu.execute_instruction_jmp(address)
    assert cpu.reg_pc == address


def test_jmp_out_of_bounds(cpu):
    with pytest.raises(MemorySpaceExceeded):
        cpu.execute_instruction_jmp(0xfffff)
