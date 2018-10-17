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

    def execute_jmp(self, address):
        exe_cycles = 3
        if self.cpu.memory_read(self.cpu.reg_pc) == 0x6c:
            lsb = self.cpu.memory_read(address)
            msb = self.cpu.memory_read(address + 1)
            address = address_from_little_endian(lsb, msb)
            exe_cycles += 2

        self.cpu.reg_pc = address
        return exe_cycles

    def execute_nop(self):
        self.cpu.reg_pc += 1
        return 2
