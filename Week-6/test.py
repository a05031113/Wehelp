# from mysql.connector.pooling import MySQLConnectionPool
import mysql.connector as connector
from mySQL import p

db = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = p(),
    database = "website"
)

cursor = db.cursor()

checkUser = "SELECT username FROM member WHERE username =%s"
User = ("aaaaaa",)
cursor.execute(checkUser, User)
f = cursor.fetchone()

if f:
    print("true")

