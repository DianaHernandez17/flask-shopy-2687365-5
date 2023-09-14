from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField(
               label = 'Nombre de usuario: ',
               validators=[InputRequired(
                    message="Nombre requerido")
               ])
    
    password = PasswordField(
                label ='Password',
                validators=[InputRequired(
                    message="Password requerido")
                    
                ])
   
    submit = SubmitField('Iniciar Sesión')

