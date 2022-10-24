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
rows = []
def test():
    for row in cursor:
        rows.append([row[0], row[2]])
        if row[1] == "test2":
            user = row[0]
    return user

print(test())
print(rows)