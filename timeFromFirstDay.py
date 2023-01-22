from datetime import datetime
def timeFromFirstDay():
    current_year = datetime.now().year
    start_of_year = datetime(current_year, 1, 1)
    now = datetime.now()
    time_passed = now - start_of_year
    seconds_passed = int(time_passed.total_seconds())
    return bin(seconds_passed)[2:]
    
    # now = datetime.now()
    # first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    # seconds_passed = (now - first_day_of_month).total_seconds()
    # minutes_passed = seconds_passed / 60
    # binOfMinutesPassed = bin(int(minutes_passed))[2:]
    # return binOfMinutesPassed


# import datetime

# def seconds_passed():
#     current_year = datetime.now().year
#     start_of_year = datetime(current_year, 1, 1)
#     now = datetime.now()
#     time_passed = now - start_of_year
#     seconds_passed = int(time_passed.total_seconds())
#     return bin(seconds_passed)[2:]

