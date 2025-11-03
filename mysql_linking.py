import mysql.connector
mycon = mysql.connector.connect(host="localhost",user="root",password="ABC123",database="NEW")
if mycon.is_connected():
    print("conncetion established")
    cursor=mycon.cursor()
    cursor.execute("select*from books_issued")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total number of rows retrived in resultset: ",count)
    for row in data:
        print(row)
