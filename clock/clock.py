class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = (minute + hour * 60) % 1440

    def __repr__(self):
        return "%02d:%02d" % (self.minutes // 60, self.minutes % 60)

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        self.minutes = (self.minutes + minutes) % 1440
        return self

    def __sub__(self, minutes):
        self.minutes = (self.minutes - minutes) % 1440
        return self
