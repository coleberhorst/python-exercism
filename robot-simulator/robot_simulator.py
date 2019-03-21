from math import sin, cos, pi

# Globals for the bearings
# Change the values as you see fit
EAST = .5
NORTH = 0
WEST = 1.5
SOUTH = 1


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing += .5
        if self.bearing == 2:
            self.bearing = 0

    def turn_left(self):
        self.bearing -= .5
        if self.bearing == -.5:
            self.bearing = 1.5

    def advance(self):
        self.coordinates = (self.coordinates[0] + round(sin(self.bearing * pi)), self.coordinates[1] + round(cos(self.bearing * pi)))

    def simulate(self, instructions):
        for step in instructions:
            if step == "R":
                self.turn_right()
            elif step == "L":
                self.turn_left()
            elif step == "A":
                self.advance()
