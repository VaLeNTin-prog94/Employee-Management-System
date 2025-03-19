from employee_db import EmployeeDB
from employee import Employee

def list_employees():
    """Вывести список всех сотрудников."""
    employees = EmployeeDB.get_all_employees()
    for emp in employees:
        emp_obj = Employee(emp[0], emp[1], emp[2])
        print(f"{emp[0]}, {emp[1]}, {emp[2]}, {emp_obj.age()} лет")

if __name__ == "__main__":
    list_employees()
