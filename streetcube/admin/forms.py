"""Form class declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,DateField,SelectField,BooleanField,HiddenField,FileField
from wtforms.validators import DataRequired,Email,EqualTo,Length,URL,ValidationError
from wtforms import validators
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    """ Login form """
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[DataRequired("Password required")])

class EmailForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired('Email is required'), validators.Email()])
    submit = SubmitField('Submit')    


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    
class UserForm(FlaskForm):
    uname = StringField('User Name', validators=[DataRequired('Name is required'), Length(min=3, max=50)])
    email = EmailField('Email', [validators.DataRequired('Email is required'), validators.Email()])
    password = PasswordField('password', validators=[DataRequired('Password is required'), Length(min=5, max=16)])
    address = StringField('ADDRESS',validators=[DataRequired('Address is required')])
    mobile = StringField('MOBILE',validators=[DataRequired('Please enter your mobile number'),Length(max=10)])
    c_name = StringField('Company Name',validators=[DataRequired('Company name is required')])
    b_name = StringField('Brand Name',validators=[DataRequired('Brand name is required')])
    descrip_of_service = StringField('Description of service',validators=[DataRequired('Description is required')])
    story = StringField('Story',validators=[DataRequired('Story field is required')])

class BookSlotForm(FlaskForm):
    select_date = StringField('Select Date',validators=[DataRequired('Date is required')])
    choose_slot = StringField('Choose Slot',validators=[DataRequired('Date is required')])