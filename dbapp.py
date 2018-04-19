from flask import Flask
import MySQLdb
import json
import configparser


app = Flask(__name__)
# app.debug = True
config = ConfigParser.ConfigParser()
config.read('./config.ini')

hostname = config.get('config', 'hostname')
username = config.get('config', 'username')
database = config.get('config', 'database')
password = config.get('config', 'password')

conn = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)


def getdepts():
    answer = []
    cur = conn.cursor()

    cur.execute("SELECT dept_name, dept_no FROM departments")

    for dname, dno in cur.fetchall():
        answer.append(dname + " " + dno)
    return json.dumps(answer)


def getmanagers():
    answer = []
    cur = conn.cursor()
    cur.execute(
        "select departments.dept_name, employees.first_name, employees.last_name from departments, dept_manager, employees where departments.dept_no=dept_manager.dept_no and dept_manager.emp_no=employees.emp_no")

    for dname, fname, lname in cur.fetchall():
        answer.append(dname + ": " + fname + " " + lname)
    return json.dumps(answer)


def getdeptmanagers(deptname):
    answer = []
    cur = conn.cursor()
    cur.execute(
        "select departments.dept_name, employees.first_name, employees.last_name from departments, dept_manager, employees where departments.dept_name='%s' and departments.dept_no=dept_manager.dept_no and dept_manager.emp_no=employees.emp_no" % (
            deptname))

    for dname, fname, lname in cur.fetchall():
        answer.append(dname + ": " + fname + " " + lname)
    return json.dumps(answer)


@app.route("/departments")
def depts_endpoint():
    answer = getdepts()
    return answer


@app.route("/managers")
def managers_endpoint():
    answer = getmanagers()
    return answer


@app.route("/managers/<deptname>")
def managersbydept_endpoint(deptname):
    answer = getdeptmanagers(deptname)
    return answer


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=5000)
