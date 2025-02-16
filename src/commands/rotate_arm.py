import wpilib, commands2

import subsystems, src.constants as constants


class RotateArm(commands2.CommandBase):
    """Repersents the command to rotate the arm in a direction for a specified time."""

    def __init__(self, arm: subsystems.Arm, direction: constants.RotationDirection, 
                 time_seconds: float):
        super().__init__()
        self.arm = arm
        self.direction = direction
        self.time_seconds = time_seconds
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
        return self.timer.get() >= self.time_seconds