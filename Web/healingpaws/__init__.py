from flask import Flask
from appdir.config import DatabaseSecretConfig
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config.from_object(DatabaseSecretConfig)
db = SQLAlchemy(app)

from appdir import routes, models,dbConnector
db.create_all()
dbConnector.databaseDebug()
