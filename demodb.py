import mysql.connector

mydb = mysql.connector.connect(host="localhost",port=3307,user="root",password="root")

mycursor = mydb.cursor()

mycursor.execute("select * from telusko.students")

print(mycursor.fetchall())
