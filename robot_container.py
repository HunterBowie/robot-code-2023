import wpilib, constants, commands2, commands2.button
import commands, subsystems

class RobotContainer:
    def __init__(self):
        self.xboxcontroller = wpilib.XboxController(0)
        self.joystick = wpilib.Joystick(1)
        self.gyroscope = wpilib.ADIS16448_IMU()

        # The robot's subsystems
        self.drive_train = subsystems.DriveTrain()
        self.arm = subsystems.Arm()
        if constants.USE_PNEUMATICS:
            self.grabber = subsystems.Grabber()
            self.grabber.close_full()

        # Autonomous routine
        self.autonomous_stabilize = commands.AutonomousStabilize(self.drive_train, self.gyroscope)
        self.autonomous_cube = commands.AutonomousCube(self.drive_train)


        # set up default drive command
        self.drive_train.setDefaultCommand(
            commands.XboxcontrollerDrive(self.xboxcontroller, self.drive_train)
        )
        self.configureButtonBindings()

    def configureButtonBindings(self) -> None:
        command_controller = commands2.button.CommandXboxController(0)
        command_joystick = commands2.button.CommandJoystick(1)

        trigger = commands2.button.JoystickButton(command_joystick, 1)
        side = commands2.button.JoystickButton(command_joystick, 2)
        left_bottom = commands2.button.JoystickButton(command_joystick, 3)
        right_bottom = commands2.button.JoystickButton(command_joystick, 4)
        left_top = commands2.button.JoystickButton(command_joystick, 5)
        right_top = commands2.button.JoystickButton(command_joystick, 6)

        if constants.USE_PNEUMATICS:
            trigger.whenPressed(commands2.InstantCommand(self.grabber.toggle_full))
            side.whenPressed(commands2.InstantCommand(self.grabber.toggle_half))
        
        left_top.whileHeld(commands2.StartEndCommand(self.arm.rotate_down, self.arm.stop_rotating))
        left_bottom.whileHeld(commands2.StartEndCommand(self.arm.rotate_up, self.arm.stop_rotating))
        right_top.whileHeld(commands2.StartEndCommand(self.arm.extend_forward, self.arm.stop_extending))
        right_bottom.whileHeld(commands2.StartEndCommand(self.arm.extend_backward, self.arm.stop_extending))
    
    def getAutonomousCommand(self) -> commands2.SequentialCommandGroup:
        if constants.AUTONOMOUS_MODE == constants.AutonomousMode.STABILIZE:
            return self.autonomous_stabilize
        return self.autonomous_cube