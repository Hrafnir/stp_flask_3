from flask import Flask
from config import Config
from models import *
from admin import *


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin.init_app(app)


from views import *

with app.app_context():
    db.create_all()
