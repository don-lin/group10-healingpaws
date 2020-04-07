from flask import Flask
from healingpaws.config import DatabaseSecretConfig
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder="html")

app.config.from_object(DatabaseSecretConfig)
db = SQLAlchemy(app)

from healingpaws import routes, models,dbConnector
db.create_all()
dbConnector.databaseDebug()
