from .utils import address_from_little_endian


class InstructionDecoder():
    def __init__(self, cpu):
        self.cpu = cpu

    def decode_implicit(self):
        return (1,)

    def decode_byte(self):
        operand = self.cpu.memory_read(self.cpu.reg_pc + 1)
        return (2, operand)

    def decode_word(self):
        lsb = self.cpu.memory_read(self.cpu.reg_pc + 1)
        msb = self.cpu.memory_read(self.cpu.reg_pc + 2)
        address = address_from_little_endian(lsb, msb)
        return (3, address)
