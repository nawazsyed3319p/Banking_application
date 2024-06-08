import sqlite3
def insertData(accno,accname,acctype,balance):
    try:
        conn=sqlite3.connect("sample.db")
        cursor=conn.cursor()
        query1="insert into acct(accno,accname,acctype,balance)values(?,?,?,?)"
        tup1=(accno,accname,acctype,balance)
        cursor.execute(query1,tup1)
        query2="insert into details(accno,accname,credit,balance) values(?,?,?,?)"
        tup2=(accno,accname,balance,balance)
        cursor.execute(query2,tup2)
        conn.commit()
        print("data insert successfully")
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
