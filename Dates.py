from datetime import datetime, timedelta
start_date = input("Enter From Date: ")
end_date = input("Enter To Date: ")
day_start = datetime.strptime(start_date, "%b %d %Y")
day_end = datetime.strptime(end_date, "%b %d %Y")
number_of_days = (day_end - day_start).days
for char in range(number_of_days + 1):
    print(day_start + timedelta(days = char))