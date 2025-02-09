import wpilib, commands2

import subsystems, constants


class RotateArm(commands2.CommandBase):
    """
    Rotates for a specified amount of time

    :param float time: Time to drive for in seconds
    :param float speed: How fast to drive (-1.0 to 1.0)
    :param float rotation: How fast to rotate (-1.0 to 1.0)
    :param DriveTrain drive_train: DriveTrain to execute command on
    """

    def __init__(self, arm: subsystems.Arm, direction: constants.RotationDirection, 
                 time: float):
        super().__init__()
        self.arm = arm
        self.direction = direction
        self.time = time
        self.timer = wpilib.Timer()
        self.addRequirements(arm)

    def initialize(self) -> None:
        if self.direction == constants.RotationDirection.UP:
            self.arm.rotate_up()
        else:
            self.arm.rotate_down()
        self.timer.reset()
        self.timer.start()
    
    def end(self, interrupted: bool) -> None:
        self.arm.stop_rotating()

    def isFinished(self) -> bool:
        return self.timer.get() >= self.time