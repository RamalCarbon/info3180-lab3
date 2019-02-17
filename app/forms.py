from flask_wtf import FlaskForm
from wtforms import StringField
# from wtforms import TextField
from wtforms.validators import DataRequired
from wtforms_components import Email
from app import mail
from flask_mail import Message
# from wtforms.fields import TextField

class MyForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[Email()]
    # email = TextField("Email",[validators.Required("Please enter your email address."),validators.Email("Please enter your email address.")])
    subject = StringField('subject',validators=[DataRequired()])
    message = TextField('message')
    submit = SubmitField("Send")