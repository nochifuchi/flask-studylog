from flask import Flask
from .database import db, init_db

def create_app():
    app = Flask(__name__, static_folder='../static/')
    app.config.from_object('study_log.config.Config')

    init_db(app)

    return app

app = create_app()

import study_log.views