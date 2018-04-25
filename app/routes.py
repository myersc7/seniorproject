from flask import render_template, flash, redirect, url_for, request, json
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProjectForm, SprintForm, User_StoriesForm, DodForm, AddMemberForm
from app.forms import RetroForm, ReviewForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Team, Sprint, User_Stories, Role
from werkzeug.urls import url_parse
import datetime

def get_review(sprint_id):
    review = db.engine.execute("select Review from sprint where sprint_id = " + sprint_id)
    name = []
    for n in review:
        name.append(n[0])

    return name[0]

def get_retro(project_id):
    retro = db.engine.execute("select Retro from sprint where sprint_id = " + sprint_id)
    name = []
    for n in retro:
        name.append(n[0])

    return name[0]

def get_sprint_id(user_stories_id):
    sprint_id = db.engine.execute(
        "Select sprint_id from user_stories_sprint_table where user_stories_id ='" + user_stories_id + "'")
    name = []
    for n in sprint_id:
        name.append(n[0])

    try:
        return name[0]
    except IndexError:
        return 'None'

def get_role(user_id, team_id):
    role_title = db.engine.execute('select role.title from role '
                                   'join team_user_table on (team_user_table.role_id = role.role_id) '
                                   'where team_user_table.user_id = ' + user_id + " and team_user_table.team_id =" + team_id)

    role = []
    for r in role_title:
        role.append(r[0])
    try:
        return role[0]
    except IndexError:
        return 'None'


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
        name.append(n[0])

    return str(name[0])


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
    if not currSprint:
        return ('/create_sprint/' + project_id)
    else:
        return ('/sprint/' + str(currSprint[0]))


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
    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])

    sprint_id = get_sprint_id(user_stories_id)
    if str(sprint_id) == 'None':
        sprint_id = str(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='PBI' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute("UPDATE user_stories_sprint_table SET sprint_id = NULL WHERE user_stories_id= '" + str(user_stories_id) + "'")
    #db.engine.execute("insert into user_stories_sprint_table (sprint_id, user_stories_id) values ('" + str(sprint[0] + "', '" + user_stories_id + "')"))
    #db.session.add(stmt)
    #db.session.commit()
    return redirect(url_for('sprint_endpoint', sprint_id=sprint_id))


@app.route('/To_do/<user_stories_id>', methods=['GET', 'POST'])
def To_do(user_stories_id: int):

    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])

    sprint_id = get_sprint_id(user_stories_id)
    if str(sprint_id) == 'None':
        sprint_id = str(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='To do' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute(
        "UPDATE user_stories_sprint_table SET sprint_id = '" + str(sprint_id) + "' WHERE user_stories_id= '" + str(user_stories_id) + "'")
    #db.session.add(stmt)
    #db.session.commit()
    return redirect(url_for('sprint_endpoint', sprint_id=sprint_id))


@app.route('/In_p/<user_stories_id>', methods=['GET', 'POST'])
def In_p(user_stories_id: int):
    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    sprint_id = get_sprint_id(user_stories_id)
    if str(sprint_id) == 'None':
        sprint_id = str(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='In Progress' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute(
        "UPDATE user_stories_sprint_table SET sprint_id = '" + str(sprint_id) + "' WHERE user_stories_id= '" + str(user_stories_id) + "'")
    #db.session.add(stmt)
    #db.session.commit()
    return redirect(url_for('sprint_endpoint', sprint_id=sprint_id))


@app.route('/Done/<user_stories_id>', methods=['GET', 'POST'])
def Done(user_stories_id: int):
    project_id = str(db.engine.execute(
        "Select project_id from user_stories_project_table where user_stories_project_table.user_stories_id ='" + user_stories_id + "'").scalar())
    curr = db.engine.execute(
        "Select sprint.sprint_id from sprint join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
        "join project on (project_sprint_table.project_id = project.project_id)"
        "where project.project_id = '" + project_id + "' ORDER BY Sprint_num DESC LIMIT 1")

    currSprint = []
    for sprint in curr:
        currSprint.append(sprint[0])
    sprint_id = get_sprint_id(user_stories_id)
    if str(sprint_id) == 'None':
        sprint_id = str(sprint[0])
    db.engine.execute("UPDATE user_stories SET Status='Done' WHERE user_stories_id= '" + user_stories_id + "'")
    db.engine.execute(
        "UPDATE user_stories_sprint_table SET sprint_id = '" + str(sprint_id) + "' WHERE user_stories_id= '" + str(user_stories_id) + "'")
    #db.session.add(stmt)
    #db.session.commit()
    return redirect(url_for('sprint_endpoint', sprint_id= sprint_id))


@app.route('/Card/<user_stories_id>', methods=['GET', 'POST'])
def card(user_stories_id):
    card = User_Stories.query.get(user_stories_id)
    form = User_StoriesForm(obj=card)
    if form.validate_on_submit():
        form.populate_obj(card)
        title = str(form.title.data)
        difficulty = str(form.Difficulty.data)
        description = str(form.Description.data)
        acc_crit = str(form.Acceptance_criteria.data)
        db.engine.execute("UPDATE user_stories SET title= \"" + title + "\" , Difficulty = \"" + difficulty + "\" , Description = \""
        + description + "\" , Acceptance_criteria = \"" + acc_crit + "\" WHERE user_stories_id= '" + user_stories_id + "'")
        return redirect(url_for("card", user_stories_id=user_stories_id))
    return render_template('Card.html', title="card", form = form, user_stories_id=user_stories_id, delete_card=delete_card)


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
    old_dod = Project.query.get(project_id)
    form = DodForm(obj = old_dod)
    if form.validate():
        form.populate_obj(old_dod)
        Dod = str(form.Dod.data)
        db.engine.execute("UPDATE project SET Dod= \"" + Dod + "\" WHERE project_id= '" + project_id +"'")
        flash("Definition of done added")
        return redirect(url_for('project_endpoint', project_id=project_id))
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
                                   + str(num) + "' and status = 'Done'").scalar()
        try:
            total = total + int(little)
        except TypeError:
            total = total
        completeDiff.append(total)

    for num in sprints_num2:
        try:
            totalDiff.append(int(big))
        except TypeError:
            totalDiff.append(0)

    # totalDiff = [50, 65, 80, 70]
    # completeDiff = [0, 20, 33, 55]
    # sprints = [1, 2, 3, 4]
    return render_template('project.html', title="Project page", get_proj_name=get_proj_name,
                           currentSprint=currentSprint, project_id=project_id,
                           sprints=sprints, totalDiff=totalDiff, completeDiff=completeDiff, form=form, get_dod=get_dod,
                           edit_githublink=edit_githublink)


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
        next_sprint_id = str(db.engine.execute("select sprint.sprint_id from sprint "
                                  " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
                                  " where sprint.sprint_num = '" + str(next_sprint) +
                                  "' and project_sprint_table.project_id ='" + str(project_id) + "'").scalar())
        flash('Congratulations, you made a sprint!')
        return redirect(url_for('sprint_endpoint', sprint_id=str(next_sprint_id)))
    next_sprint_id = str(db.engine.execute("select sprint.sprint_id from sprint "
                                           " join project_sprint_table on (sprint.sprint_id = project_sprint_table.sprint_id)"
                                           " where sprint.sprint_num = '" + str(next_sprint) +
                                           "' and project_sprint_table.project_id ='" + str(project_id) + "'"))
    return render_template('CreateSprint.html', title='Create Sprint', form=form, project_id=project_id, sprint_id=next_sprint_id)


@app.route('/delete_card/<user_stories_id>')  # Pop up with warning and confirmation
def delete_card(user_stories_id):
    project_id = str(db.engine.execute("select project_id from user_stories_project_table "
                      " where user_stories_id = '" + user_stories_id + "'").scalar())
    status = str(db.engine.execute("select status from user_stories where user_stories_id ='" + user_stories_id + "'"))
    if status != 'PBI':
        db.engine.execute(
            "delete from user_stories_sprint_table where user_stories_id= '" + user_stories_id + "'")

    db.engine.execute("delete from user_stories_project_table WHERE user_stories_id= '" + user_stories_id + "'")

    user_stories = User_Stories.query.filter_by(user_stories_id=user_stories_id).first()

    if not user_stories:
        flash('User Story not found!')

    db.session.delete(user_stories)
    db.session.commit()
    flash('User Story successfully deleted!')
    return redirect(url_for('sprint_manage_endpoint', project_id=project_id))

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
                           get_email=get_email, t_id=t_id, get_team_name=get_team_name, get_role=get_role,
                           project_id=project_id, get_role_id=get_role_id)
  

