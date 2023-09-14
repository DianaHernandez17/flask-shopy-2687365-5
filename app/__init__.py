from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#llamar modulos en la misma carpeta 
from .config import Config
from flask_bootstrap import Bootstrap


#BLUEPRINT
from .mi_blueprint import mi_blueprint
from app.clientes import clientes
from app.auth import auth




#configurar flask a traves de un objeto
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)

#registro de blueprints(modulos)
app.register_blueprint(mi_blueprint)
app.register_blueprint(clientes)
app.register_blueprint(auth)







db = SQLAlchemy(app)
migrate=Migrate(app, 
                db)

from .models import Cliente, Producto, Venta, Detalle

@app.route('/prueba')
def prueba ():
    return render_template("prueba.html")
