import sqlite3
import time
from config import DB_NAME


class EmployeeDB:
    """
    Класс для управления базой данных сотрудников.
    """

    @staticmethod
    def create_table():
        """Создать таблицу сотрудников, если она не существует."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_employees():
        """Получить всех сотрудников, отсортированных по ФИО."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, birth_date, gender FROM employees ORDER BY full_name")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def bulk_insert(employees):
        """Добавить в базу данных сразу несколько сотрудников."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)", employees)
        conn.commit()
        conn.close()

    @staticmethod
    def search_male_f():
        """Найти всех мужчин, чья фамилия начинается с 'F', и измерить время выполнения запроса."""
        start_time = time.time()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT full_name, birth_date, gender FROM employees WHERE gender='Male' AND full_name LIKE 'F%'")
        rows = cursor.fetchall()
        conn.close()
        execution_time = time.time() - start_time
        return rows, execution_time
