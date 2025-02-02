import random

def check_attendance():
    return random.randint(0, 1)  

def emp_daily_wage():
    wage_per_hour = 20
    emp_check = check_attendance()
    
    if emp_check == 1:
        daily_wage = wage_per_hour * 4
        print(f"The employee is present, so the daily wage is: {daily_wage}")
    else:
        daily_wage = 0
        print(f"The employee is absent, so the daily wage is: {daily_wage}")


emp_daily_wage()


