import sqlite3
def Balanceenquery(accno):
    try:
        conn=sqlite3.connect("sample.db")
        cursor=conn.cursor()
        query="select balance from acct where accno=?"
        tup=(accno,)
        cursor.execute(query,tup)
        bal=cursor.fetchone()
        balance=bal[0]
        print("Balance amount:",balance)
        conn.commit()
        print("data update successfully")
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
