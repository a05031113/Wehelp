# import tools I need
from flask import Flask, request, redirect, render_template, session, url_for, make_response, Response
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key="secret"
key = Fernet.generate_key()
f = Fernet(key)

# index page
@app.route("/", methods=["GET", "POST"])
def index(): 
    # if already login, return to /member
    # session way: 
    # if session.get("userID")
    if request.cookies.get("username"):
        return redirect("/member")
    # if not login, go to index 
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
        # if username of password is blank
        if not username or not password:
            return redirect("/error?messange=請輸入帳號、密碼")
        # if username and password is test
        elif username=="test" and password=="test":
            # write into cookies
            byteUsername = str.encode(username)
            cipher = f.encrypt(byteUsername)
            resp = make_response(redirect("/member"))
            resp.set_cookie("username", cipher)
            return resp
            # by session way
            # session["userID"]=username
            # session["userPass"]=password
            # return redirect("/member")
        # if one of it is wrong
        else:
            return redirect("/error?messange=帳號或密碼輸入錯誤")
    else:
        return render_template("index.html")

# signout and clean session and return to index
@app.route("/signout")
def signout():
    # session.clear() # session clear
    res = make_response(redirect("/"))
    res.delete_cookie("username")
    return res
    # session way
    # session.clear()
    # return redirect("/")

# member page
@app.route("/member", methods=["GET", "POST"])
def member(): 
    # if already login
    if request.cookies.get("username"):
        return render_template("member.html")
    # if not login yet, need to login first
    else:
        return redirect(url_for("index"))

# if something wrong
@app.route("/error")
def error():
    # show error messange
    messange = request.args.get("messange")
    return render_template("error.html", messange=messange)

# calculate square of number
@app.route("/square/<number>")
def square(number):
    num = int(number)
    nStr = str(num*num)
    return render_template("square.html", num=nStr)

if __name__=="__main__":
    app.secret_key="secret"
    app.run(port=3000, debug=True)