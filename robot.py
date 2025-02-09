import wpilib, commands2, commands2.button, wpilib.event

import commands, constants

from robot_container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        wpilib.CameraServer.launch()
        self.container = RobotContainer()
        self.autonomous_command = self.container.getAutonomousCommand()

    def robotPeriodic(self):
        super().robotPeriodic()
        wpilib.SmartDashboard.putNumber("Gyro", round(self.container.gyroscope.getGyroAngleY(), 1))
        wpilib.SmartDashboard.putData("Calibrate Gyro", commands.CalibrateGyro(
            self.container.gyroscope, self.container.drive_train))
        wpilib.SmartDashboard.putBoolean("Pneumatics", not self.container.grabber.is_closed)
        wpilib.SmartDashboard.putBoolean("Enabled", self.isEnabled())

    def autonomousInit(self):
        self.autonomous_command.schedule()

    def teleopInit(self):
        self.autonomous_command.cancel()


wpilib.run(Robot)