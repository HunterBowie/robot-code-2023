# Robot Code (First Robotics Competition)

## About the Robot

This code is for a robot that competed in the 2023 [First Robotics Competion (FRC)](https://www.firstinspires.org/robotics/frc) Candian Pacific Regionals. It had a mechanism that could grab a plastic cube or cone using a pneumatic system and a gyroscope that auto balanced the robot on tilting platform.


![Robot](./robot.jpg)



## About the Code

The project is organized according to the [command based programming](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html) design pattern/framework. This means that each part of the robot is a class in the subsystems folder and each keybind or autonomous behaviour is a class in the commands folder. The robot_container file has most of the configuration code that sets up things like keybindings and the rest of the functionality is mostly distributed among the subsytems and commands.


This is the code for balancing the robot on the tilting platform. 

```python
def execute(self) -> None:
    gyro_y = round(self.gyroscope.getGyroAngleY())
    gyro_z = round(self.gyroscope.getGyroAngleZ())

    forward_speed = self._calc_speed(gyro_y, 
    constants.STABILIZE_ACCURACY_RANGE_Y)

    rotation_speed = self._calc_speed(gyro_z, 
    constants.STABILIZE_ACCURACY_RANGE_Z)

    self.drive_train.move(forward_speed, rotation_speed)
    
def _calc_speed(self, angle: int, accuracy_range: int) -> float:
    if angle > accuracy_range:
        return -.5   
    if angle < -accuracy_range:
        return .5
    return 0.0
```

Once we got the gyroscope properly calibrated, it was pretty straightforward to write code that stabilzed it on the platform. The key was to recognize that there was a range of angles that could 
be considered flat/stabalized. If our gyroscope was giving us values outside of that range, we drive a set speed in the opposite direction.

This project was made in python using [RobotPy](https://robotpy.readthedocs.io/en/stable/) but a [previous robot](https://github.com/TempletonRobotics7190/RapidReact2022) I worked on in used Java instead. 


## Robot in Action

<video src="robotics.mov" width="320" height="240" controls></video>


## Other Contributors  
- [Kian Khadempour](https://github.com/KianKhadempour)