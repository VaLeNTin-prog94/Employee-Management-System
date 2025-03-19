# Employee Management System

## 📌 Описание проекта
Этот проект представляет собой консольное приложение для управления сотрудниками, работающее с базой данных SQLite. Приложение поддерживает добавление, просмотр, поиск и оптимизацию данных. 

## 📂 Структура проекта
```
myApp/
│── model/
│   │── __init__.py
│   │── mode_1_create_table.py
│   │── mode_2_add_employee.py
│   │── mode_3_list_employees.py
│   │── mode_4_bulk_insert.py
│   │── mode_5_search_male_f.py
│   │── mode_6_optimize.py
│   │── employee.py
│   │── employee_db.py
│── employees.db
│── config.py
│── main.py
│── app.log
```

## 🚀 Запуск приложения

1. **Создайте виртуальное окружение (рекомендуется)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate     # Для Windows
   ```
2. **Установите зависимости (если необходимо)**
   ```bash
   pip install -r requirements.txt
   ```
3. **Запустите `main.py` и выберите режим работы**
   ```bash
   python main.py
   ```

## 📌 Описание файлов

### `main.py`
Запускает программу и предлагает пользователю выбрать один из режимов работы:
- `1` – Создание таблицы сотрудников.
- `2` – Добавление сотрудника.
- `3` – Вывод всех сотрудников.
- `4` – Массовая вставка данных.
- `5` – Поиск сотрудников (пол Male, фамилия с 'F').
- `6` – Оптимизация базы данных.

### `config.py`
Содержит параметры базы данных:
```python
DB_NAME = "employees.db"
```

### `employee.py`
Содержит класс `Employee`, который отвечает за данные сотрудников.

#### Методы:
- `__init__(full_name, birth_date, gender)`: инициализирует объект сотрудника.
- `age()`: рассчитывает возраст сотрудника.
- `save_to_db()`: сохраняет сотрудника в базу данных.

### `employee_db.py`
Отвечает за работу с базой данных.

#### Методы:
- `create_table()`: создаёт таблицу `employees`, если она не существует.
- `get_all_employees()`: возвращает список всех сотрудников.
- `bulk_insert(employees)`: выполняет массовую вставку данных.
- `search_male_f()`: ищет сотрудников мужского пола, чья фамилия начинается с 'F', и замеряет время выполнения.

### `mode_1_create_table.py`
Создаёт таблицу сотрудников в базе данных.
```python
EmployeeDB.create_table()
```

### `mode_2_add_employee.py`
Позволяет пользователю вручную ввести данные сотрудника и добавить его в базу данных.
```python
full_name = input("Введите ФИО: ")
birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
gender = input("Введите пол (Male/Female): ")
emp = Employee(full_name, birth_date, gender)
emp.save_to_db()
```

### `mode_3_list_employees.py`
Выводит всех сотрудников, отсортированных по ФИО, и рассчитывает их возраст.
```python
employees = EmployeeDB.get_all_employees()
for emp in employees:
    emp_obj = Employee(emp[0], emp[1], emp[2])
    print(f"{emp[0]}, {emp[1]}, {emp[2]}, {emp_obj.age()} лет")
```

### `mode_4_bulk_insert.py`
Генерирует и добавляет **1 000 000 сотрудников**, включая **100 сотрудников с фамилией, начинающейся на 'F'**.
```python
employees = [generate_random_employee() for _ in range(999900)]
employees += [("F" + random.choice(string.ascii_lowercase * 6).capitalize(), ...)]
EmployeeDB.bulk_insert(employees)
```

### `mode_5_search_male_f.py`
Ищет сотрудников **мужского пола**, чья фамилия начинается с **'F'**, и замеряет время выполнения запроса.
```python
results, exec_time = EmployeeDB.search_male_f()
print(f"Время выполнения: {exec_time:.4f} секунд")
```

### `mode_6_optimize.py`
Создаёт **индекс** на поле `full_name` для ускорения поиска.
```python
cursor.execute("CREATE INDEX IF NOT EXISTS idx_full_name ON employees (full_name)")
```

## 📊 Оптимизация

Перед оптимизацией запрос выполнялся медленно, так как **SQLite сканировал всю таблицу**.

После создания **индекса** запрос стал быстрее, так как база данных использует **B-дерево (B-tree)** для быстрого поиска по `full_name`.

## 📌 Итоги
✅ Поддержка базы данных SQLite.
✅ Разделение логики на отдельные файлы.
✅ Удобный ввод данных через консоль.
✅ Массовая вставка и оптимизированный поиск.
✅ Логирование событий (`app.log`).

---
💡 **Проект готов к использованию!** 🚀
