import jwt, datetime
from flask import render_template, flash, redirect, url_for, request , jsonify, make_response
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProjectForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Team#, team_user_table, team_project_table
from werkzeug.urls import url_parse
from werkzeug.security import check_password_hash
from functools import wraps

# decorator for tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(user_id=data['user_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    pids = db.engine.execute("select project.project_id from project join team_project_table on"
                             " (project.project_id = team_project_table.project_id) join team on"
                             " (team_project_table.team_id = team.team_id) join team_user_table on"
                             " (team.team_id = team_user_table.team_id) where team_user_table.user_id = " + current_user.get_id())

    project_ids = []
    for pid in pids:
        project_ids.append(pid[0])
    return render_template('index.html', title='Home', project_ids=project_ids, getProjName=getProjName)

def getProjName(project_id :int):
    projName = db.engine.execute("select project.ProjName from project where project.project_id = "+project_id)

    pname = []
    for name in projName:
        pname.append(name[0])
    return str(pname[0])

'''
@app.route('/')
@app.route('/index')
@login_required
def index():
    project_ids = db.engine.execute("select project.project_id from project join team_project_table on"
                             " (project.project_id = team_project_table.project_id) join team on"
                             " (team_project_table.team_id = team.team_id) join team_user_table on"
                             " (team.team_id = team_user_table.team_id) where team_user_table.user_id = " + current_user.get_id())

    proj_ids = []

    for pid in project_ids:
        proj_ids.append(pid[0])
     
    return render_template('index.html', title='Home', proj_ids=proj_ids)

# uses the project id to get the project title
def getProjName(projectid:int):
    projectName = deb.engine.execute("select ProjName from project where project.project_id = "+projectid)

    return str(projectName)
'''
@app.route('/user/<user_id>', methods=['GET'])
@token_required
def get_user(current_user, user_id):

    if int(current_user.user_id) != int(user_id):
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(user_id = user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {}
    user_data['user_id'] = user.user_id
    user_data['email'] = user.email

    return jsonify({'user': user_data})

@app.route('/login2')
def login2():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password_hash, auth.password):
        token = jwt.encode(
            {'user_id': user.user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        token_string = jsonify({'token': token.decode('UTF-8')})
        return render_template('index.html', title='Home', token_string=token_string)

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))# try redirect to '/user/'+str(User.query.get(iduser))'
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')# try redirect to '/user/'+str(User.query.get(iduser))'
        return redirect(next_page)

    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
@login_required
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

@app.route('/project/<project_id>')
@login_required
def project_endpoint(project_id):

    sprints_num = db.engine.execute("select Sprint_num from sprint join project_sprint_table on"
                                 " (sprint.sprint_id = project_sprint_table.sprint_id) join project on"
                                 " (project_sprint_table.project_id = project.project_id)"
                                 "where project.project_id = '" + project_id + "'")
    sprints_num2 = db.engine.execute("select Sprint_num from sprint join project_sprint_table on"
                                 " (sprint.sprint_id = project_sprint_table.sprint_id) join project on"
                                 " (project_sprint_table.project_id = project.project_id)"
                                 "where project.project_id = '" + project_id + "'")
    big = db.engine.execute("select SUM(Difficulty) from user_stories join user_stories_sprint_table on"
                            " (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) join sprint on"
                            " (user_stories_sprint_table.sprint_id = sprint.sprint_id) join project_sprint_table on"
                            " (sprint.sprint_id = project_sprint_table.sprint_id) join project on"
                            " (project_sprint_table.project_id = project.project_id)"
                            "where project.project_id = '" + project_id + "'").scalar()
    completeDiff = []
    totalDiff = []
    sprints = []
    for num in sprints_num:
        sprints.append(num[0])

    total = 0
    for num in sprints:
        little = db.engine.execute("select SUM(Difficulty) from user_stories join user_stories_sprint_table on"
                                   " (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) join sprint on"
                                   " (user_stories_sprint_table.sprint_id = sprint.sprint_id) join project_sprint_table on"
                                   " (sprint.sprint_id = project_sprint_table.sprint_id) join project on"
                                   " (project_sprint_table.project_id = project.project_id)"
                                   "where project.project_id = '" + project_id + "' and sprint.sprint_num = '" + str(num) + "'").scalar()
        total = total + int(little)
        completeDiff.append(total)
    for num in sprints_num2:
        totalDiff.append(int(big))
    #totalDiff = [50, 65, 80, 70]
    #completeDiff = [0, 20, 33, 55]
    #sprints = [1, 2, 3, 4]
    return render_template('project.html', getProjName=getProjName,  project_id=project_id, sprints=sprints, totalDiff=totalDiff, completeDiff=completeDiff)

def getProjName(project_id :int):
    projName = db.engine.execute("select project.proj_name from project where project.project_id = "+project_id)

    pname = []
    for name in projName:
        pname.append(name[0])
    return str(pname[0])


@app.route('/CreateProject', methods=['GET', 'POST'])
@login_required
def CreateProject():
    teams = db.engine.execute('select team_name from team join team_user_table on (team.idteam = team_user_table.idteam) where team_user_table.iduser = '+current_user.get_id())
    team_names = []
    for name in teams:
        team_names.append(name[0])
        

    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(ProjName=form.ProjName.data, total_diff=0)
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


