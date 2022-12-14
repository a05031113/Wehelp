# import tools I need
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import jsonify
import mysql.connector as connector
from werkzeug.security import check_password_hash, generate_password_hash
from mySQL import p


def connection():
    db = connector.connect(
        pool_name="mypool",
        pool_size=5,
        host="127.0.0.1",
        user="root",
        password=p(),
        database="website"
    )
    return db


app = Flask(__name__)
app.secret_key = "secret"

# index page


@app.route("/")
def index():
    # if already login, return to /member
    if session.get("userID"):
        return redirect("/member")
    # if not login, go to index
    else:
        return render_template("index.html")

# signup page


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    # check fill in information or not
    if not name:
        return redirect("/error?message=請輸入姓名")
    elif not username or not password:
        return redirect("/error?message=請輸入帳號, 密碼")
    elif not password == confirmation:
        return redirect("/error?message=密碼不一致")
    # check already signup or not
    try:
        db = connection()
        cursor = db.cursor()
        check_user = "SELECT username FROM member WHERE username =%s"
        user = (username,)
        cursor.execute(check_user, user)
        is_password = cursor.fetchone()
        if is_password:
            return redirect("error?message=帳號已經被註冊")
        else:
            # insert data into database
            insert = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            insert_val = (name, username, generate_password_hash(password))
            cursor.execute(insert, insert_val)
            db.commit()
            # save username into session
            select = "SELECT id, username FROM member WHERE username=%s"
            select_val = (username,)
            cursor.execute(select, select_val)
            for row in cursor:
                session["userID"] = row[0]
            # return to /member
            return redirect("/member")
    except:
        print("something wrong")
    finally:
        cursor.close()
        db.close()

# check signin data


@app.route("/signin", methods=["POST"])
def signin():
    # user data
    username = request.form.get("username")
    password = request.form.get("password")
    # if username or password are blank
    if not username or not password:
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        try:
            db = connection()
            cursor = db.cursor()
            # check username and password
            check = "SELECT password, id FROM member WHERE username = %s"
            check_val = (username,)
            cursor.execute(check, check_val)
            for member in cursor:
                if check_password_hash(member[0], password):
                    session["userID"] = member[1]
                    return redirect("/member")
            # if wrong return to error
            return redirect("/error?message=帳號或密碼輸入錯誤")
        except:
            print("something wrong")
        finally:
            cursor.close()
            db.close()

# signout and clean session and return to index


@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")

# member page


@app.route("/member")
def member():
    # if already login
    if session.get("userID"):
        try:
            db = connection()
            cursor = db.cursor()
            # show name on /member
            check_name = "SELECT name FROM member WHERE id=%s"
            check_val = (session["userID"],)
            cursor.execute(check_name, check_val)
            for name in cursor:
                name = name[0]
            # show message
            cursor.execute("""
                SELECT name, content FROM member 
                INNER JOIN message ON member.id=message.member_id 
                ORDER BY message.time DESC
                """)
            rows = []
            for row in cursor:
                rows.append([row[0], row[1]])
            return render_template("member.html", name=name, rows=rows)
        except:
            print("something wrong")
        finally:
            cursor.close()
            db.close()
    # if not login yet, need to login first
    else:
        return redirect("/")


@app.route("/api/member", methods=["GET", "PATCH"])
def api():
    # if already login
    if session.get("userID"):
        # if request is PATCH
        if request.method == "PATCH":
            db = connection()
            cursor = db.cursor()
            try:
                # get json
                rename = request.get_json()
                # update name
                change = "UPDATE member SET name = %s WHERE id = %s"
                change_val = (rename["name"], session["userID"])
                cursor.execute(change, change_val)
                db.commit()
                return jsonify({"ok": True})
            except:
                return jsonify({"error": True})
            finally:
                cursor.close()
                db.close()
        # send api to frontend
        else:
            db = connection()
            cursor = db.cursor()
            try:
                username = request.args.get("username")
                check_user = "SELECT id, name FROM member WHERE username = %s"
                check_val = (username, )
                cursor.execute(check_user, check_val)
                user_data = cursor.fetchone()
                # if find username
                if user_data:
                    data = {
                        "data": {
                            "id": user_data[0],
                            "name": user_data[1],
                            "username": username
                        }
                    }
                    return jsonify(data)
                # if not in data
                else:
                    data = {
                        "data": None
                    }
                    return jsonify(data)
            except:
                print("something error")
            finally:
                cursor.close()
                db.close()
        # if not login, go back to "/"
    else:
        return jsonify({"error": True})


@app.route("/message", methods=["POST"])
def message():
    if session.get("userID"):
        try:
            db = connection()
            cursor = db.cursor()
            # get message content
            message = request.form.get("message")
            # insert information into table of message
            insert = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
            insert_val = (session["userID"], message)
            cursor.execute(insert, insert_val)
            db.commit()
            return redirect("/member")
        except:
            print("something wrong")
        finally:
            cursor.close()
            db.close()
    else:
        return redirect("/")


@app.route("/error")
def error():
    # show error message
    message = request.args.get("message")
    return render_template("error.html", message=message)


if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(port=3000, debug=True)
