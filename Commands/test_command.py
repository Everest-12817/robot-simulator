from Commands.Command import Command


class test_command(Command):
    def __init__(self, robot):
        super(test_command, self).__init__()
        self.robot = robot
        self.condition = self.check_dist()

    def check_dist(self):
        return self.robot.x < 200

    def execute(self):
        self.robot.x += 5
