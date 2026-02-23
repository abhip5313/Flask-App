from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = {
        "fullname": request.form.get("fullname"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "username": request.form.get("username"),
        "password": request.form.get("password"),
    }
    return render_template("success.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
