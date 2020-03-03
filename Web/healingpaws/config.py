import os
# The idea of how to write flask form come from the week9-Introducing Flask and week10-Flask-and-WebForms and week11-Flask and Databases
#After learn these PPT. I write this code
class DatabaseSecretConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    imagedir = os.path.join(basedir, 'upload_jpg')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'mydb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False