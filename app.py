from flask import Flask
from configparser import ConfigParser
import json
from app import app, db, User
from app.models import User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.debug = True
config=ConfigParser()
config.read('./config.ini')
 
hostname = config.get('config','hostname')
username = config.get('config','username')
database = config.get('config','database')
password = config.get('config','password')

conn = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname:port/database'
db = SQLAlchemy(app)

def getUsers( ) :
    answer = []
    cur = conn.cursor()

    cur.execute( "SELECT idUser, email, password FROM user" )

    for idUser, email, password in cur.fetchall() :
       answer.append("ID: " + idUser + " Email: " + email + " Password: " + password)
    return json.dumps(answer)

def insertUser(User):
    cur = conn.cursor()
    id = cur.fetchone()
    
    if(id == 'NULL'):
       print ("User db is empty")
       id = 1
    
    answer = "ID: " + str(id) + " Email: " + email + " Password: " + password
    print (answer)

    # REMIND TO ADD USERNAME ATTRIBUTE TO USER DB
    cur.execute('''INSERT INTO user (id,email,password) VALUES (%s,%s,%s)''', (int(id),email,password))
    conn.commit()

    return answer

@app.route("/user")
def users_endpoint():
    answer=getUsers( )
    return answer

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


@app.route("/addUser")
def addUser_endpoint():
    # int idUser, email, password
    u = User(id='1', email='admin@example.com', password='admin')    
    insertUser(u)
    return answer
 
if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=5000)

