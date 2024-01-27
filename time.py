given_time = input()
is_seconds = given_time[-1] == "S"
given_time = given_time[:-1]
given_time = int(given_time)
if is_seconds:
    seconds_to_hours = given_time / 3600 
    seconds_to_hours = round(seconds_to_hours,2)
    hours = str(seconds_to_hours) + "H"
else:
    minutes_to_hours = given_time / 60 
    minutes_to_hours = round(minutes_to_hours,2)
    hours = str(minutes_to_hours) + "H"
print(hours)