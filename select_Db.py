import sqlite3

try:
    db_connection = sqlite3.connect("test_db.db")
    query = "select name from sqlite_schema where type= 'table';"
    cursor = db_connection.cursor()
    cursor.execute(query)
    test = cursor.fetchall()
    print(test)
except sqlite3.Error as error:
    print(error)
finally:
    db_connection.close()