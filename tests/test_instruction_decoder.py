from unittest.mock import Mock

import pytest

from rocknes.decoder import InstructionDecoder


@pytest.fixture
def cpu():
    cpu = Mock()
    cpu.reg_pc = 0
    return cpu


def test_decode_implicit(cpu):
    decoder = InstructionDecoder(cpu)

    assert decoder.decode_implicit() == (1,)


def test_decode_byte(cpu):
    cpu.memory_read = Mock(return_value=0x10)
    decoder = InstructionDecoder(cpu)

    length, operand = decoder.decode_byte()

    assert length == 2
    assert operand == 0x10


def test_decode_word(cpu):
    cpu.memory_read = Mock(side_effect=[0xaa, 0xbb])
    decoder = InstructionDecoder(cpu)

    length, operand = decoder.decode_word()

    assert length == 3
    assert operand == 0xbbaa
