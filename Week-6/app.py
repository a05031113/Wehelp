# import tools I need
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector as connector
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

db = connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "website"
)
cursor = db.cursor()

app = Flask(__name__)
app.secret_key="secret"

# index page
@app.route("/", methods=["GET", "POST"])
def index(): 
    # if already login, return to /member
    if session.get("userID"):
        return redirect("/member")
    # if not login, go to index 
    else:
        return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if request.method == "POST":
        # check fill in information or not
        if not name:
            return redirect("/error?message=請輸入姓名")
        elif not username or not password:
            return redirect("/error?message=請輸入帳號, 密碼")
        elif not password == confirmation:
            return redirect("/error?message=密碼不一致")
        # collect data form member
        checkUser = "SELECT username FROM member WHERE username =%s"
        User = (username,)
        cursor.execute(checkUser, User)
        checklist = []
        for row in cursor:
            checklist.append(row)
        if len(checklist) == 1:
            return redirect("error?message=帳號已經被註冊")
        else:
            # insert data into database
            now = datetime.now()
            date_now = now.strftime("%y-%m-%d %H:%M:%S")
            insert = "INSERT INTO member (name, username, password, time) VALUES (%s, %s, %s, %s)"
            insertVal = (name, username, generate_password_hash(password), date_now)
            cursor.execute(insert, insertVal)
            db.commit()
            # save username into session
            session["userID"]=username
            # return to /member
            return redirect("/member")
    else:
        return render_template("index.html")

# check signin data
@app.route("/signin", methods=["GET", "POST"])
def signin():
    # if "post"
    if request.method == "POST":
        # user data 
        username = request.form.get("username")
        password = request.form.get("password")
        # if username or password are blank
        if not username or not password:
            return redirect("/error?message=請輸入帳號、密碼")
        else:
            # check username and password
            check = "SELECT password FROM member WHERE username = %s"
            checkVal = (username,)
            cursor.execute(check, checkVal)
            for member in cursor:
                if check_password_hash(member[0], password):
                    session["userID"]=username
                    return redirect("/member")
            # if wrong return to error
            return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        return render_template("index.html")

# signout and clean session and return to index
@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")

# member page

@app.route("/member", methods=["GET", "POST"])
def member(): 
    # if already login
    if session.get("userID"):
        # show name on /member
        checkName = "SELECT name FROM member WHERE username=%s"
        checkVal = (session["userID"],)
        cursor.execute(checkName, checkVal)
        for name in cursor:
            name = name[0]
        # show message
        cursor.execute("""
            SELECT name, username, content FROM member 
            INNER JOIN message ON member.id=message.member_id 
            ORDER BY message.time DESC
            """)
        rows = []
        for row in cursor:
            rows.append([row[0], row[2]])
        return render_template("member.html", name=name, rows=rows)
    # if not login yet, need to login first
    else:
        return redirect("/")

@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        # get message content
        message = request.form.get("message")
        # get user's member_id
        checkId = "SELECT id FROM member WHERE username=%s"
        checkVal = (session["userID"],)
        cursor.execute(checkId, checkVal)
        for id in cursor:
            member_id = id
        # insert information into table of message
        now = datetime.now()
        date_now = now.strftime("%y-%m-%d %H:%M:%S")
        insert = "INSERT INTO message (member_id, content, time) VALUES (%s, %s, %s)"
        insertVal = (member_id[0], message, date_now)
        cursor.execute(insert, insertVal)
        db.commit()
        return redirect("/member")
    else:
        return redirect("/member")


# if something wrong
@app.route("/error")
def error():
    # show error messange
    message = request.args.get("message")
    return render_template("error.html", message=message)

if __name__=="__main__":
    app.secret_key="secret"
    app.run(port=3000, debug=True)