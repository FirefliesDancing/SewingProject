import smtplib
import imaplib
import poplib
import time
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "i dont really know"

app.run(host="0.0.0.0", port=80)


# input("Parent Name: ")
# input("Student(s) name(s)")
# input("Prefered email adress: ")
# input("Number of uniforms: ")
# input("Number of patches: ")
# input("Which class does your child attend? ")
# input("What days do your students go to class? ")

