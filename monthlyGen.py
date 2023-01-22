from datetime import datetime, timedelta

now = datetime.now()
first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

seconds_passed = (now - first_day_of_month).total_seconds()
minutes_passed = seconds_passed / 60

print("Minutes passed from first day of the month: ", len(bin(int(minutes_passed))[2:]))

