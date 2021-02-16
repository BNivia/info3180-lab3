from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = TextAreaField('Body',validators=[DataRequired()])