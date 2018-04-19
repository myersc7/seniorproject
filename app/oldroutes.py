from flask import render_template, flash, redirect, url_for, request , json 
import MySQLdb
from configparser import ConfigParser
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProjectForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Team#, team_user_table, team_project_table
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    projects = db.engine.execute("select ProjName from project join team_project_table on"
                             " (project.idProject = team_project_table.idProject) join team on"
                             " (team_project_table.idteam = team.idteam) join team_user_table on"
                             " (team.idteam = team_user_table.idteam) where team_user_table.iduser = " + current_user.get_id())

    names = []
    for name in projects:
        names.append(name[0])
    return render_template('index.html', title='Home', names=names)


@app.route('/logintest', methods=['GET', 'POST'])
def logintest():
    if current_user.is_authenticated:
        return redirect(url_for('index'))# try redirect to '/user/'+str(USer.query.get(iduser))'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')# try redirect to '/user/'+str(USer.query.get(iduser))'
        return redirect(next_page)
    return render_template('testlogin.html',  title='Sign In', form=form)
	

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))# try redirect to '/user/'+str(USer.query.get(iduser))'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')# try redirect to '/user/'+str(USer.query.get(iduser))'
        return redirect(next_page)
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/project/<ProjName>')
@login_required
def project_endpoint(ProjName):
    sprints = [1, 2, 3, 4]
    totalDiff = [50, 65, 80, 70]
    completeDiff = [0, 20, 33, 55]
    return render_template('project.html', ProjName=ProjName, sprints=sprints, totalDiff=totalDiff, completeDiff=completeDiff)


@app.route('/CreateProject', methods=['GET', 'POST'])
@login_required
def CreateProject():
    teams = db.engine.execute('select team_name from team join team_user_table on (team.idteam = team_user_table.idteam) where team_user_table.iduser = '+current_user.get_id())
    team_names = []
    for name in teams:
        team_names.append(name[0])
        

    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(ProjName=form.ProjName.data, total_diff = 0)
        team = Team(team_name=form.team_name.data)
        db.session.add(project)
        db.session.add(team)
        team.projteams.append(project)
        team.userteams.append(current_user)
        #db.session.add(team_user_tbl)
        #db.session.add(team_project_tbl)
        db.session.commit()
        flash('Congratulations, you made a project!')
       # return render_template('index.html', title='Home', project=project)
        return redirect(url_for('index'))
    return render_template('CreateProject.html', title='Create Project', form=form, team_names=team_names)

'''
@app.route('/team/<ProjName>')
@login_required
def team_endpoint(ProjName):
  
    members = db.engine.execute("select user.iduser from user join team_user_table on (user.iduser = team_user_table.iduser) "
                                "join team on (team_user_table.idteam = team.idteam) join team_project_table on (team.idteam = team_project_table.idteam) "
                                "join project on (team_project_table.idproject = project.idproject) where project.ProjName = '"+ProjName+"'")
  
    #usernames = []
    #emails = []
    #roles = []
    for userid in members:
        usernames.append(str(db.engine.execute("select username from user where iduser = "+userid[0])#some error in this line or the one beneath it
        emails.append(str(db.engine.execute("select email from user where iduser = "+userid[0])#was working before I entered these
   
    return render_template('team.html', usernames=usernames, emails=emails)
'''

'''
@app.route('/payload', methods=['POST'])
def payload():
	if request.method == 'POST':
		print(request.json)
		return 'success', 200
	else:
		abort(400)
   '''