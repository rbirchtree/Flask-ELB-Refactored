from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phonenumber = StringField('Phone Number', validators=[DataRequired()])
    propertyaddress = StringField('Property Address', validators=[DataRequired()])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')