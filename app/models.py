from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import synonym, relationship, backref

team_project_table = db.Table('team_project_table',
                              db.Column('project_id', db.Integer, db.ForeignKey('project.project_id')),
                              db.Column('team_id', db.Integer, db.ForeignKey('team.team_id'))
                              )

team_user_table = db.Table('team_user_table',
                           db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                           db.Column('team_id', db.Integer, db.ForeignKey('team.team_id')),
                           db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
                           )

team_sprint_table = db.Table('team_sprint_table',
                             db.Column('sprint_id', db.Integer, db.ForeignKey('sprint.sprint_id')),
                             db.Column('team_id', db.Integer, db.ForeignKey('team.team_id'))
                             )

project_sprint_table = db.Table('project_sprint_table',
                                db.Column('sprint_id', db.Integer, db.ForeignKey('sprint.sprint_id')),
                                db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'))
                                )

role_user_table = db.Table('role_user_table',
                           db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                           db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
                           )

works_on = db.Table('works_on',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                    db.Column('user_stories_id', db.Integer, db.ForeignKey('user_stories.user_stories_id'))
                    )

user_user_stories_table = db.Table('user_user_stories_table',
                                   db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                                   db.Column('user_stories_id', db.Integer,
                                             db.ForeignKey('user_stories.user_stories_id'))
                                   )

user_stories_sprint_table = db.Table('user_stories_sprint_table',
                                     db.Column('sprint_id', db.Integer, db.ForeignKey('sprint.sprint_id')),
                                     db.Column('user_stories_id', db.Integer,
                                               db.ForeignKey('user_stories.user_stories_id'))
                                     )

user_stories_project_table = db.Table('user_stories_project_table',
                                      db.Column('project_id', db.Integer, db.ForeignKey('project.project_id')),
                                      db.Column('user_stories_id', db.Integer,
                                                db.ForeignKey('user_stories.user_stories_id'))
                                      )


# check
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password_hash = db.Column(db.String(120))
    id = synonym('user_id')
    # user_team = relationship('Team', secondary = 'team_user_table')

    teams = db.relationship('Team', secondary=team_user_table, backref=db.backref('userteams', lazy='dynamic'))
    user_stories = db.relationship('User_Stories', secondary=works_on, backref=db.backref('ususers', lazy='dynamic'))
    roles = db.relationship('Role', secondary=role_user_table, backref=db.backref('userroles', lazy='dynamic'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proj_name = db.Column(db.String(45))
    total_diff = db.Column(db.Integer)
    id = synonym('project_id')
    Dod = db.Column(db.String(200))
    # proj_team = relationship('Team', secondary = 'team_project_table')
    teams = db.relationship('Team', secondary=team_project_table, backref=db.backref('projteams', lazy='dynamic'))
    sprints = db.relationship('Sprint', secondary=project_sprint_table,
                              backref=db.backref('projsprint', lazy='dynamic'))
    # userstories = db.relationship('UserStories', secondary=user_stories_project_table, backred=db.backref('projuserstroies', lazy='dynamic'))


class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(45))
    id = synonym('team_id')
    # projects = db.relationship('Project', secondary=team_project_table, backref=db.backref('projteams', lazy='dynamic'))
    # users = db.relationship('User', secondary=team_user_table, backref=db.backref('teamusers', lazy='dynamic'))
    sprints = db.relationship('Sprint', secondary=team_sprint_table, backref=db.backref('teamsprint', lazy='dynamic'))


class To_do(db.Model):
    __tablename__ = 'to_do'
    to_do_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean)
    text = db.Column(db.String(45))
    id = synonym('to_do_id')
    user_stories_id = db.Column(db.Integer, db.ForeignKey('user_stories.user_stories_id'))
    # todo_us = db.relationship('User_Stories', backref=db.backref('todo_userstories', lazy='dynamic'))


class Requirements(db.Model):
    __tablename__ = 'requirements'
    requirements_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean)
    text = db.Column(db.String(45))
    id = synonym('requirements_id')
    user_stories_id = db.Column(db.Integer, db.ForeignKey('user_stories.user_stories_id'))
    # req_us = db.relationship('User_Stories', backref=db.backref('req_userstories', lazy='dynamic'))


class User_Stories(db.Model):
    __tablename__ = 'user_stories'
    user_stories_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Acceptance_criteria = db.Column(db.String(45))
    Status = db.Column(db.String(45))
    title = db.Column(db.String(45))
    Description = db.Column(db.String(400))
    Github_link = db.Column(db.String(100))
    Difficulty = db.Column(db.Integer)
    id = synonym('user_stories_id')

    # users = db.relationship('User', secondary=works_on, backref=db.backref('ususerr', lazy='dynamic'))
    sprints = db.relationship('Sprint', secondary=user_stories_sprint_table,
                              backref=db.backref('teamusers', lazy='dynamic'))
    #us_todo = db.relationship('To_do', backref=db.backref('usto_do'))
    #us_req = db.relationship('Requirements', backref=db.backref('us_req'))
    projects = db.relationship('Project', secondary=user_stories_project_table,
                               backref=db.backref('usproj', lazy='dynamic'))


class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45), nullable=False, unique=True)
    id = synonym('role_id')
    # users = db.relationship('User', secondary=role_user_table, backref=db.backref('roleusers', lazy='dynamic'))


class Sprint(db.Model):
    __tablename__ = 'sprint'
    sprint_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    end_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    sprint_num = db.Column(db.Integer)
    Retro = db.Column(db.String(200))
    Review = db.Column(db.String(200))
    id = synonym('sprint_id')
    # Teams = db.relationship('Team', secondary=team_sprint_table, backref=db.backref('teamsprints', lazy='dynamic'))
    # user_stories = db.relationship('User_Stories', secondary=user_stories_sprint_table, backref=db.backref('sprintus', lazy='dynamic'))
    projects = db.relationship('Project', secondary=project_sprint_table,
                               backref=db.backref('sprintproj', lazy='dynamic'))
