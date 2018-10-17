from .decoder import InstructionDecoder
from .executor import InstructionExecutor


class Cpu():
    def __init__(self, rom=None):
        self.rom = rom
        self.reg_pc = 0
        self.reg_sp = 0
        self.reg_a = 0
        self.reg_x = 0
        self.reg_y = 0
        self.flag_z = 0
        self.flag_n = 0
        self.decoder = InstructionDecoder(self)
        self.executor = InstructionExecutor(self)

        self.opcode_functions = {
            0x4c: (self.decoder.decode_jmp, self.executor.execute_jmp_absolute),
            0x6c: (self.decoder.decode_jmp, self.executor.execute_jmp_indirect),
            0xea: (self.decoder.decode_nop, self.executor.execute_nop),
        }

    def decode_execute(self):
        opcode = self.memory_read(self.reg_pc)
        decode_fn, execute_fn = self.opcode_functions[opcode]

        instruction_length, *params = decode_fn()
        exe_cycles = execute_fn(*params)

        return instruction_length, exe_cycles

    def memory_read(self, address):
        pass

    def memory_write(self, address):
        pass
