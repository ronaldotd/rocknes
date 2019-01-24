from rocknes.executor import InstructionExecutor


def test_execute_bcc_branch_not_taken(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0xa0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0xa)

    assert cycles == 2
    assert cpu.reg_pc == 0xa2


def test_execute_bcc_branch_taken_positive_offset(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xa0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0xa)

    assert cycles == 3
    assert cpu.reg_pc == 0xac


def test_execute_bcc_branch_taken_negative_offset(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xa0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0xfb)

    assert cycles == 3
    assert cpu.reg_pc == 0x9d


def test_execute_bcc_branch_taken_zero_offset(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xa0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0)

    assert cycles == 3
    assert cpu.reg_pc == 0xa2


def test_execute_bcc_branch_taken_positive_offset_page_boundary(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xdd
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0x7f)

    assert cycles == 4
    assert cpu.reg_pc == 0x15e


def test_execute_bcc_branch_taken_negative_offset_page_boundary(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xac55
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcc(0x80)

    assert cycles == 4
    assert cpu.reg_pc == 0xabd7


def test_execute_bcs_branch_not_taken(cpu):
    cpu.status_c = False
    cpu.reg_pc = 0xc0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0xa)

    assert cycles == 2
    assert cpu.reg_pc == 0xc2


def test_execute_bcs_branch_taken_positive_offset(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0x20
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0xa)

    assert cycles == 3
    assert cpu.reg_pc == 0x2c


def test_execute_bcs_branch_taken_negative_offset(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0x70
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0xfb)

    assert cycles == 3
    assert cpu.reg_pc == 0x6d


def test_execute_bcs_branch_taken_zero_offset(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0x10
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0)

    assert cycles == 3
    assert cpu.reg_pc == 0x12


def test_execute_bcs_branch_taken_positive_offset_page_boundary(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0xdd
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0x7f)

    assert cycles == 4
    assert cpu.reg_pc == 0x15e


def test_execute_bcs_branch_taken_negative_offset_page_boundary(cpu):
    cpu.status_c = True
    cpu.reg_pc = 0xac55
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bcs(0x80)

    assert cycles == 4
    assert cpu.reg_pc == 0xabd7


def test_execute_beq_branch_not_taken(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0xc0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0xa)

    assert cycles == 2
    assert cpu.reg_pc == 0xc2


def test_execute_beq_branch_taken_positive_offset(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0x20
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0xa)

    assert cycles == 3
    assert cpu.reg_pc == 0x2c


def test_execute_beq_branch_taken_negative_offset(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0x70
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0xfb)

    assert cycles == 3
    assert cpu.reg_pc == 0x6d


def test_execute_beq_branch_taken_zero_offset(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0x10
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0)

    assert cycles == 3
    assert cpu.reg_pc == 0x12


def test_execute_bmi_branch_not_taken(cpu):
    cpu.status_n = False
    cpu.reg_pc = 0xc0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0xa)

    assert cycles == 2
    assert cpu.reg_pc == 0xc2


def test_execute_bmi_branch_taken_positive_offset(cpu):
    cpu.status_n = True
    cpu.reg_pc = 0x20
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0xa)

    assert cycles == 3
    assert cpu.reg_pc == 0x2c


def test_execute_bmi_branch_taken_negative_offset(cpu):
    cpu.status_n = True
    cpu.reg_pc = 0x70
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0xfb)

    assert cycles == 3
    assert cpu.reg_pc == 0x6d


def test_execute_bmi_branch_taken_zero_offset(cpu):
    cpu.status_n = True
    cpu.reg_pc = 0x10
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0)

    assert cycles == 3
    assert cpu.reg_pc == 0x12


def test_execute_bmi_branch_taken_positive_offset_page_boundary(cpu):
    cpu.status_n = True
    cpu.reg_pc = 0xdd
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0x7f)

    assert cycles == 4
    assert cpu.reg_pc == 0x15e


def test_execute_bmi_branch_taken_negative_offset_page_boundary(cpu):
    cpu.status_n = True
    cpu.reg_pc = 0xac55
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bmi(0x80)

    assert cycles == 4
    assert cpu.reg_pc == 0xabd7


def test_execute_beq_branch_taken_positive_offset_page_boundary(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0xdd
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0x7f)

    assert cycles == 4
    assert cpu.reg_pc == 0x15e


def test_execute_beq_branch_taken_negative_offset_page_boundary(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0xac55
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_beq(0x80)

    assert cycles == 4
    assert cpu.reg_pc == 0xabd7


def test_execute_bne_branch_not_taken(cpu):
    cpu.status_z = True
    cpu.reg_pc = 0xc0
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0xa)

    assert cycles == 2
    assert cpu.reg_pc == 0xc2


def test_execute_bne_branch_taken_positive_offset(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0x20
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0xa)

    assert cycles == 3
    assert cpu.reg_pc == 0x2c


def test_execute_bne_branch_taken_negative_offset(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0x70
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0xfb)

    assert cycles == 3
    assert cpu.reg_pc == 0x6d


def test_execute_bne_branch_taken_zero_offset(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0x10
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0)

    assert cycles == 3
    assert cpu.reg_pc == 0x12


def test_execute_bne_branch_taken_positive_offset_page_boundary(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0xdd
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0x7f)

    assert cycles == 4
    assert cpu.reg_pc == 0x15e


def test_execute_bne_branch_taken_negative_offset_page_boundary(cpu):
    cpu.status_z = False
    cpu.reg_pc = 0xac55
    executor = InstructionExecutor(cpu)

    cycles = executor.execute_bne(0x80)

    assert cycles == 4
    assert cpu.reg_pc == 0xabd7
