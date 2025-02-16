import wpilib, commands2

import subsystems


class CalibrateGyro(commands2.CommandBase):    
    def __init__(self, gyroscope: wpilib.ADIS16448_IMU, drive_train: subsystems.DriveTrain):
        super().__init__()
        self.gyroscope = gyroscope
        self.addRequirements(drive_train)
        self.timer = wpilib.Timer()

    def initialize(self):
        self.gyroscope.configCalTime(self.gyroscope.CalibrationTime._128ms)
        self.gyroscope.calibrate()
        self.timer.reset()
        self.timer.start()
        print("calibratize")
    
    def isFinished(self) -> bool:
        return self.timer.get() > .128
