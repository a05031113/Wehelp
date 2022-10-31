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

check_user = "SELECT id, name FROM member WHERE username = %s"
check_val = ("check", )
cursor.execute(check_user, check_val)
user_data = cursor.fetchone()

print(user_data[0])

