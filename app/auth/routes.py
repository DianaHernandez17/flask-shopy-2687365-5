from . import auth
from flask import render_template,redirect,flash
from .forms import LoginForm
import app

#dependencias para auth
from flask_login import current_user, login_user,logout_user

#ruta de login 
@auth.route('/login' , 
            methods = ['GET' , 'POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        # Seleccionar el Cliente con ese username
        c = app.models.Cliente.query.filter_by(username = f.username.data).first()
        if c is None or c.check_password(f.password.data):
            return redirect('/auth/login')
        else:
            login_user(c , True)
            return redirect('/clientes/listar')
    return render_template("login.html",
                           f = f)


#ruta de logout
@auth.route('/logout')
def  logout():
    
    logout_user()
    return redirect("/auth/login")
