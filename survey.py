import smtplib
import imaplib
import poplib
import time
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    # The following variables are getting info from the submitted form
    # Saving them so that it can use that info when submitting the SQL statement
    pname = request.form["pname"]
    email = request.form["email"]
    uniform = request.form["uniform"]
    patches = request.form["patches"]

    return render_template("submitted_index.html")


# This is a thing for python that makes it so that if someone calls on this file as a library
# then they can get the functions without actually running the program (if you have questions text me)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)