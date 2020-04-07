import os

class DatabaseSecretConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    imagedir = os.path.join(basedir, 'upload_jpg')
    cssdir=os.path.join(basedir,'html/css')
    jsdir=os.path.join(basedir,'html/javascript')
    imgdir = os.path.join(basedir,'html/img')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'mydb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False