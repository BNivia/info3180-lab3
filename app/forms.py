from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()], description="Please enter your full name.")
    email = StringField('E-mail', validators=[DataRequired(), Email()], description="Please enter your email address.")
    subject = StringField('Subject', validators=[DataRequired()], description="Please enter the subject of your message.")
    body = TextAreaField('Body',validators=[DataRequired()], description="Please enter the messgae you would like to send.")