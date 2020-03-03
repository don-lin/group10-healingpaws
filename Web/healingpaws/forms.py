from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, FileField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('goto sign up if password wrong')
    submit=SubmitField('log in')


class UpdateForm(FlaskForm):
    birthday=StringField('birthday')
    email=StringField('email')
    gender = RadioField('Gender', choices = [('1','Male'),('0','Female')])
    cv = FileField('Update your profile photo (JPG file)')
    update=SubmitField('update')


class SignupForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('sign up')


class CommentForm(FlaskForm):
    commentContent=StringField('Comments Content')
    commentSubmit=SubmitField("comment")
    favorSubmit=SubmitField("favor")
    hateSubmit=SubmitField("hate")

class ResetForm(FlaskForm):
    password=PasswordField('Input a new password',validators=[DataRequired()])
    submit=SubmitField('reset password')


class MessageForm(FlaskForm):
    messageTitle=StringField("title",validators=[DataRequired()])
    messageContent=TextAreaField("content",validators=[DataRequired()])
    photo=FileField("You can attach a image for the message(JPG file, Not Mandatory)")
    messageSend=SubmitField("send message")

