from .utils import address_from_little_endian, addresses_on_same_page


class InstructionExecutor():
    def __init__(self, cpu):
        self.cpu = cpu

    def execute_and_immediate(self, operand):
        self.cpu.reg_a &= operand

        if self.cpu.reg_a == 0:
            self.cpu.status_z = True

        if self.cpu.reg_a & 0x80:
            self.cpu.status_n = True

        return 2

    def execute_and_zero_page(self, operand_address):
        operand = self.cpu.memory_read(operand_address)
        return self.execute_and_immediate(operand) + 1

    def execute_and_zero_page_x(self, operand_address):
        operand_address = (operand_address + self.cpu.reg_x) & 0xff
        operand = self.cpu.memory_read(operand_address)
        return self.execute_and_immediate(operand) + 2

    def execute_bcc(self, offset):
        return self._execute_branch(offset, not self.cpu.status_c)

    def execute_bcs(self, offset):
        return self._execute_branch(offset, self.cpu.status_c)

    def execute_beq(self, offset):
        return self._execute_branch(offset, self.cpu.status_z)

    def execute_jmp_absolute(self, address):
        self.cpu.reg_pc = address
        return 3

    def execute_jmp_indirect(self, address):
        lsb = self.cpu.memory_read(address)
        msb = self.cpu.memory_read(address + 1)
        address = address_from_little_endian(lsb, msb)
        return self.execute_jmp_absolute(address) + 2

    def execute_nop(self):
        return 2

    def _execute_branch(self, offset, take_branch):
        cycles = 2
        self.cpu.reg_pc += 2

        if take_branch:
            cycles += 1
            old_pc = self.cpu.reg_pc
            if offset > 127:
                offset = -(256 - offset)
            self.cpu.reg_pc += offset
            if not addresses_on_same_page(old_pc, self.cpu.reg_pc):
                cycles += 1

        return cycles
