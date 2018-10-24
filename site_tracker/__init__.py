from flask import Flask

from .dao import db
from tracker.views import tracker
from user.views import users

app = Flask(__name__)
app.config.from_object('config')


@app.context_processor
def provide_constants():
    return {"constants": {"RIGHTS": "2018 Calvin's Dad"}}

db.init_app(app)


app.register_blueprint(tracking)
app.register_blueprint(users)
