import random

def check_attendance():
    return random.randint(0, 1)

def emp_monthly_wage():
    wage_per_hour = 20
    working_days_in_month = 20
    total_wage = 0
    
    for i in range(working_days_in_month):
        emp_check = check_attendance()
        if emp_check == 1:
            total_wage += wage_per_hour * 8
        else:
            total_wage += 0
    
    print(f"The total monthly wage for the employee is: {total_wage}")

emp_monthly_wage()

