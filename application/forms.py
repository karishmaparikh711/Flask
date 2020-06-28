from flask_wtf import FlaskForm
from wtforms import Form, validators
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import Form,validators,StringField,IntegerField,FloatField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import Patient,Admin



class LoginForm(FlaskForm):
    username   = StringField("Username", [validators.DataRequired(message="Username is Required"), validators.Length(message='UserName should be Minimun 4 characters.',
                          min=4) ] )
    password = PasswordField("Password", [ validators.DataRequired(message="Password is Required"), validators.Length(message='Password should be and 5 characters.',
                          min=5)] )
    submit = SubmitField("Login")


class CreateCustomer(FlaskForm):
    ssnid = IntegerField("SSN ID", [validators.DataRequired(message="SSN ID is Required"), validators.NumberRange(message='SSN should be exactly 9', min=100000000, max=999999999) ])
    name = StringField("Name", [validators.DataRequired(message="Name is Required"), validators.Regexp(message='Name should only alphabet', regex=r'^[a-zA-Z ]*$') , validators.Length(message='Name should only alphabet and minimum 3 character', min=3, max=25) ] )
    age = IntegerField("Age", [validators.DataRequired(message="Age is Required"), validators.NumberRange(message='Minimum age is 10', min=10, max=120) ])
    address = StringField("Address", [ validators.DataRequired(message="Address is Required") ])
    dateofadmit=StringField("DAte of Admit",[validators.DataRequired(message="Date of admit is Required")])
    typeofbed=StringField("Type of bed",[validators.DataRequired(message="Type of bed Required")])
    state = StringField()
    city = StringField()
    submit = SubmitField("Register Now")





        