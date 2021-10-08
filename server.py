from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    return render_template("read_all.html", all_users = users)

@app.route("/newUser")
def displayForm():
    return render_template("create.html")

@app.route("/AddUser", methods=["POST"])
def addUser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
