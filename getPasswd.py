from datetime import datetime, timedelta
import requests


def minutes_passed(month, day, hour, minute):
      year = datetime.now().year
      first_day_of_year = datetime(year, 1, 1)
      specific_time = datetime(year, month, day, hour, minute)
      time_passed = specific_time - first_day_of_year
      _minutes_passed = int(time_passed.total_seconds()/60)
      minutes = (bin(abs(int(_minutes_passed)))[2:])
      return minutes


def seconds_passed(month, day, hour, minute, second):
    current_year = datetime.now().year
    start_of_year = datetime(current_year, 1, 1)
    specific_time = datetime(current_year, month, day, hour, minute, second)
    time_passed = specific_time - start_of_year
    seconds_passed = int(time_passed.total_seconds())
    return (bin(seconds_passed)[2:])

def getPassword(_from_date,_from_hour, _to_date,_to_hour):

      __from_binOfSecondsPassed = seconds_passed(1, int(_from_date), int(_from_hour), 0, 0)
      print(__from_binOfSecondsPassed)
      __to_binOfSecondsPassed = seconds_passed(1, int(_to_date), int(_to_hour), 0, 0)
      print(__to_binOfSecondsPassed)
      url = "http://192.168.61.8:5223/input_hash?From="+__from_binOfSecondsPassed+"&To="+__to_binOfSecondsPassed
      response = requests.get(url)
      if response.status_code == 200:
            data = response.json()
            print(data)
            return str(data)
      else:
            print('Error:', response.status_code)


getPassword('22','6','22','9')


# month = 1#int(input("Enter the month: "))
# day = 22#int(input("Enter the day: "))
# hour = 8#int(input("Enter the hour: "))
# minute = 4#int(input("Enter the minute: "))

# _minutes = minutes_passed(month, day, hour, minute)
# minutes = len(bin(abs(int(_minutes)))[2:])
# print(f"Minutes passed from the first day of the year to {month}/{day} {hour}:{minute} : {minutes}")



# import datetime

# def seconds_passed(month, day, hour, minute, second):
#     current_year = datetime.datetime.now().year
#     start_of_year = datetime.datetime(current_year, 1, 1)
#     specific_time = datetime.datetime(current_year, month, day, hour, minute, second)
#     time_passed = specific_time - start_of_year
#     seconds_passed = int(time_passed.total_seconds())
#     return len(bin(seconds_passed)[2:])

# month = int(input("Enter the month: "))
# day = int(input("Enter the day: "))
# hour = int(input("Enter the hour: "))
# minute = int(input("Enter the minute: "))
# second = int(input("Enter the second: "))

# seconds = seconds_passed(month, day, hour, minute, second)
# print(f"Seconds passed since the start of current year for {month}/{day} {hour}:{minute}:{second} in binary: {seconds}")
