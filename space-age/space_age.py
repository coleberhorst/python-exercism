class SpaceAge(object):
    EARTH_YEAR_TO_SECONDS = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 0.2408467, 2)
    def on_venus(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 0.61519726, 2)
    def on_earth(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 1, 2)
    def on_mars(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 1.8808158, 2)
    def on_jupiter(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 11.862615, 2)
    def on_saturn(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 29.447498, 2)
    def on_uranus(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 84.016846, 2)
    def on_neptune(self):
        return round(self.seconds / self.EARTH_YEAR_TO_SECONDS / 164.79132, 2)
