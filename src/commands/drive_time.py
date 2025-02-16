import wpilib, commands2

import subsystems


class DriveTime(commands2.CommandBase):
    """Repersents a command to drive the robot for a specified amount of time."""

    def __init__(self, time_seconds: float, forward_speed: float, rotation_speed: float, 
                 drive_train: subsystems.DriveTrain):
        super().__init__()
        self.drive_train = drive_train
        self.time_seconds = time_seconds
        self.forward_speed = forward_speed
        self.rotation_speed = rotation_speed
        self.timer = wpilib.Timer()
        self.addRequirements(drive_train)

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()
    
    def execute(self) -> None:
        self.drive_train.move(self.forward_speed, self.rotation_speed)
    
    def end(self, interrupted: bool) -> None:
        self.drive_train.move(0.0, 0.0)

    def isFinished(self) -> bool:
        return self.timer.get() >= self.time_seconds