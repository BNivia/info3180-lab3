from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    body = StringField('body',validators=[DataRequired()])