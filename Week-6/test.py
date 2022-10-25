import mysql.connector as connector

db = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Password",
    database = "website"
)

cursor = db.cursor()

cursor.execute("""
            SELECT name, username, content FROM member 
            INNER JOIN message ON member.id=message.member_id 
            ORDER BY message.time DESC
            """)
for i in cursor:
    print(i)