@app.route('/addmember/<project_id>',  methods=['GET', 'POST'])
@login_required
def add_member(project_id):
    form = AddMemberForm()
    t_id = db.engine.execute("select team_id from team_project_table where project_id = "+project_id)
    team_id = []
    for t in t_id:
        team_id.append(str(t[0]))

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        u_id = db.engine.execute("select user_id from user where username = '"+username+"' and email = '"+email+"'")
        user_id = []
        for u in u_id:
            user_id.append(str(u[0]))
        if not user_id:
            flash('User not found!')
        else:
            u_name = db.engine.execute("select team_user_table_id from team_user_table where team_id = "+team_id[0]+" and user_id = "+user_id[0])
            usernames = []
            for name in u_name:
                usernames.append(name[0])
            if not usernames:
                db.engine.execute("insert into team_user_table (user_id, team_id) values ("+user_id[0]+", "+team_id[0]+")")
                flash('Congratulations, you added a member!')
                return redirect('/team/' + project_id)
            else:
                flash(username+' is already a member of the team')

    return render_template('AddMember.html', title='Add Member', form=form)



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
def sprint_endpoint(sprint_id, methods=['GET', 'POST']):
    '''
    if sprint_id is None:
        project_id = db.engine.execute("select project.project_id from project join team_project_table on"
                             " (project.project_id = team_project_table.project_id) join team on"
                             " (team_project_table.team_id = team.team_id) join team_user_table on"
                             " (team.team_id = team_user_table.team_id) where team_user_table.user_id = " + current_user.get_id())


        return(redirect(url_for('create_sprint', project_id = project_id))
    '''
    old_retro = Sprint.query.get(sprint_id)
    sprintretro = RetroForm(obj=old_retro)
    if sprintretro.validate_on_submit():
        sprintretro.populate_obj(old_retro)
        Retro = str(sprintretro.Retro.data)
        db.engine.execute("UPDATE sprint SET Retro= \"" + Retro + "\" WHERE sprint_id= '" + sprint_id + "'")
        flash("Sprint Retrospective added")
        return redirect(url_for('sprint_endpoint', sprint_id=sprint_id))

    old_review = Sprint.query.get(sprint_id)
    sprintreview = ReviewForm(obj=old_review)
    if sprintreview.validate_on_submit():
        sprintreview.populate_obj(old_retro)
        Review = str(sprintreview.Review.data)
        db.engine.execute("UPDATE sprint SET Review= \"" + Review + "\" WHERE sprint_id= '" + sprint_id + "'")
        flash("Sprint Review added")
        return redirect(url_for('sprint_endpoint', sprint_id=sprint_id))

    project_id = str(
        db.engine.execute("select project_id from project_sprint_table where sprint_id ='" + sprint_id + "'").scalar())

    todo_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                " where user_stories_sprint_table.sprint_id = '" + str(sprint_id) +
                                "' and user_stories.status = 'To do'")

    todo = []
    for user_story in todo_us:
        todo.append(user_story[0])

    inprogress_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                      " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                      " where user_stories_sprint_table.sprint_id = '" + sprint_id +
                                      "' and user_stories.status = 'In Progress'")

    in_progress = []
    for ip_us in inprogress_us:
        in_progress.append(ip_us[0])

    done_us = db.engine.execute("select user_stories.user_stories_id from user_stories "
                                " join user_stories_sprint_table on (user_stories.user_stories_id = user_stories_sprint_table.user_stories_id) "
                                " where user_stories_sprint_table.sprint_id = '" + sprint_id +
                                "' and user_stories.status = 'Done'")

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
                           get_description=get_description, get_acceptance_criteria=get_acceptance_criteria,
                           sprintretro=sprintretro, sprintreview=sprintreview)


