from .utils import address_from_little_endian


class InstructionDecoder():
    def __init__(self, cpu):
        self.cpu = cpu

    def decode_and_immediate(self):
        operand = self.cpu.memory_read(self.cpu.reg_pc + 1)
        return (2, operand)

    def decode_and_zero_page(self):
        operand_address = self.cpu.memory_read(self.cpu.reg_pc + 1)
        return (2, operand_address)

    def decode_and_absolute(self):
        lsb = self.cpu.memory_read(self.cpu.reg_pc + 1)
        msb = self.cpu.memory_read(self.cpu.reg_pc + 2)
        operand_address = address_from_little_endian(lsb, msb)
        return (3, operand_address)

    def decode_jmp(self):
        lsb = self.cpu.memory_read(self.cpu.reg_pc + 1)
        msb = self.cpu.memory_read(self.cpu.reg_pc + 2)
        address = address_from_little_endian(lsb, msb)
        return (3, address)

    def decode_nop(self):
        return (1,)
