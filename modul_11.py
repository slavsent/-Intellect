import sqlite3

db = sqlite3.connect("data.db")
db.execute('''CREATE TABLE IF NOT EXISTS worker (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary REAL);''')


def create():
    try:
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        while True:
            name = input("Введите имя: ")
            try:
                salary = float(input("Введите зарплату: "))
            except ValueError:
                print("Вы ввели не цифровое значение")
                continue
            data = (name, salary)
            query = "INSERT into worker (name, salary) VALUES (?, ?)"
            cursor.execute(query, data)
            db.commit()
            pr = input("Вы хотите еще добавить запись (Y/N): ")
            if pr == "N" or pr == "n":
                cursor.close()
                break

    except:
        print("Ошибка добавления записи")


def read_one():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    id_worker = int(input("Введите ID работника: "))
    query = "SELECT * from worker WHERE id = ?"
    result = cursor.execute(query, (id_worker,))
    if result:
        for i in result:
            print(f"Имя: {i[1]}")
            print(f"Зарплата: {i[2]}")
    else:
        print("Такого ID не существует")
        cursor.close()


def read_all():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    query = "SELECT * from worker"
    result = cursor.execute(query)
    if result:
        for i in result:
            print(f"Имя: {i[1]}")
            print(f"Зарплата: {i[2]}\n")
    else:
        print('В базе данных еще нет записей')


def update():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    try:
        id_worker = int(input("Введите ID: "))
        name = input("Введите имя: ")
        salary = int(input("Введите зарплату: "))
        data = (name, salary, id_worker,)
        query = "UPDATE worker set name = ?, salary = ? WHERE id = ?"
        result = cursor.execute(query, data)
        db.commit()
        cursor.close()
    except Exception:
        print('Вы ввели не верные данные')
    else:
        if result:
            print("Запись обновлена")
        else:
            print("Запись не найдена")


def delete():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    try:
        id_worker = int(input("Enter ID: "))
    except ValueError:
        print('Введены не верные данные')
    else:
        query = "DELETE from worker where ID = ?"
        result = cursor.execute(query, (id_worker,))
        db.commit()
        cursor.close()
        if result:
            print("Запись удалена")
        else:
            print("Запись с таким ID не найдена")


if __name__ == '__main__':
    try:
        while True:
            print("1. Создать запись: ")
            print("2. Просмотреть: ")
            print("3. Изменить: ")
            print("4. Удалить: ")
            print("5. Выход")
            pr = input("Введите номер пункта меню: ")
            if pr == '1':
                create()
            elif pr == '2':
                print("1. Просмотр конкретной записи")
                print("2. Просмотр всех записей")
                choice = input("Введите номер пункта меню: ")
                if choice == '1':
                    read_one()
                elif choice == '2':
                    read_all()
                else:
                    print("Вы ввели не верный пункт меню")
            elif pr == '3':
                update()
            elif pr == '4':
                delete()
            elif pr == '5':
                break
            else:
                print("Вы ввели не верный пункт меню")
    except:
        print("Ошибка работы с БД")
