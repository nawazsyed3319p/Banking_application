import sqlite3
def Display():
    try:
        conn=sqlite3.connect("sample.db")
        cursor=conn.cursor()
        query="select *from acct"
        cursor.execute(query)
        records=cursor.fetchall()
        print("accno\taccname\tacctype\tbalance")
        for row in records:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
