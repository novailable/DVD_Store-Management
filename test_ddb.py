import sqlite3

try:
    #grave_accent
    db_connection = sqlite3.connect("test_db.db")
    sql_query = "CREATE TABLE if not exists `customer` (`idcustomer` INT GENERATED, \
                `fName` VARCHAR(45) NULL,\
                `lName` VARCHAR(45) NULL,\
                `acc_no` VARCHAR(45) NOT NULL,\
                PRIMARY KEY (`idcustomer`, `acc_no`))"
    insert_query = "INSERT INTO customer VALUE 'column1'; "
    cursor = db_connection.cursor()
    cursor.execute(sql_query)
    cursor.execute(insert_query)
    db_connection.commit()      #commit to database

except sqlite3.Error as error:
    print(error)
finally:
    if db_connection:
        print("closing")
        db_connection.close()