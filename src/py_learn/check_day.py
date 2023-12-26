import datetime

today = datetime.date.today()
week_number = today.isocalendar()[1]
day_of_week = today.weekday()

print(f"Today is week {week_number}, day {day_of_week+1} of the week.")