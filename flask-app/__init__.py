from flask import Flask 

from .commands import create_tables
from .extensions import db, login_manager
from .models import Doctor
##TODO: from .routes.auth import auth add login
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    ##login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_doctor(user_id):
        return Doctor.query.get(doctor_id)

    app.register_blueprint(main)
    ##app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app