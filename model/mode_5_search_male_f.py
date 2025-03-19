from employee_db import EmployeeDB

def search_male_f():
    """Поиск сотрудников мужского пола, чья фамилия начинается с 'F'."""
    results, exec_time = EmployeeDB.search_male_f()
    for emp in results:
        print(emp)
    print(f"Время выполнения: {exec_time:.4f} секунд")

if __name__ == "__main__":
    search_male_f()
