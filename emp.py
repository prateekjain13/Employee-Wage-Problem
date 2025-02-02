import random

def check_attendance():
    return random.randint(0, 1)

def emp_monthly_wage():
    wage_per_hour = 20
    total_working_hours = 100
    total_working_days = 20
    total_hours_worked = 0
    total_days_worked = 0
    total_wage = 0
    
    while total_hours_worked < total_working_hours and total_days_worked < total_working_days:
        emp_check = check_attendance()
        if emp_check == 1:
            total_hours_worked += 8
            total_days_worked += 1
            total_wage += wage_per_hour * 8
    
    print(f"The total monthly wage for the employee is: {total_wage}")

emp_monthly_wage()


