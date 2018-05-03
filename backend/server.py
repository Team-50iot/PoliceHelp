from DBcm import UseDatabase
import mysql.connector
from flask import Flask, request,jsonify,redirect,render_template


app = Flask(__name__,template_folder='Our_WebSite')


conn = mysql.connector.connect(user="root",
                               password="11111111",
                               host="localhost",

                               database="mydb")





@app.route('/')
def hello() -> '302':
    return  redirect('/index')

@app.route('/index')
def index() -> 'html':
    return render_template('index.html')

@app.route('/blog')
def news() -> 'html':
    return render_template('blog.html')

@app.route('/vkontakte')
def vkontakte() -> 'html':
    return render_template('vkontakte.html')



@app.route('/db', methods=['GET'])
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
    app.run(debug=True, use_reloader=True)
