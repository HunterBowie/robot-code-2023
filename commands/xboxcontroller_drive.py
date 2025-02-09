import wpilib, commands2, subsystems, constants

class XboxcontrollerDrive(commands2.CommandBase):
    def __init__(self, xboxcontroller: wpilib.XboxController, drive_train: subsystems.DriveTrain):
        super().__init__()
        self.xboxcontroller = xboxcontroller
        self.drive_train = drive_train
        self.addRequirements(drive_train)
    
    def execute(self) -> None:
        forward_speed = self.xboxcontroller.getLeftY()
        # if abs(self.xboxcontroller.getLeftY()) < 0.3:
        #     if self.xboxcontroller.getLeftY() > 0:
        #         forward_speed = constants.SLOW_FIXED_SPEED
        #     if self.xboxcontroller.getLeftY() > 0:
        #         forward_speed = -constants.SLOW_FIXED_SPEED
        rotation_speed = self.xboxcontroller.getRightX()
        # if abs(self.xboxcontroller.getRightX()) < 0.3:
        #     if self.xboxcontroller.getRightX() > 0:
        #         rotation_speed = constants.SLOW_FIXED_SPEED
        #     if self.xboxcontroller.getRightX() > 0:
        #         rotation_speed = -constants.SLOW_FIXED_SPEED
        self.drive_train.move(forward_speed, -rotation_speed)
    
