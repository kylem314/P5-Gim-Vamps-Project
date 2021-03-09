#imports
from flask import (Flask, g, redirect, render_template, request, session, url_for)
from user import user_create
from flask_sqlalchemy import SQLAlchemy
import requests
import chessdata
from chessdata import board, movelist, og_board, ogstoreboard, movesdata, actualMove, previousMove
from markupsafe import escape
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from user import validate_user, User, user_create, user_update_stats
from htmlToPythonAdditions import HTPlen5
import getpass
import mysql.connector
import webbrowser
import random


app = Flask(__name__)


# database setup
dbURI = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)

#conn = mysql.connector.connect(user='root', password='',
                               #host='localhost',database='company')

#if conn:
    #print ("Connected Successfully")
#else:
    #print ("Connection Not Established")

#login setup
app.config['SECRET_KEY'] = '1234'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#using login_manager.user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()


#route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #username and password variables from form
        username = request.form['Username']
        password = request.form['password']
        #just to check if username and password was collected
        print(username +" " + password)
        #calls validate_user function from user.py
        user = validate_user(username, password)

        if user:
            #if validate_user = true, log user in and return profile.html template
            login_user(user)
            db.session.commit()
            #variables that are called in profile.html
            session['user_name'] = user.username
            session['tactics_elo'] = user.tactics_elo
            session['tactics_streak'] = user.tactics_streak
            session['multiplayer_elo'] = user.multiplayer_elo
            return render_template("profile.html")
    else:
        print('Bar')
        #if validate_user = false, return login page
    return render_template("login.html")


#route for profile page
#@login_required tag used to ensure that user cannot access profile if not signed in
@app.route('/profile')
@login_required
def profile():
        return render_template('profile.html', name=current_user.username)

#route for logging out
#@login_required tag used to ensure that user must be logged in to log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))

#home page route
@app.route('/')
def home():
    return render_template("home.html")

#play menu route
@app.route('/play')
def playmenu():
    return render_template("playmenu.html")

#sign up page route
@app.route('/signup' ,methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        #get username and password from form
        username = request.form['Username']
        password = request.form['password']
        #calls user_create function from user.py
        user_create(username, password)
        #returns signconfirm.html(signup confirmation page)
        return render_template("signconfirm.html")
        db.session.commit()

    else:
        print('Bar')
        #if for some reason form doesn't go through for some reason, returns signup page again
    return render_template("signup.html")

#sign up success page returned after post process above
@app.route('/signupsuccess')
def signconfirm():
    return render_template("signconfirm.html")

@app.route('/chessdicttable')
def chessdicttable():
    return render_template("chessdicttable.html")

#main ai chess game route
@app.route('/multiplayermain')
def playai():
    return render_template("multiplayermain.html")


#multiplayer chess game route
@app.route('/MultiplayerMenu')
def MultiplayerMenu():
    return render_template("MultiplayerMenu.html")

@app.route('/multiplayermain')
def multiplayermain():
    return render_template("multiplayermain.html")

#easter egg route(found on how to play section on home page)
@app.route('/easter')
def easter():
    return render_template("easter.html")

#route to replay a chess game
@app.route('/replaygame')
def replaygame():
    return render_template("replaygame.html")

#route to join a chess game
@app.route('/joingame')
def joingame():
    return render_template("joingame.html")

#chess offline website leaderboards
@app.route('/leaderboards')
def leaderboards():
    return render_template("leaderboards.html")

#web api route where data is grabbed from different types of chess
@app.route('/lichesslb/<type>/', methods=['GET', 'POST'])
def lichesslb(type):
    print(type)
    url = "https://lichess.org/player/top/100/" + type + "/"
    headers = {
        'Accept': 'application/vnd.lichess.v3+json'
    }
    response = requests.get(url, headers=headers)
    data = response.json().get('users')
    type = type.capitalize()
    return render_template("webapi2.html", data=data, type=type)



#Chess code
@app.route("/createBoardTable", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoardTable():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        movelist.clear()#resets the stored moves when create board is selected
        board = og_board #resets the board
        storeboard = ogstoreboard #resets the storboard
        return render_template("chessDictTable.html", displayClicked="  ", allBoard=chessdata.split_board(board))


@app.route("/board/<space>", methods=['GET','POST'])
def boardprint(space):
    if request.method == 'POST':
        return render_template("chessDictTable.html", displayClicked=space, movelist=chessdata.movesdata(space),  message=chessdata.sample(len(movelist),chessdata.movelist[-2:]), allBoard=chessdata.split_board(board))



if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

