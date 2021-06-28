"""
@Author: Ayur Ninawe
@Date: 2021-06-27 17:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-27 17:30:30
@Title : Employee Wage Computation.
"""

import random
print("Wellcome to employee wage computation")

def calculate_Hour(employee_status):
    """
    Description:
        this function determine the work hours
    Parameter:
        employee_status is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if employee_status == is_full_time:
        day_hour = 8
    elif employee_status == is_part_time:
        day_hour = 4 
    else:
        day_hour = 0
    return day_hour
    

def calculate_Wage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    daily_wage_list = []
    wage_data_dict = {}
    WAGE_PER_HOUR = 20
    DAYS_FOR_MONTH = 20
    HOURS_FOR_MONTH = 100
    working_days = 0
    total_working_hours = 0
    total_wage = 0
    while working_days < DAYS_FOR_MONTH and total_working_hours < HOURS_FOR_MONTH:
        attendance = random.randint(0,2)
        employee_status = switcher.get(attendance)
        working_hours = calculate_Hour(employee_status)
        daily_wage = working_hours * WAGE_PER_HOUR
        daily_wage_list.append(daily_wage)
        total_wage +=daily_wage
        total_working_hours += working_hours
        working_days += 1

        wage_data_dict ["Day "+str(working_days+1)]= {
        "daily_wage": daily_wage,
        "total_wage": total_wage
        }
    #print("Daily wage:", daily_wage_list)
    #return total_wage
    return wage_data_dict

absent = 0
is_full_time = 1
is_part_time = 2

switcher = {
    0: absent,
    1: is_full_time,
    2: is_full_time,
}

print("Total employee wage for month is:",calculate_Wage())