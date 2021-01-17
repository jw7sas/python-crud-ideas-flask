from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    """ Formulario de registro de usuarios. """
    name = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField("Apellido", validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    email = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=30)])
    cellphone = StringField("Celular", validators=[DataRequired(), Length(min=7, max=20)])
    password = PasswordField("Nueva contraseña", validators=[
        DataRequired(),
        Length(min=6, max=10),
        EqualTo('password_confirm')
    ])
    password_confirm = PasswordField("Confimarción de contraseña", validators=[DataRequired(), Length(min=6, max=10)])

    submit = SubmitField("Registrame")


class LoginForm(FlaskForm):
    """ Formulario de login. """
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=10)])

    submit = SubmitField("Login")