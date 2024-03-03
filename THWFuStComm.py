from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO


from src.login import Login
from src.main import Mainview
from src.backend import *

APP_SECRET_KEY = '3vSi6eaE2WKfQpjGM30p' # MUST BE CHANGED FOR PRODUCTION INSTANCES! (to a random secure value)
#this value is publicly on github and cannot be used in production environments

class THWFuStComm:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = APP_SECRET_KEY
        self.login = Login()
        self.mainview = Mainview()

        self.socket_io = SocketIO(self.app, cors_allowed_origins="*")

        self.setup_routes()

    def setup_routes(self):
        self.app.route("/")(self.home)
        self.app.route("/login", methods=['POST'])(self.login.login)
        self.app.route("/login", methods=['GET'])(self.login.showlogin)
        self.app.route("/logout")(self.login.logout)
        #self.app.add_url_rule('/<role>', view_func=self.select_role)

        @self.socket_io.on('message')
        def handle_message(message):
            self.handle_message(message)

    def home(self):
        if 'login' in session and session['login']:
            return self.mainview.viewmainhtml()
        else:
            return self.login.showlogin()
    
    #def select_role(self, role):
    #    print(self.agents)
    #    if role == "Funker":
    #        return render_template('main.html')
    #    else:
    #        return render_template('main.html')
            
    def handle_message(self,message):
        print("Received message:",message)
        self.socket_io.emit('message',message)
    
    def run(self):
        #self.app.run(host='0.0.0.0', port=5000, debug=True)
        self.socket_io.run(self.app,host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    THWFuStComm_app = THWFuStComm()
    THWFuStComm_app.run()
    
