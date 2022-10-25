import mysql.connector as connector

db = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Password",
    database = "website"
)

cursor = db.cursor()

check = "SELECT username FROM member WHERE username = %s"
val = ("a",)
cursor.execute(check, val)
l = []
for i in cursor:
    l.append(i)

print(len(l))

