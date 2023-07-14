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
    estimated_cost = patches * 4 # We have to do the multiplication in the python file, not the html

    # For the html to know what the variables are, we have to pass them in as arguments when rendering
    # Remember that html does no logic or programming itself, so any logic like what variables are (or math)
    # We need to do in the python file and then render it to the html file
    # So where it says 'pname=pname' for example it is saying:
    # pname(from html file) = pname(from python file) -> This will then go in, find the spot asking to be replaced with pname var and replace it with the value
    return render_template("submitted_index.html", pname=pname, patches=patches, estimated_cost=estimated_cost)


# This is a thing for python that makes it so that if someone calls on this file as a library
# then they can get the functions without actually running the program (if you have questions text me)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)