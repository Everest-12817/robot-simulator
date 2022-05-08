from Robot_Programing.instruction import InstructionTypes, Instruction
from Robotics.robot import RobotMotors


class RunMotor(Instruction):
    def __init__(self, motor, power):
        super(RunMotor, self).__init__(InstructionTypes.run_motor)
        self.motor = motor
        self.power = power

    def get_instruction_type(self):
        return InstructionTypes.run_motor

    def __str__(self):
        return f"run {self.motor} {self.power}"

    def call(self):
        if self.motor == RobotMotors.right_motor:
            self.robot.Vr = self.power
        elif self.motor == RobotMotors.left_motor:
            self.robot.Vl = self.power
