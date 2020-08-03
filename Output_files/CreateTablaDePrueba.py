
from flask import Flask, escape, request
import Connection
import mysql.connector


app = Flask(__name__)

@app.route('/Insert')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'





