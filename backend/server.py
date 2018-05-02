from flask import Flask , jsonify
from DBcm import UseDatabase
import mysql.connector
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
app = Flask(__name__)


conn = mysql.connector.connect(user="root",
                               password="11111111",
                               host="localhost",

                               database="mydb")


@app.route('/', methods=['GET'])
def home():
    script = """SELECT  id , time  , number from data"""
    cursor = conn.cursor()

    cursor.execute(script)
    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)




if __name__ == '__main__':
    app.run(debug=True)
