from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ProjectForm(FlaskForm):
    ProjName = StringField('Project Name')
    submit = SubmitField('Submit')
    team_name = StringField('Team Name')

class User_StoriesForm(FlaskForm):
    Difficulty = IntegerField('Difficulty')
    Acceptance_criteria = StringField('Acceptance_criteria')
    Status = StringField('Status')
    Description = StringField('Descriprion')
    Github_link = StringField('Github_link')

class TodoForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')

class requirementsForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')

class RoleForm(FlaskForm):
    title = StringField('title')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


