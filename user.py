from flask import Flask
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#database set up
class User(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tactics_elo = db.Column(db.Integer, nullable=False)
    tactics_streak = db.Column(db.Integer, nullable=False)
    multiplayer_elo = db.Column(db.Integer, nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username

#default scores for ELO system
TACTICS_ELO_DEFAULT = 1500
TACTICS_STREAK_DEFAULT = 0
MULTIPLAYER_ELO_DEFAULT = 1500

#function creates user
def user_create(username, password):
    print('User name is ' + username + ' and password is ' + password)

    new_user = User(username=username, password=password, tactics_elo=TACTICS_ELO_DEFAULT, tactics_streak=TACTICS_STREAK_DEFAULT, multiplayer_elo=MULTIPLAYER_ELO_DEFAULT)
    db.session.add(new_user)
    db.session.commit()

#call function after game is done to update user stats regarding ELO system
def user_update_stats(username, tactics_elo, tactics_streak, multiplayer_elo):
    user = User.query.filter_by(username=username).first()
    user.tactics_elo = tactics_elo
    user.tactics_streak = tactics_streak
    user.multiplayer_elo = multiplayer_elo
    db.session.commit()

#function for logging in
def validate_user(username, password):
    testuser=User.query.filter_by(username=username).first()
    if testuser:
        print("got user")
        if testuser.password == password:
            testuser.is_authenticated = True
            return testuser
    return None









