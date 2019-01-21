from unittest.mock import Mock

import pytest


@pytest.fixture
def cpu():
    cpu = Mock()
    cpu.reg_pc = 0
    return cpu