@app.route('/deleteproject/<project_id>', methods=['POST'])
@token_required
def delete_project(current_user, project_id):

    project = Project.query.filter_by(project_id=project_id).first()

    if not project:
        flash('Project not found')

    db.session.delete(project)
    db.session.commit()


    # When deleting a project from the user page, delete traces from
    # project, team_user_table, team_project_table
    
    project = Project.query.filter_by(project_id=project_id, user_id=current_user.get_id).first()
    team = Team.query.all()
    db.session.add(project)
    db.session.add(team)
    team.projteams.append(project)
    team.userteams.append(current_user)
    db.session.commit()
    
    flash('Project successfully deleted!')
        # return render_template('index.html', title='Home', project=project)
    return redirect(url_for('index'))
    
'''
d>, methods=['DELETE'])
@token_required
def delete_project(current_user, project_id):

    project = Project.query.filter_by(project_id=project_id).first()

    if not project:
        return jsonify({'message': 'No project found'})

    db.session.delete(project)
    db.session.commit()

    db.session.commit()
        
    
    flash('Project successfully deleted!')
        # return render_template('index.html', title='Home', project=project)
    return redirect(url_for('index'))
'''

@app.route('/sprintmanage/<project_id>')
@login_required
def sprint_manage_endpoint(project_id):

    sprints = db.engine.execute("select sprint_id from project_sprint_table where project_sprint_table.project_id = "+project_id)
    # may have to use an order by start date to get them in the proper order

    sprintids = []
    for sprint in sprints:
        sprintids.append(sprint[0])

    pb = db.engine.execute("select user_stories_id from user_stories_sprint_table where user_stories_sprint_table.sprint_id in "
                           "(select sprint_id from project_sprint_table where project_sprint_table.project_id = "+project_id+")")

    prodBackIds = []
    for prodback in pb:
        prodBackIds.append(prodback[0])

    return render_template('sprintManagement.html', sprintids=sprintids, prodBackIds=prodBackIds, myfunction=getTitle, getDifficulty=getDifficulty)

@app.route('/sprint/<idsprint>')
@login_required
def sprint_endpoint(idsprint):

    todo_us = db.engine.execute("select user_stories.user_stories_id from user_stories join user_stories_sprint_table on "
                                "(user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                "where user_stories_sprint_table.sprint_id = "+idsprint+" and user_stories.status = 'To Do'")

    todo = []
    for user_story in todo_us:
        todo.append(us[0])

    inprogress_us = db.engine.execute("select user_stories.user_stories_id from user_stories join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) where user_stories_sprint_table.sprint_id = "+idsprint+" and user_stories.status = 'In Progress'")

    inprogress = []
    for ip_us in inprogress_us:
        inprogress.append(ip_us[0])

    done_us = db.engine.execute("select user_stories.user_stories_id from user_stories join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) where user_stories_sprint_table.sprint_id = "+idsprint+" and user_stories.status = 'Done'")

    done = []
    for dn_us in done_us:
        done.append(dn_us[0])

    return render_template('Sprint.html', todo=todo, inprogress=inprogress, done=done)


def getTitle(id:int):
    userstorytitle = db.engine.execute("select title from user_stories where user_stories.user_stories_id = "+id)

    title = []
    for t in userstorytitle:
        title.append(t[0])
    return str(title[0])


def getDifficulty(id:int):
    diff = db.engine.execute("select difficulty from user_stories where user_stories.user_stories_id = " + id)

    difficulty = []
    for d in diff:
        difficulty.append(d[0])
    return str(difficulty[0])



'''
@app.route('/team/<ProjName>')
@login_required
def team_endpoint(ProjName):
  
    members = db.engine.execute("select user.user_id from user join team_user_table on (user.user_id = team_user_table.user_user_id) "
                                "join team on (team_user_table.team_id = team.team_id) join team_project_table on (team.team_id = team_project_table.team_id) "
                                "join project on (team_project_table.project_id = project.project_id) where project.ProjName = '"+ProjName+"'")
  
    usernames = []
    emails = []
    #roles = []
    for userid in members:
        usernames.append((db.engine.execute("select username from user where user_id = '" + userid[0] + "'")#some error in this line or the one beneath it
        emails.append((db.engine.execute("select email from user where user_id = '"+ str(userid[0])+ "'")#was working before I entered these
 
    return render_template('team.html', usernames=usernames, emails=emails)
'''


@app.route('/team/<project_id>')
@login_required
def team_endpoint(project_id):
  
    members = db.engine.execute("select user.user_id from user join team_user_table on (user.user_id = team_user_table.user_id) "
                                "join team on (team_user_table.team_id = team.team_id) join team_project_table on (team.team_id = team_project_table.team_id) "
                                "join project on (team_project_table.project_id = project.project_id) where project.project_id = "+project_id)
  
    member_ids = []
    for id in members:
        member_ids.append(id[0])

    return render_template('team.html', member_ids=member_ids, getUsername=getUsername, getEmail=getEmail)



@app.route('/payload', methods=['POST'])
def payload():
	if request.method == 'POST':
		print(request.json)
		return 'success', 200
	else:
		abort(400)

