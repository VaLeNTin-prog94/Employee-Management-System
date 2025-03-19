import random
import string
from employee_db import EmployeeDB

def generate_random_employee():
    """Генерация случайного сотрудника."""
    first_letter = random.choice(string.ascii_uppercase)
    name = first_letter + ''.join(random.choices(string.ascii_lowercase, k=6))
    surname = ''.join(random.choices(string.ascii_lowercase, k=7)).capitalize()
    full_name = f"{surname} {name}"
    birth_date = f"{random.randint(1960, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    gender = random.choice(["Male", "Female"])
    return full_name, birth_date, gender

def generate_bulk_data():
    """Генерация и добавление большого количества сотрудников в базу данных."""
    employees = [generate_random_employee() for _ in range(999900)]
    employees += [(f"F{random.choice(string.ascii_lowercase * 6).capitalize()} {random.choice(string.ascii_uppercase)}",
                   f"{random.randint(1960, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                   "Male") for _ in range(100)]
    EmployeeDB.bulk_insert(employees)
    print("Массовые данные успешно добавлены.")

if __name__ == "__main__":
    generate_bulk_data()
