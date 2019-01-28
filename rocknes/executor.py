from .utils import address_from_little_endian, addresses_on_same_page


class InstructionExecutor():
    def __init__(self, cpu):
        self.cpu = cpu

    def execute_adc_immediate(self, operand):
        self._execute_adc(operand)
        self.cpu.reg_pc += 2
        return 2


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

    def execute_bmi(self, offset):
        return self._execute_branch(offset, self.cpu.status_n)

    def execute_bne(self, offset):
        return self._execute_branch(offset, not self.cpu.status_z)

    def execute_bpl(self, offset):
        return self._execute_branch(offset, not self.cpu.status_n)

    def execute_bvc(self, offset):
        return self._execute_branch(offset, not self.cpu.status_v)

    def execute_bvs(self, offset):
        return self._execute_branch(offset, self.cpu.status_v)

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

    def _execute_adc(self, operand):
        result = self.cpu.reg_a + operand

        self.cpu.status_c = True if result & 0x100 else False
        self.cpu.status_n = True if result & 0x80 else False
        self.cpu.status_z = result & 0xff == 0
        # overflow is set when the sign of both inputs is different from the sign of the result
        # http://www.righto.com/2012/12/the-6502-overflow-flag-explained.html
        self.cpu.status_v = bool((self.cpu.reg_a ^ result & 0xff) & (operand ^ result & 0xff) & 0x80)

        self.cpu.reg_a = result & 0xff

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
