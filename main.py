from model import mode_1_create_table, mode_2_add_employee, mode_3_list_employees, mode_4_bulk_insert, \
    mode_5_search_male_f, mode_6_optimize


def main():
    """Главная точка входа в программу."""
    print("Выберите режим работы приложения:")
    print("1 - Создать таблицу сотрудников")
    print("2 - Добавить сотрудника")
    print("3 - Вывести всех сотрудников")
    print("4 - Массовое добавление сотрудников")
    print("5 - Поиск сотрудников (пол Male, фамилия с 'F')")
    print("6 - Оптимизация базы данных")

    choice = input("Введите номер режима: ")

    if choice == "1":
        mode_1_create_table.create_table()
    elif choice == "2":
        mode_2_add_employee.add_employee()
    elif choice == "3":
        mode_3_list_employees.list_employees()
    elif choice == "4":
        mode_4_bulk_insert.generate_bulk_data()
    elif choice == "5":
        mode_5_search_male_f.search_male_f()
    elif choice == "6":
        mode_6_optimize.optimize_database()
    else:
        print("Некорректный ввод. Пожалуйста, выберите существующий режим.")


if __name__ == "__main__":
    main()
