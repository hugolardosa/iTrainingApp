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
                            [Address] text,
                            [City] text,
                            [Phone_Number] INTEGER,
                            [Postal_Code] INTEGER);"""

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
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
    
    'PT_DETAILS': '''INSERT INTO PERSONAL_TRAINERS(email, PT_Name, Password, Address, City, Phone_Number, Postal_Code)
                VALUES (?,?,?,?,?,?,?)'''

}


def create_entry_db(sql_table, values):
    conn = sqlite3.connect('databases/' + db)
    c = conn.cursor()
    sql = table_prototipe.get(sql_table)
    task = values
    c.execute(sql, task)
    conn.commit()
    conn.close()
