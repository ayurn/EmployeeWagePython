"""
@Author: Ayur Ninawe
@Date: 2021-06-27 17:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-27 17:30:30
@Title : Employee Wage Computation.

"""

import random

print("Welcome to Employee Wage Computation")

WAGE_PER_HOUR = 20
FULL_TIME_HOURS = 8
PART_TIME_HOURS = 4
DAYS_FOR_MONTH = 20
day_hour = 0


def is_absent():
    """
    executes when employee is absent
    :return: day hour as 0 when employee is absent
    """
    return day_hour


def is_full_time():
    """
    executes when employee type is full time
    :return: day hours as 8
    """
    return FULL_TIME_HOURS


def is_part_time():
    """
    executes when employee type is part time
    :return: day hours as 4
    """
    return PART_TIME_HOURS


employee_status = {0: is_absent, 1: is_full_time, 2: is_part_time}
attendance_check = random.randint(0, 2)
day_hour = employee_status.get(attendance_check)()

daily_employee_wage = WAGE_PER_HOUR * day_hour
employee_wage = daily_employee_wage * DAYS_FOR_MONTH
print("employee wage is : ", employee_wage)