import sqlite3

cursor = None


def db_connection():
    return sqlite3.connect("dvd_store_mng.db")


def insert_tb(tb_name, val_list=None):
    if val_list is None:
        val_list = []
    _db_con = db_connection()
    try:
        _i_cursor = _db_con.cursor()
        _i_query = f"INSERT INTO {tb_name} VALUES ("
        _i_query += "?, " * (len(val_list) - 1) + "?);"
        _i_cursor.execute(_i_query, val_list)
        _db_con.commit()
        # print("Completed!")
    except sqlite3.Error as error:
        print(error)
    finally:
        if _db_con:
            _db_con.close()


def select_tb(query=None, tb_name=None, condition=None):
    _db_con = db_connection()
    try:
        _s_cursor = _db_con.cursor()
        _s_query = query
        if query is None:
            _s_query = f"select * from {tb_name}"
        if condition:
            _s_query += f" {condition}"

        _s_cursor.execute(_s_query)
        return _s_cursor.fetchall()
    except sqlite3.Error as error:
        print(error)
    finally:
        _db_con.close()


def update_tb(tb_name, col_name, value, condition):
    _db_con = db_connection()
    try:
        _u_cursor = _db_con.cursor()
        _u_query = f"UPDATE {tb_name} SET {col_name} = {value} {condition}"
        _u_cursor.execute(_u_query)
        _db_con.commit()
    except sqlite3.Error as error:
        print(error)


def delete_tb_data(tb_name, condition):
    _db_con = db_connection()
    try:
        _d_cursor = _db_con.cursor()
        _d_query = f"Delete from {tb_name} where {condition};"
        _d_cursor.execute(_d_query)
        _db_con.commit()
        print("The Record is successfully deleted!")
    except sqlite3.Error as error:
        print("Fail to delete record, contact database admin.", error)


if __name__ == '__main__':
    print(select_tb("rental", " join copies_dvd on copies_dvd.c_dvd_id = rental.c_dvd_id where rental.acc_num = 1001 "))
