import sqlite3

db = 'database.db'

sql_client_details_table = """ CREATE TABLE IF NOT EXISTS CLIENT_DETAILS(
                                        [email] text, 
                                        [Client_Name] text, 
                                        [Password] text , 
                                        [Address] text, 
                                        [City] text,
                                        [Phone_Number] INTEGER,
                                        [Postal_Code] INTEGER, 
                                        [Birthday] text, 
                                        [Weight] INTEGER, 
                                        [Height] INTEGER, 
                                        [Obj] text, 
                                        [Problems] text);"""
sql_PT_table = """ CREATE TABLE IF NOT EXISTS PERSONAL_TRAINERS(
                            [email] text,
                            [PT_Name] text,
                            [Password] text,
                            [Code] text,
                            [Address] text,
                            [City] text,
                            [Phone_Number] INTEGER,
                            [Postal_Code] INTEGER);"""

sql_train_table = """ CREATE TABLE IF NOT EXISTS TRAIN(
                            [Client] text,
                            [Exercise] text,
                            [Reps] INTEGER,
                            [Material] text,
                            [ExTime] INTEGER,
                            [Inst] text);"""


def create_db():
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()

    # CLIENT DETAILS
    c.execute(sql_client_details_table)
    c.execute(sql_PT_table)

    c.close()
    conn.commit()
    conn.close()


def edit_db(sql_table, values, client):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    for val in values:
        sql = ''' UPDATE ?
                  SET ? = ? ,
                  WHERE Client_Name = ?'''
        task = (sql_table, val[0], val[1], client)
        c.execute(sql, task)

    conn.commit()
    conn.close()


table_prototipe = {
    'CLIENT_DETAILS': ''' INSERT INTO CLIENT_DETAILS(email, Client_Name, Password, Address, City, Phone_Number, Postal_Code,Birthday,Weight,Height,Obj,Problems) 
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',

    'PT_DETAILS': '''INSERT INTO PERSONAL_TRAINERS(email, PT_Name, Password, Code, Address, City, Phone_Number, Postal_Code)
                VALUES (?,?,?,?,?,?,?,?)''',

    'ADD_TRAIN': '''INSERT INTO TRAIN(Client, Exercise, Reps, Material, Extime, Inst)
                VALUES (?,?,?,?,?,?)''',

    'CHECK_PASSWORD': '''SELECT Password FROM CLIENT_DETAILS WHERE email == ?
                VALUES (?)''',

    'GET_PT': '''SELECT ? from PERSONAL_TRAINER WHERE email == ?
            VALUES (?,?)'''
}


def create_entry_db(sql_table, values):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    sql = table_prototipe.get(sql_table)
    task = values
    c.execute(sql, task)
    conn.commit()
    conn.close()


def get_element(sql_table, selection, element):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    sql = table_prototipe.get(sql_table)
    if selection is None:
        c.execute(sql, element)
    else:
        c.execute(sql, (selection,element))
    if c is None and sql_table is 'CHECK_PASSWORD':
        c.execute('''SELECT PASSWORD FROM PERSONAL_TRAINER WHERE email == ? VALUES (?)''', element)
        return c
    return c
#TODO