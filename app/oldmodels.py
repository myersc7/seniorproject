from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import synonym, relationship, backref

team_project_table = db.Table('team_project_table',
                db.Column('idProject', db.Integer, db.ForeignKey('project.idproject')),
                db.Column('idteam', db.Integer, db.ForeignKey('team.idteam'))
) 

team_user_table = db.Table('team_user_table',
                db.Column('idUser', db.Integer, db.ForeignKey('user.idUser')),
                db.Column('idteam', db.Integer, db.ForeignKey('team.idteam'))
)

team_sprint_table = db.Table('team_sprint_table',
                db.Column('idsprint', db.Integer, db.ForeignKey('sprint.idsprint')),
                db.Column('idteam', db.Integer, db.ForeignKey('team.idteam'))
)

role_user_table = db.Table('role_user_table',
                db.Column('idUser', db.Integer, db.ForeignKey('user.idUser')),
                db.Column('idrole', db.Integer, db.ForeignKey('role.idrole'))
)

works_on = db.Table('works_on',
                db.Column('iduser', db.Integer, db.ForeignKey('user.iduser')),
                db.Column('iduser_stories', db.Integer, db.ForeignKey('user_stories.iduser_stories'))
)

user_user_stories_table = db.Table('user_user_stories_table',
                db.Column('iduser', db.Integer, db.ForeignKey('user.iduser')),
                db.Column('iduser_stories', db.Integer, db.ForeignKey('team.iduser_stories'))
)


user_stories_sprint_table = db.Table('user_stories_sprint_table',
                db.Column('idsprint', db.Integer, db.ForeignKey('sprint.idsprint')),
                db.Column('iduser_stories', db.Integer, db.ForeignKey('user_stories.iduser_stories'))
)



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password_hash = db.Column(db.String(120))
    id = synonym('idUser')
   #user_team = relationship('Team', secondary = 'team_user_table')

    teams = db.relationship('Team', secondary=team_user_table, backref=db.backref('userteams', lazy = 'dynamic'))
    user_stories = db.relationship('User_Stories', secondary=works_on, backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary=role_user_table, backref=db.backref('userroles', lazy='dynamic'))
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Project(db.Model):
    __tablename__ = 'project'
    idproject = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProjName = db.Column(db.String(45))
    total_diff = db.Column(db.Integer)
    id = synonym('idproject')    
   #proj_team = relationship('Team', secondary = 'team_project_table')
    teams = db.relationship('Team', secondary=team_project_table, backref=db.backref('projteams', lazy = 'dynamic'))
   # sprints = db.relationship('Sprint', secondary=project_sprint_table, backref=db.backref('projsprint', lazy='dynamic'))

class Team(db.Model):
    __tablename__ = 'team'
    idteam = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(45))
    id = synonym('idteam')
    projects = db.relationship('Project', secondary=team_project_table, backref=db.backref('projteams', lazy='dynamic'))
    users = db.relationship('User', secondary=team_user_table, backref=db.backref('teamusers', lazy='dynamic'))
    sprints = db.relationship('Sprint', secondary=team_sprint_table, backref=db.backref('teamsprint', lazy='dynamic'))

class To_do(db.Model):
    __tablename__ = 'to_do'
    idto_do = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean)
    text = db.Column(db.String(45))
   #iduser_stories = db.Column(db.Integer, db.ForeignKey(user_stories.idUser_Stories))
    todo_us = db.relationship('User_Stories', backref=db.backref('todo_userstories', lazy='dynamic'))

class Requirements(db.Model):
    __tablename__ = 'requirements'
    idrequirements = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean)
    text = db.Column(db.String(45))
    #iduser_stories = db.Column(db.Integer, db.ForeignKey(user_stories.idUser_Stories))
    todo_us = db.relationship('User_Stories', backref=db.backref('req_userstories', lazy='dynamic'))

class User_Stories(db.Model):
    __tablename__ = 'user_stories'
    idUser_Stories = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Acceptance_criteria = db.Column(db.String(45))
    Status = db.Column(db.String(45))
    Description = db.Column(db.String(400))
    Github_link = db.Column(db.String(100))
    Difficulty = db.Column(db.Integer)
    users = db.relationship('User', secondary=works_on, backref=db.backref('ususerr', lazy='dynamic'))
    sprints = db.relationship('sprint', secondary=user_stories_sprint_table, backref=db.backref('teamusers', lazy='dynamic'))

class Role(db.Model):
    __tablename__ = 'role'
    idrole = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45))
    users = db.relationship('User', secondary=role_user_table, backref=db.backref('roleusers', lazy='dynamic'))

class Sprint(db.Model):
    __tablename__ = 'sprint'
    SprintID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    end_date = db.Column(db.DateTime)
    Start_date = db.Column(db.DateTime)
    Teams = db.relationship('Team', secondary=team_sprint_table, backref=db.backref('teamsprints', lazy='dynamic'))
    user_stories = db.relationship('User_Stories', secondary=user_stories_sprint_table, backref=db.backref('sprintus', lazy='dynamic'))
    #projects = db.relationship('Project', secondary=project_sprint_table, backref=db.backref('sprintproj', lazy='dynamic'))
