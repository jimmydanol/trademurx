from flask import Flask
from newtest import *

app = Flask(__name__)

@app.route("/")
def index():
    return "Try entering a serial number at the end of the URL, e.g., trademurx.com/87216818"

@app.route("/<int:serial_num>")
def serial_query(serial_num):
    owner, id = get_query(serial_num)
    return f"Hello, {owner}! I like how you make {id}"