@app.route('/create_card/<project_id>', methods=['GET', 'POST'])
@login_required
def create_card(project_id):
    form = User_StoriesForm()
    if form.validate():
        user_stories = User_Stories(Difficulty=form.Difficulty.data, Acceptance_criteria=form.Acceptance_criteria.data,
                                    title=form.title.data, Description=form.Description.data, Status="PBI")
        project = Project.query.filter_by(project_id=project_id).first()
        db.session.add(user_stories)
        user_stories.projects.append(project)
        db.session.commit()
        user_stories_id = db.engine.execute("Select user_stories_id from user_stories ORDER BY user_stories_id DESC limit 1").scalar()
        db.engine.execute("insert into user_stories_sprint_table (user_stories_id) values ('" + str(user_stories_id) + "')")
        flash('Congratulations, you made a User Story!')
        return redirect(url_for('sprint_manage_endpoint', project_id=project_id))
    return render_template('CreateUserStory.html', title='Create User Story', form=form, project_id=project_id)


def get_role_id(role_title):
    role = Role.query.filter_by(title=role_title).first()

    try:
        return role.role_id
    except IndexError:
        return 'None'


@app.route('/assign_role/<team_id>/<project_id>/<user_id>/<role_id>', methods=['GET', 'POST'])
@login_required
def assign_role(team_id, project_id, role_id, user_id):
    role = Role.query.filter_by(role_id=role_id).first()

    # Rename title to role_title in db to eliminate conflict with title keyword in python?
    if role is None:
        flash('Role not found!')

    db.engine.execute("update team_user_table set role_id = " + role_id + " where team_id = " + team_id +
                      " and user_id = " + user_id)
    flash('Role assignment successful!')
    # Make role.html to render the data onto page
    return redirect(url_for('team_endpoint', project_id=project_id))  # Title conflicts with title for html?


@app.route('/remove_role/<role_id>/<project_id>/<team_id>/<user_id>', methods=['GET', 'POST'])
@login_required
def remove_role(role_id, project_id, team_id, user_id):
    # Make a role unique so its easier to maintain
    role = Role.query.filter_by(role_id=role_id).first()

    if role is None:
        flash('Role was not found!')
        return redirect(url_for('team_endpoint', project_id=project_id))
    # how to delete an attribute from a table?

    db.engine.execute("update team_user_table set role_id = null where team_id = " + team_id +
                      " and user_id = "+user_id)
    flash('Role successfully removed!')
    return redirect(url_for('team_endpoint', project_id=project_id))


def edit_githublink(project_id, github_link):
    proj = Project.query.filter_by(project_id=project_id).first()

    if not proj:
        flash('Project not found!')

    db.engine.execute("update project set github_link = " + github_link + " where project_id = " + project_id)

    return redirect(url_for('project_endpoint', project_id=project_id))

