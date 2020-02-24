from wtforms import (Form, 
                     StringField, 
                     PasswordField,
                     HiddenField, 
                     validators, 
                     SubmitField)
from wtforms.validators import (ValidationError, 
                                DataRequired, 
                                Email, 
                                EqualTo, 
                                Length, 
                                Optional)
from wtforms_components import EmailField


class SignupForm(Form):
    """ User Signup Form """
    username = StringField('Username', validators=[DataRequired
               (message=('Enter Your Username'))])
    email = EmailField("Email",
            [DataRequired(), Length(3, 254)])
    firstname = StringField('Firstname', validators=[DataRequired
                (message=('Enter your Firstname'))])
    lastname = StringField('Lastname', validators=[DataRequired
               (message=('Enter your Lastname'))])
    password = PasswordField('Password',validators=[DataRequired(message='Please enter a password.'),
               Length(min=6,message=("Minimum of six characters"))])
    
class LoginForm(Form):
        email = EmailField("Email",
            [DataRequired(), Length(3, 254)])
        password = PasswordField('Password',validators=[DataRequired(message='Enter your password.')])
