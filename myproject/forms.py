from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from wtforms import ValidationError
from flask_login import current_user
from myproject.models import User

#after Registration user must be able to login
class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    submit = SubmitField('Log in ')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email(message='Invalid Email')])
    username = StringField('Username',validators = [DataRequired(),Length(min=3,max=32)])
    password = PasswordField('Password',validators = [DataRequired(),EqualTo('pass_confirm',message = 'Passwords must match!'),Length(min=3)])
    pass_confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Register')


    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():  # to check that email has already been registered or not
           raise ValidationError('Your email has been already registered!')


    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():  # to check that username has already been taken or not
           raise ValidationError('Username is taken!')


class HowToSplit(FlaskForm):
    selection = IntegerField('Select the option number',validators=[DataRequired()])
    submit = SubmitField('Submit')
