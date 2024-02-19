import sqlite3
from contextlib import closing

from flask import Flask, Response, redirect, render_template, request, url_for

app = Flask(__name__)
conn = sqlite3.connect("database.db", check_same_thread=False)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "hash" not in request.form or "password" not in request.form:
            return Response("Invalid request parameters passed.", content_type="text/plain")

        hash = request.form["hash"]
        password = request.form["password"]

        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT * FROM users WHERE hash=? AND password=?", (hash, password))
            data = cursor.fetchall()
            if len(data) < 1:
                return Response("Error: Invalid credentials entered.", content_type="text/plain")

        return redirect(url_for("details_page", user=hash))

    return render_template("index.html")


@app.route("/details")
def details_page():
    user = request.args.get("user", None)
    if not user:
        return render_template("details.html", detail="Could not find details for this user")

    detail = "Could not find details for this user"
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT message FROM users WHERE hash=?", (user,))
        data = cursor.fetchall()
        if len(data) >= 1:
            detail = f"Message: {data[0][0]}"

    return render_template("details.html", detail=detail)


if __name__ == "__main__":
    app.run()
