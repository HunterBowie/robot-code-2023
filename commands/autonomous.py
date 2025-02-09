import wpilib, commands2
import subsystems, constants
from commands.drive_time import DriveTime
from commands.stabilize import Stabilize

class AutonomousCube(commands2.SequentialCommandGroup):
    def __init__(self, drive_train: subsystems.DriveTrain):
        super().__init__(
            # Move forward for 1 second
            DriveTime(1, constants.SLOW_FIXED_SPEED, 0.0, drive_train),
            # Move backward for 4 seconds
            DriveTime(4, -constants.SLOW_FIXED_SPEED, 0.0, drive_train),
            # Move forward for 2 seconds
            DriveTime(2, constants.SLOW_FIXED_SPEED, 0.0, drive_train),
        )

class AutonomousStabilize(commands2.SequentialCommandGroup):
    def __init__(self, drive_train: subsystems.DriveTrain, gyroscope: wpilib.ADIS16448_IMU):
        super().__init__(
            # Move forward for 1 second
            DriveTime(1, constants.SLOW_FIXED_SPEED, 0.0, drive_train),
            # Move backward for 4 seconds
            DriveTime(4, -constants.SLOW_FIXED_SPEED, 0.0, drive_train),
            # Move forward for 2 seconds
            DriveTime(2, constants.SLOW_FIXED_SPEED, 0.0, drive_train),
            # Stabilize
            Stabilize(drive_train, gyroscope)
        )
        