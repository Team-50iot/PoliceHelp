import mysql.connector
from flask import Flask,jsonify,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='Our_WebSite')


user, password = '1pavel1', 'ppm021999'
host = '1pavel1.mysql.pythonanywhere-services.com'
db = '1pavel1$PoliceHelp' # dbFlask was created as a PythonAnywhere MySQL database

# connection string: mysql://user:pword@host/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}/{3}'.format(user, password, host, db)
db = SQLAlchemy(app)



'''SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{1pavel1}:{ppm021999}@{1pavel1.mysql.pythonanywhere-services.com}/{PoliceHelp}".format(
    username="1pavel1",
    password="ppm021999",
    hostname="1pavel1.mysql.pythonanywhere-services.com",
    databasename="PoliceHelp",

)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


conn = SQLAlchemy(app)'''

'''conn = mysql.connector.connect(user="1pavel1",
                               password="ppm021999",
                               host="1pavel1.mysql.pythonanywhere-services.com",
                               database="1pavel1$PoliceHelp")'''





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
    script = """SELECT  id , time  , number from info"""
    cursor = db.cursor()

    cursor.execute(script)
    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
