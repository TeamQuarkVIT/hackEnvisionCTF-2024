import sqlite3
from contextlib import closing

from flask import Flask, render_template, request

app = Flask(
    __name__, static_url_path="/", static_folder="web/static", template_folder="web/template"
)
conn = sqlite3.connect("database.db", check_same_thread=False)


def is_invalid_query(query: str) -> bool:
    if query.lower().count("insert") > 1:
        return True

    if "drop" in query.lower():
        return True

    if "delete" in query.lower():
        return True

    return False


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("sqli_chal.html")

    if "username" not in request.form or "password" not in request.form:
        return "Error: Invalid POST parameters passed to endpoint."

    username = request.form["username"]
    password = request.form["password"]

    query = 'SELECT * FROM users WHERE username="{}" AND password="{}"'.format(username, password)
    if is_invalid_query(query):
        return "Error: Woah, that's unexpected..."

    with closing(conn.cursor()) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

        if len(data) < 1:
            return "Error: Username entered not found in database."

        output = "Username details found in database:</br>"
        for row in data:
            output += row[0] + " | " + row[1] + "</br>"

        return output


if __name__ == "__main__":
    app.run()

