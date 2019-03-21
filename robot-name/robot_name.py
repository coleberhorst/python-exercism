import random
from random import randint
import string

class Robot(object):
    robot_names = []

    def __init__(self):
        self.reset()
    def reset(self):
        self.name = ""
        while self.name in Robot.robot_names:
            self.name = "".join(random.choices(string.ascii_uppercase, k=2)) + str(randint(100,999))
        Robot.robot_names.append(self.name)
