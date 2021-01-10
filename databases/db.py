import os
import sqlite3

db = 'database.db'


def create_db():
    if not os.path.isfile(db):
        conn = sqlite3.connect(db)
        c = conn.cursor()

        c.execute('''CREATE TABLE CLIENT_LOGIN
            ([ID] INTEGER PRIMARY KEY, [email] text, [Password] text''')

        c.execute('''CREATE CLIENT_DETAILS
                    ([email] text, [Client_Name] text ,[Password] text , [Address] text, [Phone_Number] INTEGER, \
                    [Postal_Code] INTEGER, [Birthday] text, [Weight] INTEGER, [Height] INTEGER, [Obj] text, \
                    [Problems] text''')
        c.close()
        conn.commit()
        conn.close()
