import sqlite3
def accountant(accno):
    try:
        conn=sqlite3.connect("sample.db")
        cursor=conn.cursor()
        query="select *from details where accno=?"
        tup=(accno,)
        cursor.execute(query,tup)
        records=cursor.fetchall()
        print("accno\taccname\tcredit\tdebit\tbalance")
        for row in records:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
            conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
