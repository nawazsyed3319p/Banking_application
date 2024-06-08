import sqlite3
def withdraw(accno,balance):
    try:
        conn=sqlite3.connect("sample.db")
        cursor=conn.cursor()
        q1="select accno,accname,balance from acct"
        cursor.execute(q1)
        records=cursor.fetchall()
        for row in records:
            if(row[0]==accno):
                q2="update acct set balance=balance-? where accno=?"
                t2=(balance,accno)
        cursor.execute(q2,t2)
        q3="insert into details(accno,accname,debit,balance) values(?,?,?,?)"
        t3=(row[0],row[1],balance,row[2]-balance)
        cursor.execute(q3,t3)
        conn.commit()
        print("data update successfully")
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
