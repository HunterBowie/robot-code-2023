import wpilib, commands2

import subsystems


class DriveTime(commands2.CommandBase):
    """
    Drives for a specified amount of time

    :param float time: Time to drive for in seconds
    :param float speed: How fast to drive (-1.0 to 1.0)
    :param float rotation: How fast to rotate (-1.0 to 1.0)
    :param DriveTrain drive_train: DriveTrain to execute command on
    """

    def __init__(self, time: float, speed: float, rotation: float, 
                 drive_train: subsystems.DriveTrain):
        super().__init__()
        self.drive_train = drive_train
        self.time = time
        self.speed = speed
        self.rotation = rotation
        self.timer = wpilib.Timer()
        self.addRequirements(drive_train)

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()
    
    def execute(self) -> None:
        self.drive_train.move(self.speed, self.rotation)
    
    def end(self, interrupted: bool) -> None:
        self.drive_train.move(0.0, 0.0)

    def isFinished(self) -> bool:
        return self.timer.get() >= self.time