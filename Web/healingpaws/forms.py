# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, FileField,TextAreaField, SelectField
# from wtforms.validators import DataRequired
# from flask_wtf.file import FileRequired, FileAllowed

# class LoginForm(FlaskForm):
#     username=StringField('Username',validators=[DataRequired()])
#     password=PasswordField('Password',validators=[DataRequired()])
#     remember_me=BooleanField('goto sign up if password wrong')
#     submit=SubmitField('log in')

# #ssss
# class UpdateForm(FlaskForm):
#     birthday=StringField('birthday')
#     email=StringField('email')
#     gender = RadioField('Gender', choices = [('1','Male'),('0','Female')])
#     cv = FileField('Update your profile photo (JPG file)')
#     update=SubmitField('update')

# class CommentForm(FlaskForm):
#     commentContent=StringField('Comments Content')
#     commentSubmit=SubmitField("comment")
#     favorSubmit=SubmitField("favor")
#     hateSubmit=SubmitField("hate")

# class ResetForm(FlaskForm):
#     password=PasswordField('Input a new password',validators=[DataRequired()])
#     submit=SubmitField('reset password')


# class MessageForm(FlaskForm):
#     messageTitle=StringField("title",validators=[DataRequired()])
#     messageContent=TextAreaField("content",validators=[DataRequired()])
#     photo=FileField("You can attach a image for the message(JPG file, Not Mandatory)")
#     messageSend=SubmitField("send message")

# class SignupForm(FlaskForm):
# 	username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'username'})
# 	email = StringField('Email', validators=[DataRequired()], render_kw={'class': 'password'})
# 	password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'password'})
# 	password2 = PasswordField('Repeat Password', validators=[DataRequired()], render_kw={'class': 'password'})
# 	accept_rules = BooleanField('I accept the site rules', validators=[DataRequired()])
# 	submit = SubmitField('Register',render_kw={'class':'submit'})

# class CustomerProfileForm(FlaskForm):
#     #picture这块我不太会写
#     # picture = FileField('picture')
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired()])
#     # phone = StringField('Phone Number', validators=[DataRequired()])
#     gender = SelectField('Gender', coerce=int, choices=[(1, 'male'), (2, 'female')])
#     submit = SubmitField("Save")
