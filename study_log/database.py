from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
import os

db = SQLAlchemy()

# engine = create_engine('mysql+pymysql://{user}:{password}@{host}/studylog?charset=utf8'.format(**{
#     'user': os.getenv('DB_USER', 'root'),
#     'password': os.getenv('DB_PASSWORD', 'QEQF9731'),
#     'host': os.getenv('DB_HOST', 'localhost'),
# }))

# Session = sessionmaker(bind=engine)
# session = Session()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)