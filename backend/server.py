from flask import Flask
from DBcm import UseDatabase
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(user="root",
                               password="11111111",
                               host="localhost",

                               database="mydb")


@app.route('/', methods=['GET'])
def home():
    script = """SELECt time from data"""
    cursor = conn.cursor()

    cursor.execute(script)
    rv = cursor.fetchone()


    return rv



if __name__ == '__main__':
    app.run(host='192.168.137.154', port=8000,debug=True)
