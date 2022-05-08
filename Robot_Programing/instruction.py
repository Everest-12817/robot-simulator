import enum


class InstructionTypes(enum.Enum):
    run_motor = 0
    variable = 1


class Instruction:
    def __init__(self, instruction_type):
        self.instruction_type = instruction_type
        self._robot = None

    @property
    def robot(self):
        return self._robot

    @robot.setter
    def robot(self, robot):
        self._robot = robot

    def get_instruction_type(self):
        raise NotImplementedError("[Instruction] Cannot get type of pure instruction ")

    def __str__(self):
        raise NotImplementedError("[Instruction] Cannot get string on pure instruction ")

    def call(self):
        raise NotImplementedError("[Instruction] Cannot call pure instruction ")
