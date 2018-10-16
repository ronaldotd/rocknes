import pytest

from rocknes.cpu import Cpu


@pytest.fixture
def cpu():
    return Cpu()
