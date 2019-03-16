from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField 
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired('Your name is required!')])
    email = TextField('Email Address', validators=[DataRequired('An email address is required!'), Email('Please enter an appropriate email address.')])
    subject = TextField('Subject', validators=[DataRequired('A subject is required!')])
    message = TextAreaField('Message', validators=[DataRequired('A message is required!')])