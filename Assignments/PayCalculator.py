def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
    overtime_pay = overtime_hours * 1.5 * hourly_wage
    total_weekly_pay = (hourly_wage * regular_hours) + overtime_pay
    return overtime_pay, total_weekly_pay

def process_employee_details(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            employee_info = line.strip().split(',')
            employee_name = employee_info[1]
            hourly_wage = float(employee_info[2])
            regular_hours = float(employee_info[3])
            overtime_hours = float(employee_info[4])

            overtime_pay, total_weekly_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)

            # Save results in a new file with the employee's name
            output_file_path = employee_name + '.txt'
            with open(output_file_path, 'w') as output_file:
                output_file.write(f'Overtime Pay: {overtime_pay}\n')
                output_file.write(f'Total Weekly Pay: {total_weekly_pay}\n')

# Provide the file path to the "Employee_details" file
file_path = 'Employee_details.txt'
process_employee_details(file_path)
