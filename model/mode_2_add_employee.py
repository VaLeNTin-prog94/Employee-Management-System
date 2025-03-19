import sys
from employee import Employee


def add_employee():
    """Добавить нового сотрудника в базу данных."""
    full_name = input("Введите ФИО: ")
    birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
    gender = input("Введите пол (Male/Female): ")

    emp = Employee(full_name, birth_date, gender)
    emp.save_to_db()
    print(f"Сотрудник {full_name} успешно добавлен.")


if __name__ == "__main__":
    add_employee()
