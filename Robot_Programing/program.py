from Robot_Programing.instruction import InstructionTypes, Instruction


class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.program_stack = []
        self.symbol_table = {}
        self.pc = 0
