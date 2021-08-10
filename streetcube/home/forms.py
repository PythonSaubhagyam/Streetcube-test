"""Form class declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,DateField,SelectField,BooleanField,HiddenField,FileField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,Length,URL,ValidationError,Regexp
from wtforms import validators
from wtforms.fields.html5 import EmailField

from streetcube.models import UserInfo,Contact




class LoginForm(FlaskForm):
    """ Login form """
    email = EmailField('email', validators=[DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[DataRequired("Password required")])


class EmailForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired('Email is required'), validators.Email()])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        user_object = UserInfo.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already exists. Select a different email.")

class UserForm(FlaskForm):
    uname = StringField('User Name',validators=[DataRequired('Name is required'),Length(min=2,max=16)]) 
    submit = SubmitField('Submit')


class UserLastNameForm(FlaskForm):
    lname = StringField('Last Name',validators=[DataRequired('Name is required'),Length(min=2,max=16)]) 
    submit = SubmitField('Submit')    


class PasswordForm(FlaskForm):
    password = StringField('password',validators=[DataRequired('Password is required'),Length(min=5,max=16)])
    submit = SubmitField('Submit')

class MobileForm(FlaskForm):
    # is_show_mobile = BooleanField('IS_SHOW_MOBILE',validators=[DataRequired()])
    mobile = StringField('MOBILE',validators=[DataRequired('Please enter your mobile number'),Length(min=3,max=20)])
    submit = SubmitField('Submit')


class OtpForm(FlaskForm):
    otp = StringField('MOBILE',validators=[DataRequired('Please enter your otp no'),Length(min=4,max=4)])
    submit = SubmitField('Submit')

class MobileVerifyForm(FlaskForm):
    is_mobile_verified = BooleanField('IS_MOBILE_VERIFIED',validators=[DataRequired()])
    submit = SubmitField('Submit')

#custom register form

class RegisterForm(FlaskForm):
    # email = EmailField('Email', [validators.DataRequired('Email is required'), validators.Email()])
    email = EmailField('Email', [validators.DataRequired(),validators.EqualTo('confemail', message='Email must be same')])
    confemail = EmailField('Email', [validators.DataRequired('Email is required'), validators.Email()])
    uname = StringField('User Name',validators=[DataRequired('Name is required'),Length(min=2,max=16)]) 
    lname = StringField('Last Name',validators=[DataRequired('Name is required'),Length(min=2,max=16)]) 
    password = StringField('password',validators=[DataRequired('Password is required'),Length(min=5,max=16)])
    mobile = StringField('MOBILE',validators=[DataRequired('Please enter your mobile number. Ex: 1234567890'), Length(min=10,max=10)])
    submit = SubmitField('Submit') 

    def validate_email(self, email):
        user_object = UserInfo.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already exists. Select a different email.")   




class TraderDetailsForm(FlaskForm):
    address = StringField('ADDRESS',validators=[DataRequired('Address is required')])
    mobile = StringField('MOBILE',validators=[DataRequired('Please enter your mobile number'),Length(max=10)])
    email = StringField('EMAIL',validators=[DataRequired('Email is required')])
    c_name = StringField('Company Name',validators=[DataRequired('Company name is required')])
    b_name = StringField('Brand Name',validators=[DataRequired('Brand name is required')])
    descrip_of_service = StringField('Description of service',validators=[DataRequired('Description is required')])
    story = StringField('Story',validators=[DataRequired('Story field is required')])
    


class TraderDetailsUploadForm(FlaskForm):
    pub_lib_insu = FileField('Public libility insurance',validators=[DataRequired('Insurance document is required')])
    c_19risk_asses = FileField('Covid 19 risk assessment',validators=[DataRequired('Covid 19 assessment document is required')])
    food_certi = FileField('Food certificate',validators=[DataRequired('Food document is required')])

class BookSlotForm(FlaskForm):
    select_date = StringField('Select Date',validators=[DataRequired('Date is required')])

class ShowBookDateForm(FlaskForm):
    select_date = DateField('Select Date',validators=[DataRequired('Date is required')])


class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired('Full name is required')])
    email = StringField('EMAIL', validators=[DataRequired('Email is required')])
    subject = StringField('SUBJECT', validators=[DataRequired('Subject  is required')])
    msg = StringField('Message', validators=[DataRequired('Message is required')])


