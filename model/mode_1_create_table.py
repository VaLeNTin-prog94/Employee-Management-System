from employee_db import EmployeeDB

def create_table():
    """Создать таблицу сотрудников."""
    EmployeeDB.create_table()
    print("Таблица успешно создана.")

if __name__ == "__main__":
    create_table()
