import os

class DevelopmentConfig:

    # Flask
    DEBUG = True
    SECRET_KEY = '\x9b\xa2|\xcf\xd3\xee\xe1v| <`o\xfb_4\xc6\xda\x81\x02\xd3e\xf4\x16'

    # sqlalchemy
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/heroku_27e2cd148cb227a?charset=utf8'.format(**{
      'user': os.getenv('DB_USER', 'beab2a78d26a0a'),
      'password': os.getenv('DB_PASSWORD', '4ed1bd4c'),
      'host': os.getenv('DB_HOST', 'us-cdbr-iron-east-02.cleardb.net'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig