import datetime
import sqlite3
from config import DB_NAME


class Employee:
    """
    Класс, представляющий сотрудника.
    """

    def __init__(self, full_name, birth_date, gender):
        """
        Инициализация объекта сотрудника.
        :param full_name: Полное имя сотрудника
        :param birth_date: Дата рождения в формате YYYY-MM-DD
        :param gender: Пол сотрудника (Male/Female)
        """
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender

    def age(self):
        """Рассчитать возраст сотрудника."""
        today = datetime.date.today()
        birth = datetime.datetime.strptime(self.birth_date, "%Y-%m-%d").date()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def save_to_db(self):
        """Сохранить сотрудника в базу данных."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)",
                       (self.full_name, self.birth_date, self.gender))
        conn.commit()
        conn.close()
