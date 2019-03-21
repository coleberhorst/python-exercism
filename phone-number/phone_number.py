import re

class Phone(object):
    def __init__(self, phone_number):
        temp = re.sub('[^0-9]', '', phone_number)
        if len(temp) == 11 and not temp[0] == "1":
            raise ValueError("{} is not a North American phone number.".format(temp))
        self.number = temp[-10:]
        self.area_code = self.number[0:3]
        if len(self.number) < 10:
            raise ValueError("{} is not a 10 or 11 digit phone number.".format(self.number))
        elif self.area_code[0] in ("0", "1"):
            raise ValueError("{} Area Codes cannot start with 0 or 1.".format(self.area_code))
        elif self.number[3] in ("0", "1"):
            raise ValueError("{} Exchange Code cannot start with 0 or 1.".format(self.number))

    def pretty(self):
        return "({}) {}-{}".format(self.number[:3], self.number[3:6], self.number[6:])
