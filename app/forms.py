from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

#Forms use a library called WTF forms that make it easy to obtain and maintain restrictions on data coming form the
#user, it also provides a submit button in html

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ProjectForm(FlaskForm):
    proj_name = StringField('Project Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    team_name = StringField('Team Name', validators=[DataRequired()])
    github_link = StringField('GitHub Link')


class AddMemberForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enter')


class DodForm(FlaskForm):
    Dod = TextAreaField('Def of done', validators=[DataRequired()])
    submit = SubmitField('Save')


class User_StoriesForm(FlaskForm):
    Difficulty = IntegerField('Difficulty', validators=[DataRequired()])
    Acceptance_criteria = TextAreaField('Acceptance Criteria', validators=[DataRequired()])
    status = StringField('Status')
    Description = TextAreaField('Description', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    Review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Save')


class RetroForm(FlaskForm):
    Retro = TextAreaField('Retro', validators=[DataRequired()])
    submit = SubmitField('Save')


class TodoForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')


class RequirementsForm(FlaskForm):
    status = BooleanField('stats')
    text = StringField('text')


class RoleForm(FlaskForm):
    title = StringField('Role Title', validators=[DataRequired()])  # Make this field unique?
    submit = SubmitField('Create role')


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
    #Makes it so that the user know the format that the date has to be entered in, format also converts the format that
    #We chose to enforce to the format that MYSQL uses
    start_date = DateField('Start Date (MM-DD-YYYY)', format='%m-%d-%Y', validators=[DataRequired()])
    end_date = DateField('End Date (MM-DD-YYYY)', format='%m-%d-%Y', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GitHubForm(FlaskForm):
    github_link = StringField('Edit GitHub link', validators=[DataRequired()])
    submit = SubmitField('Update GitHub link')
