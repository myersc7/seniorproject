from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ProjectForm(FlaskForm):
    proj_name = StringField('Project Name',validators=[DataRequired()])
    submit = SubmitField('Submit')
    team_name = StringField('Team Name', validators=[DataRequired()])
    github_link = StringField('Github Link')


class User_StoriesForm(FlaskForm):
    difficulty = IntegerField('Difficulty')
    acceptance_criteria = TextAreaField('Acceptance Criteria')
    status = StringField('Status')
    description = StringField('Description')
    title = StringField('Title')
    submit = SubmitField('Submit')


class TodoForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')


class RequirementsForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')


class RoleForm(FlaskForm):
    title = StringField('title')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SprintForm(FlaskForm):
    start_date = DateField('Start Date (YYYY-MM-DD)', validators=[DataRequired()])
    end_date = DateField('End Date (YYYY-MM-DD)', validators=[DataRequired()])
    sprint_num = IntegerField('Sprint Number', validators=[DataRequired()])
    submit = SubmitField('Submit')
