from flask import render_template, flash, redirect, url_for, request, json
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProjectForm, SprintForm, User_StoriesForm, DodForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Team, Sprint, User_Stories, Role
from werkzeug.urls import url_parse
import datetime


def get_role(user_id):
    role_title = db.engine.execute('select role.title from role '
                                   'join role_user_table on (role_user_table.role_id = role.role_id) '
                                   'join user on (role_user_table.user_id = user.user_id)'
                                   'where user.user_id = ' + user_id)

    role = []
    for r in role_title:
        role.append(r[0])
    try:
        return role[0]
    except IndexError:
        return 0


def get_team_id(team_id):
    team_id = db.engine.execute("select team_id from team where team.team_id = " + team_id)
    t_id = []
    for id in team_id:
        t_id.append(id[0])

    return t_id[0]


def get_team_name(team_id):
    team_name = db.engine.execute("select team_name from team where team_id = " + team_id)
    name = []
    for n in team_name:
        name.append(n[0])

    return name[0]


def get_dod(project_id):
    dod = db.engine.execute("select Dod from project where project_id = " + project_id)
    name = []
    for n in dod:
        n.append(n[0])

    return n[0]


def currentSprintNum(project_id: int):
    curr = db.engine.execute(
        "Select sprint.sprint_num from sprint "
        " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        " join project on (project_sprint_table.project_id = project.project_id)"
        " where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    try:
        return str(currSprint[0])
    except IndexError:
        return 0


def currentSprint(project_id: int):
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint "
        "join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []

    for sprint in curr:
        currSprint.append(sprint[0])
    try:
        return str(currSprint[0])
    except IndexError:
        return None


def get_proj_name(project_id: int):
    proj_name = db.engine.execute("select project.proj_name from project where project.project_id = " + project_id)

    pname = []
    for name in proj_name:
        pname.append(name[0])
    return str(pname[0])


def get_title(id: int):
    user_story_title = db.engine.execute("select title from user_stories where user_stories.user_stories_id = " + id)

    title = []
    for t in user_story_title:
        title.append(t[0])
    return str(title[0])


def get_difficulty(id: int):
    diff = db.engine.execute("select difficulty from user_stories where user_stories.user_stories_id = " + id)

    difficulty = []
    for d in diff:
        difficulty.append(d[0])
    return str(difficulty[0])


def get_description(id: int):
    descrip = db.engine.execute("select description from user_stories where user_stories.user_stories_id = " + id)

    description = []
    for desc in descrip:
        description.append(desc[0])
    return str(description[0])


def get_acceptance_criteria(id: int):
    accept = db.engine.execute(
        "select acceptance_criteria from user_stories where user_stories.user_stories_id = " + id)

    acceptance = []
    for acc in accept:
        acceptance.append(acc[0])
    return str(acceptance[0])


def get_username(user_id):
    username = db.engine.execute("select username from user where user.user_id = " + user_id)

    name = []
    for user in username:
        name.append(user[0])

    return name[0]


def get_email(user_id):
    email = db.engine.execute("select email from user where user.user_id = " + user_id)

    user_email = []
    for e in email:
        user_email.append(e[0])

    return user_email[0]


@app.route('/PBI/<user_stories_id>', methods=['GET', 'POST'])
def PBI(user_stories_id: int):
    project_id = str(db.engine.execute("Select project_id from user_stories_project_table "
                                       " where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    sprint_id = str(db.engine.execute("Select sprint_id from user_stories_sprint_table "
                                      " where user_stories_spint_table.user_stories_id ='" + user_stories_id + "'").scalar())

    curr = db.engine.execute("Select sprint.sprint_id from sprint "
                             " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
                             " join project on (project_sprint_table.project_id = project.project_id)"
                             " where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='PBI' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute("insert into user_stories_sprint_table (sprint_id, user_stories_id) values ('" + str(
        sprint[0] + "', '" + user_stories_id + "')"))
    # db.session.add(stmt)
    # db.session.commit()
    return redirect(url_for('Sprint', sprint_id=sprint_id))


@app.route('/To_do/<user_stories_id>', methods=['GET', 'POST'])
def To_do(user_stories_id: int):
    sprint_id = str(db.engine.execute(
        "Select sprint_id from user_stories_sprint_table where user_stories_spint_table.user_stories_id ='" + user_stories_id + "'").scalar())
    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute("Select sprint.sprint_id from sprint "
                             " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id) "
                             "join project on (project_sprint_table.project_id = project.project_id)"
                             "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='To do' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute("insert into user_stories_sprint_table (sprint_id, user_stories_id) values ('" + str(
        sprint[0]) + "', '" + user_stories_id + "')")
    # db.session.add(stmt)
    # db.session.commit()
    return redirect(url_for('Sprint', sprint_id=sprint_id))


@app.route('/In_p/<user_stories_id>', methods=['GET', 'POST'])
def In_p(user_stories_id: int):
    sprint_id = str(db.engine.execute("Select sprint_id from user_stories_sprint_table "
                                      " where user_stories_spint_table.user_stories_id ='" + user_stories_id + "'").scalar())

    project_id = str(db.engine.execute("Select project_id from user_stories_project_table "
                                       " where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())

    curr = db.engine.execute("Select sprint.sprint_id from sprint "
                             " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
                             " join project on (project_sprint_table.project_id = project.project_id)"
                             " where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    db.engine.execute("UPDATE project SET Status='In Progress' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute("insert into user_stories_sprint_table (sprint_id, user_stories_id) values ('" + str(
        sprint[0]) + "', '" + user_stories_id + "')")
    # db.session.add(stmt)
    # db.session.commit()
    return redirect(url_for('Sprint', sprint_id=sprint_id))


@app.route('/Done/<user_stories_id>', methods=['GET', 'POST'])
def Done(user_stories_id: int):
    sprint_id = str(db.engine.execute(
        "Select sprint_id from user_stories_sprint_table where user_stories_spint_table.user_stories_id ='" + user_stories_id + "'").scalar())
    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='Done' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute("insert into user_stories_sprint_table (sprint_id, user_stories_id) values ('" + str(
        sprint[0]) + "', '" + user_stories_id + "')")
    # db.session.add(stmt)
    # db.session.commit()
    return redirect(url_for('Sprint', sprint_id=sprint_id))


@app.route('/Card/<user_stories_id>', methods=['GET', 'POST'])
def card(user_stories_id: int):
    return render_template('Card.html', title="card", get_title=get_title,
                           get_difficulty=get_difficulty, get_description=get_description,
                           get_acceptance_criteria=get_acceptance_criteria, user_stories_id=user_stories_id)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    proj_ids = db.engine.execute("select project.project_id from project join team_project_table on"
                                 " (project.project_id = team_project_table.project_id) join team on"
                                 " (team_project_table.team_id = team.team_id) join team_user_table on"
                                 " (team.team_id = team_user_table.team_id) where team_user_table.user_id = " + current_user.get_id())

    project_ids = []
    for pid in proj_ids:
        project_ids.append(pid[0])
    return render_template('index.html', title='Home', project_ids=project_ids, get_proj_name=get_proj_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


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
        # only accept alphanumeric characters for username
        if form.username.data.isalnum() is True:

            user = User(username=form.username.data, email=form.email.data)

            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        else:
            flash('Please use alphanumeric characters for username.')
    return render_template('register.html', title='Register', form=form)


@app.route('/project/<project_id>', methods=['GET', 'POST'])
@login_required
def project_endpoint(project_id):
    form = DodForm()
    if form.validate():
        Dod = str(form.Dod.data)
        db.engine.execute("UPDATE project SET Dod= \"Check\" WHERE project_id= 1")
        flash("Definition of done added")
        return redirect(url_for('index'))

    sprints_num = db.engine.execute("select sprint_num from sprint "
                                    "join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id) "
                                    "join project on (project_sprint_table.project_id = project.project_id) "
                                    " where project.project_id = '" + project_id + "'")
    sprints_num2 = db.engine.execute("select sprint_num from sprint join project_sprint_table on "
                                     " (sprint.sprint_id = project_sprint_table.sprint_id) join project on "
                                     " (project_sprint_table.project_id = project.project_id) "
                                     " where project.project_id = '" + project_id + "'")
    big = db.engine.execute("select SUM(difficulty) from user_stories "
                            " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                            " join sprint on (user_stories_sprint_table.sprint_id = sprint.sprint_id) "
                            " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id) "
                            " join project on (project_sprint_table.project_id = project.project_id) "
                            " where project.project_id = '" + project_id + "'").scalar()

    completeDiff = []
    totalDiff = []
    sprints = []

    for num in sprints_num:
        sprints.append(num[0])

    total = 0
    for num in sprints:
        little = db.engine.execute("select SUM(difficulty) from user_stories "
                                   " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                   " join sprint on (user_stories_sprint_table.sprint_id = sprint.sprint_id) "
                                   " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id) "
                                   " join project on (project_sprint_table.project_id = project.project_id) "
                                   " where project.project_id = '" + project_id + "' and sprint.sprint_num = '"
                                   + str(num) + "'").scalar()
        # try:
        #   return str(currSprint[0])
        # except IndexError:
        #   return None
        total = total + int(little)
        completeDiff.append(total)

    for num in sprints_num2:
        totalDiff.append(int(big))

    # totalDiff = [50, 65, 80, 70]
    # completeDiff = [0, 20, 33, 55]
    # sprints = [1, 2, 3, 4]
    return render_template('project.html', title="Project page", get_proj_name=get_proj_name,
                           currentSprint=currentSprint, project_id=project_id,
                           sprints=sprints, totalDiff=totalDiff, completeDiff=completeDiff, form=form, get_dod=get_dod)


@app.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    teams = db.engine.execute('select team_name from team '
                              ' join team_user_table on (team.team_id = team_user_table.team_id)'
                              ' where team_user_table.user_id = ' + current_user.get_id())
    team_names = []
    for name in teams:
        team_names.append(name[0])

    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(proj_name=form.proj_name.data, total_diff=0)
        team = Team(team_name=form.team_name.data)

        db.session.add(project)
        db.session.add(team)
        team.projteams.append(project)
        team.userteams.append(current_user)
        db.session.commit()
        flash('Congratulations, you made a project!')
        return redirect(url_for('index'))
    return render_template('CreateProjectNew.html', title='Create Project', form=form, team_names=team_names)


@app.route('/delete_project/<project_id>')
@login_required
def delete_project(project_id):
    if current_user.is_authenticated:
        project = Project.query.filter_by(project_id=project_id).first()

        if not project:
            flash('Project not found!')

        db.session.delete(project)
        db.session.commit()
        flash('Project successfully deleted!')
        return redirect(url_for('index'))


@app.route('/create_sprint/<project_id>', methods=['GET', 'POST'])
@login_required
def create_sprint(project_id):
    next_sprint = int(currentSprintNum(project_id)) + 1
    form = SprintForm()
    if form.validate():
        sprint = Sprint(start_date=form.start_date.data, end_date=form.end_date.data, sprint_num=next_sprint)
        project = Project.query.filter_by(project_id=project_id).first()
        db.session.add(sprint)
        sprint.projects.append(project)
        db.session.commit()
        flash('Congratulations, you made a sprint!')
        return redirect(url_for('sprint_endpoint', sprint_id=next_sprint))
    return render_template('CreateSprint.html', title='Create Sprint', form=form, project_id=project_id)


@app.route('/delete_card')  # Pop up with warning and confirmation
def delete_card(user_stories_id):
    db.engine.execute("delete * from user_stories where user_stories.user_stories_id = " + user_stories_id)
    db.engine.execute(
        "delete * from user_stories_sprint_table where user_stories_sprint_table.user_stories_id = " + user_stories_id)
    db.engine.execute(
        "delete * from user_user_stories_table where user_user_stories_table.user_stories_id = " + user_stories_id)
    db.engine.execute("delete * from to_do where to_do.user_stories_id = " + user_stories_id)
    db.engine.execute("delete * from works_on where works_on.user_stories_id = " + user_stories_id)
    db.engine.execute("delete * from requirements where requirements.user_stories_id = " + user_stories_id)


@app.route('/team/<project_id>')
@login_required
def team_endpoint(project_id):
    members = db.engine.execute("select user.user_id from user "
                                " join team_user_table on (user.user_id = team_user_table.user_id) "
                                " join team on (team_user_table.team_id = team.team_id) "
                                " join team_project_table on (team.team_id = team_project_table.team_id) "
                                " join project on (team_project_table.project_id = project.project_id) "
                                " where project.project_id = " + project_id)

    team_ids = db.engine.execute("select team.team_id from team "
                                 " join team_user_table on (team.team_id = team_user_table.team_id) "
                                 " join user on (team_user_table.user_id = user.user_id) "
                                 " join team_project_table on (team_project_table.team_id = team.team_id) "
                                 " join project on (team_project_table.project_id = project.project_id) "
                                 " where project.project_id = " + project_id)

    # role_ids = db.engine.execute("select role.role_id from role "
    #                             "join role_user_table on (role.role_id = role_user_table.role_id) "
    #                             "join user on (role_user_table.user_id = user.user_id)")

    member_ids = []
    for id in members:
        member_ids.append(id[0])

    t_id = []
    for id in team_ids:
        t_id.append(id[0])

    return render_template('team.html', title="Team", member_ids=member_ids, get_username=get_username,
                           get_email=get_email, t_id=t_id, get_team_name=get_team_name, get_role=get_role)


@app.route('/sprint_manage/<project_id>')
@login_required
def sprint_manage_endpoint(project_id):
    sprints = db.engine.execute("select sprint_id from project_sprint_table "
                                " where project_sprint_table.project_id = " + project_id)
    # may have to use an order by start date to get them in the proper order

    sprint_ids = []
    for sprint in sprints:
        sprint_ids.append(sprint[0])

    pb = db.engine.execute("select user_stories_id from user_stories_project_table "
                           " where user_stories_project_table.project_id = " + project_id)

    prod_back_ids = []
    for prod_back in pb:
        prod_back_ids.append(prod_back[0])

    return render_template('sprintManagement.html', title="Sprint Management", get_sprint_num=get_sprint_num,
                           sprint_ids=sprint_ids, prod_back_ids=prod_back_ids, get_title=get_title,
                           get_difficulty=get_difficulty, get_description=get_description,
                           get_acceptance_criteria=get_acceptance_criteria, project_id=project_id)


def get_sprint_num(sprint_id):
    sprint_num = db.engine.execute("select sprint_num from sprint where sprint_id = " + sprint_id)

    sprint = []
    for s in sprint_num:
        sprint.append(s[0])

    return sprint[0]


@app.route('/sprint/<sprint_id>')
@login_required
def sprint_endpoint(sprint_id):
    '''
    if sprint_id is None:
        project_id = db.engine.execute("select project.project_id from project join team_project_table on"
                             " (project.project_id = team_project_table.project_id) join team on"
                             " (team_project_table.team_id = team.team_id) join team_user_table on"
                             " (team.team_id = team_user_table.team_id) where team_user_table.user_id = " + current_user.get_id())


        return(redirect(url_for('create_sprint', project_id = project_id))
    '''

    project_id = str(
        db.engine.execute("select project_id from project_sprint_table where sprint_id ='" + sprint_id + "'").scalar())

    todo_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                " where user_stories_sprint_table.sprint_id = " + sprint_id +
                                " and user_stories.status = 'To do'")

    todo = []
    for user_story in todo_us:
        todo.append(user_story[0])

    inprogress_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                      " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                      " where user_stories_sprint_table.sprint_id = " + sprint_id +
                                      " and user_stories.status = 'In Progress'")

    in_progress = []
    for ip_us in inprogress_us:
        in_progress.append(ip_us[0])

    done_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                " where user_stories_sprint_table.sprint_id = " + sprint_id +
                                " and user_stories.status = 'Done'")

    done = []
    for dn_us in done_us:
        done.append(dn_us[0])

    pb = db.engine.execute("select user_stories.user_stories_id from user_stories "
                           " join user_stories_project_table on (user_stories_project_table.user_stories_id = user_stories.user_stories_id)"
                           " where user_stories_project_table.project_id ='" + project_id +
                           "' and user_stories.status = 'PBI'")

    prod_back_ids = []
    for prod_back in pb:
        prod_back_ids.append(prod_back[0])
    return render_template('Sprint.html', title="Sprint Page", project_id=project_id, todo=todo, inprogress=in_progress,
                           done=done, prod_back_ids=prod_back_ids, get_title=get_title, get_difficulty=get_difficulty,
                           get_description=get_description, get_acceptance_criteria=get_acceptance_criteria)


@app.route('/create_card/<project_id>', methods=['GET', 'POST'])
@login_required
def create_card(project_id):
    form = User_StoriesForm()
    if form.validate():
        user_stories = User_Stories(Difficulty=form.difficulty.data, Acceptance_criteria=form.acceptance_criteria.data,
                                    title=form.title.data, Status="PBI")
        project = Project.query.filter_by(project_id=project_id).first()
        db.session.add(user_stories)
        user_stories.projects.append(project)
        db.session.commit()
        flash('Congratulations, you made a User Story!')
        return redirect(url_for('sprint_manage_endpoint', project_id=project_id))
    return render_template('CreateUserStory.html', title='Create User Story', form=form, project_id=project_id)


@app.route('/assign_role/<team_id>/<project_id>/<user_id>/<role_id>')
@login_required
def assign_role(team_id, project_id, user_id, role_id):
    role = Role.query.filter_by(role_id=role_id).first()
    user = User.query.filter_by(user_id=user_id).first()
    team = Team.query.filter_by(team_id=team_id).first()
    # Rename title to role_title in db to eliminate conflict with title keyword in python?
    if not role:
        flash('Role not found!')
    # FUNCTIONAL BUT ROLES CAN BE DUPLICATED FIX IF CAN OR SET ROLE BY THE MOST CURRENT COMMIT?
    elif role is not None:
        user.role.append(role)
        db.session.commit()
        # user.teams.append(team)
        # db.session.commit()

    # Make role.html to render the data onto page
    return redirect(url_for('team_endpoint', project_id=project_id))  # Title conflicts with title for html?
