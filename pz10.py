import mysql.connector
from mysql.connector import Error

def test_user(user, password):
    print(f"\nПодключение как {user}")
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=user,
            password=password,
            database='university1'
        )
        cursor = connection.cursor()

        print("Пробуем выполнить SELECT на view_groups:")
        try:
            cursor.execute("SELECT * FROM view_groups;")
            print(cursor.fetchall())
        except Error as e:
            print("Ошибка при доступе к view_groups:", e)
        print("Пробуем выполнить SELECT на view_grades:")
        try:
            cursor.execute("SELECT * FROM view_grades;")
            print(cursor.fetchall())
        except Error as e:
            print("Ошибка при доступе к view_grades:", e)

        cursor.close()
        connection.close()

    except Error as e:
        print("Ошибка подключения или выполнения запроса:", e)

users = [
    ('user_g', 'guest123'),
    ('user_s', 'stud123'),
    ('user_t', 'teach123')
]

for user, password in users:
    test_user(user, password)