import mysql.connector
mydb = mysql.connector.connect(host="localhost",
        user="root",
        password="root",
        port="3306",
        database="coco")


def checkforusername(username):
    mycursor = mydb.cursor()
    mycursor.execute("select * from users")
    users = mycursor.fetchall()
    for names in users:

        if names[0] == username:
            return True
        else:
            pass


def checkforpassword(password):
    mycursor = mydb.cursor()
    mycursor.execute("select * from users")
    users = mycursor.fetchall()
    print(users)
    for passwords in users:
        if passwords[1] == password:
            return True
        else:
            pass