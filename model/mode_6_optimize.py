import sqlite3
from config import DB_NAME

def optimize_database():
    """Оптимизация базы данных: добавление индекса."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_full_name ON employees (full_name)")
    conn.commit()
    conn.close()
    print("Индекс успешно создан.")

if __name__ == "__main__":
    optimize_database()
