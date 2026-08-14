from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(_name_)
app.secret_key = "mysecretkey"


def get_db():
    return sqlite3.connect("blog.db")


@app.route("/")
def home():
    db = get_db()
    posts = db.execute("SELECT * FROM posts").fetchall()
    db.close()
    return render_template("home.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        db.commit()
        db.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        db.close()

        if user:
            session["username"] = username
            return redirect("/")

        return "Invalid username or password"

    return render_template("login.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if "username" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        db = get_db()
        db.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content)
        )
        db.commit()
        db.close()

        return redirect("/")

    return render_template("create.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")


if _name_ == "_main_":
    app.run(debug=True)
