from flask import render_template as render, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import UserModel
from .form import LoginForm, RegisterForm
from app.services import get_user_by_username, register_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Método vista para el login de usuarios. """
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        user = get_user_by_username(login_form.username.data)
        if user is not None:
            if user.check_password(login_form.password.data):
                user_model = UserModel(user)
                login_user(user_model)
                flash("Bienvenido al sistema de ideas ....", category="info")
                return redirect(url_for("ideas.home"))
            else:
                flash("Credenciales incorrectas", category="error")
        else:
            flash("Credenciales incorrectas", category="error")

    return render('auth/login.html', **context)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Método vista para el registro de usuarios. """
    register_form = RegisterForm()
    context = {
        'register_form': register_form
    }

    if register_form.validate_on_submit():
        user = get_user_by_username(register_form.username.data)
        if user is None:
            # Proceso de registro de usuario
            user_data = {
                'name': register_form.name.data,
                'lastName': register_form.lastName.data,
                'username': register_form.username.data,
                'email': register_form.email.data,
                'cellphone': register_form.cellphone.data,
                'password': register_form.password.data,
            }

            register_user(user_data)
            user_model = UserModel(
                get_user_by_username(register_form.username.data)
            )
            login_user(user_model)
            flash(" Registro exitoso, bienvenido", category="info")
            return redirect(url_for("ideas.home"))
        else:
            flash("El usuario ya existe en el sistema!", category="warning")

    return render('auth/signup.html', **context)


@auth.route('/logout')
@login_required
def logout():
    """ Método para cerrar sesion. """
    logout_user()
    flash("Cerrarte sesion !!", category="info")
    
    return redirect(url_for('index'))

