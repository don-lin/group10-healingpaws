from flask import Flask
from healingpaws.config import DatabaseSecretConfig
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder="html")


def get_content(arr,id):
    for a in arr:
        if a.id==id:
            return a
    return None
app.add_template_global(get_content,'get_content')


app.config.from_object(DatabaseSecretConfig)
db = SQLAlchemy(app)

from healingpaws import routes, models,dbConnector
db.create_all()
