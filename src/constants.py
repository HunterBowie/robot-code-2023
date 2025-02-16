from enum import Enum, auto

class RotationDirection(Enum):
    """Directions that the arm can rotate"""

    UP = auto()
    DOWN = auto()

class AutonomousMode(Enum):
    """What mode the autonomous function is in"""

    STABILIZE = auto()
    CUBE = auto()

ROTATE_SPEED = .3
EXTEND_SPEED = .4


STABILIZE_ACCURACY_RANGE_Y = 2
STABILIZE_ACCURACY_RANGE_Z = 3
AUTONOMOUS_MODE = AutonomousMode.STABILIZE
USE_PNEUMATICS = True


# pneumatics
USE_PNEUMATICS = True
PNEUMATICS_MODULE_ID = 7
RIGHT_SOLENOID_ID = 11
LEFT_SOLENOID_ID = 14

# driving
SLOW_FIXED_SPEED = 0.4

# autonomous
AUTONOMOUS_MODE = 0