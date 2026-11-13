import sqlite3


def get_connection():
    return sqlite3.connect('app.db')


def show_menu():
    print("\n===== СПИСОК ЗАДАЧ =====")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Задача выполнена")
    print("4. Удалить задачу")
    print("0. Выход")


def main():
    while True:
        show_menu()
        choice = input("Выбери действие: ").strip()

        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            delete_task()
        elif choice == '0':
            print("До встречи!")
            break
        else:
            print("Нет такого пункта.")


if __name__ == '__main__':
    main()