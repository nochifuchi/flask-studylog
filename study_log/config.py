import os

class DevelopmentConfig:

    # Flask
    DEBUG = True
    SECRET_KEY = '\x9b\xa2|\xcf\xd3\xee\xe1v| <`o\xfb_4\xc6\xda\x81\x02\xd3e\xf4\x16'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/studylog?charset=utf8'.format(**{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'QEQF9731'),
      'host': os.getenv('DB_HOST', 'localhost'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig