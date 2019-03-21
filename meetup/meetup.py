import datetime
import calendar


day_of_week_iso = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
which_table = { "first": 1,
                "second": 2,
                "third": 3,
                "fourth": 4,
                "fifth": 5,
            }


def meetup_day(year, month, day_of_the_week, which):
    dow_number = day_of_week_iso[day_of_the_week]
    if which in which_table:
        start = 1
    elif "teenth" == which:
        start = 13
    else:
        start = calendar.monthrange(year, month)[1]
    result = datetime.date(year, month, start)
    result = datetime.date(year, month, result.weekday() - dow_number + start)

    return result


class MeetupDayException(Exception):
    pass
