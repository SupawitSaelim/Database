import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Oat0811609596mysql.',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'canyon 123' WHERE address = 'valley 345'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount,'record(s) affected')