import mysql.connector
mydb = mysql.connector.connect(host="localhost",
        user="root",
        password="root",
        port="3306",
        database="coco")
mycursor = mydb.cursor()
# print(mycursor.fetchall())


def createuser(username, password):
    mycursor.execute(f'INSERT INTO USERS(username, password) VALUES ("{username}", "{password}")')
    mydb.commit()