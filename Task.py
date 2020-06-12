from datetime import time
from datetime import date


class Task:
    def __init__(self):
        self._description = ""
        self._due_date = ""  # MySql type DATE
        self._due_time = ""  # MySql type TIME

    def set_description(self):
        self._description = input("What would you like to be reminded of?\n")

    def get_description(self):
        return self._description

    def set_due_date(self):
        print("When is the task due? (format: YYYY MM DD)\n")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        self._due_date = date(year, month, day).strftime('%Y-%m-%d')

    def get_due_date(self):
        return self._due_date

    def set_due_time(self):
        print("\nTime? (format: HH:MM)")
        h = int(input("Hour: "))
        m = int(input("Minutes: "))
        self._due_time = time(h, m).strftime('%H:%M:%S')

    def get_due_time(self):
        return self._due_time
