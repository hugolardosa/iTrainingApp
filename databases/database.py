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

    'CHECK_PASSWORD': '''SELECT PASSWORD FROM CLIENT_DETAILS WHERE email == ? ''',

    'CHECK_EMAIL': '''SELECT EMAIL FROM CLIENT_DETAILS WHERE email == ? ''',

    'GET_PT': '''SELECT ? from PERSONAL_TRAINERS WHERE email == ?''',

    'GET': '''SELECT ? FROM ? WHERE ? == ?'''
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
    tmp = None
    if selection is None:
        c.execute(sql, (element,))
        tmp = c.fetchone()
    else:
        c.execute(sql, (selection, element))

    if tmp is not None:
        return tmp

    if tmp is None:
        if sql_table is 'CHECK_PASSWORD':
            c.execute('''SELECT PASSWORD FROM PERSONAL_TRAINERS WHERE email == ?''', (element,))
        elif sql_table is 'CHECK_EMAIL':
            c.execute('''SELECT EMAIL FROM PERSONAL_TRAINERS WHERE email == ?''', (element,))
        return c.fetchone()
    return c.fetchone()


def get(sql_table, selection, e1, element):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    sql = table_prototipe.get(sql_table)
    c.execute(sql, (selection, e1, element,))
    return c.fetchone()


def setondb(personid, values):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    table=''
    tmp = ['EMAIL','CLIENT_NAME','PASSWORD','ADDRESS','CITY','PHONE_NUMBER','POSTAL_CODE','BIRTHDAY','WEIGHT','HEIGHT','OBJ','PROBLEMS']
    c.execute('''SELECT EMAIL FROM CLIENT_DETAILS WHERE EMAIL==?''',(personid,))
    t=c.fetchone()
    if  t is None:
        for val in values:
            x=tmp.pop(0)
            if val is not None:
                c.execute('''UPDATE PERSONAL_TRAINERS SET ? \
                        = ? WHERE email== ?''',( x, val, personid))
    else:
        for val in values:
            x=tmp.pop(0)
            if val is not None:
                c.execute('''UPDATE CLIENT_DETAILS SET ? \
                
                = ? WHERE email== ?''',( x, val, personid))



