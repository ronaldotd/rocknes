from .exceptions import MemorySpaceExceeded
from .utils import address_from_little_endian


class Cpu():
    def __init__(self, rom=None):
        self.rom = rom
        self.reg_pc = 0
        self.reg_sp = 0
        self.reg_a = 0
        self.reg_x = 0
        self.reg_y = 0

        self.opcode_functions = {
            0x4c: (self.decode_jmp_absolute, self.execute_instruction_jmp),
            0x6c: (self.decode_jmp_indirect, self.execute_instruction_jmp),
        }

    def decode_execute(self):
        opcode = self.memory_read(self.reg_pc)
        decode_execute_fns = self.opcode_functions[opcode]
        decode_fn, execute_fn = decode_execute_fns

        instruction_length, exe_cycles, *params = decode_fn()
        execute_fn(*params)

        return instruction_length, exe_cycles

    def memory_read(self, address):
        pass

    def memory_write(self, address):
        pass

    def decode_jmp_absolute(self):
        lsb = self.memory_read(self.reg_pc + 1)
        msb = self.memory_read(self.reg_pc + 2)
        address = address_from_little_endian(lsb, msb)
        return (3, 3, address)

    def decode_jmp_indirect(self):
        lsb = self.memory_read(self.reg_pc + 1)
        msb = self.memory_read(self.reg_pc + 2)
        address = address_from_little_endian(lsb, msb)

        lsb = self.memory_read(address)
        msb = self.memory_read(address + 1)
        address = address_from_little_endian(lsb, msb)

        return (3, 5, address)

    def execute_instruction_jmp(self, address):
        if address > 0xffff:
            raise MemorySpaceExceeded()
        self.reg_pc = address
