import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="Flask@123",
        database="flaskdb"
    )

@app.route("/")
def register():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    fullname = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (fullname, email, phone, username, password)
        VALUES (%s, %s, %s, %s, %s)
    """, (fullname, email, phone, username, password))

    conn.commit()

    cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("success.html", user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)