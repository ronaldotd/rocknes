from .utils import address_from_little_endian


class InstructionExecutor():
    def __init__(self, cpu):
        self.cpu = cpu

    def execute_and_immediate(self, operand):
        self.cpu.reg_a &= operand

        if self.cpu.reg_a == 0:
            self.cpu.flag_z = 1

        if self.cpu.reg_a & 0x80:
            self.cpu.flag_n = 1

        return 2

    def execute_jmp_absolute(self, address):
        self.cpu.reg_pc = address
        return 3

    def execute_jmp_indirect(self, address):
        lsb = self.cpu.memory_read(address)
        msb = self.cpu.memory_read(address + 1)
        address = address_from_little_endian(lsb, msb)
        return self.execute_jmp_absolute(address) + 2

    def execute_nop(self):
        self.cpu.reg_pc += 1
        return 2
