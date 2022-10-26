# from mysql.connector.pooling import MySQLConnectionPool
import mysql.connector as connector
from mySQL import p

db = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = p(),
    database = "website"
)



