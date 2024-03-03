from src.backend import *
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO

class Login:
    def __init__(self) -> None:
        pass

    def login(self):
        try:
            usersign = request.form['usersign']
            userpw = request.form['userpw']
        except:
            return render_template('index.html', message=f"Login fehlgeschlagen, Benutzername und Passwort müssen korrekt ausgefüllt werden!")
        
        if usersign == "" or userpw == "":
            return render_template('index.html', message=f"Login fehlgeschlagen, Benutzername und Passwort müssen korrekt ausgefüllt werden!")
        
        ret = User.login(usersign, userpw)

        if ret != User.INVALID_USER_ID:
            session['login'] = True
            session['userid'] = ret
            session['usersign'] = usersign
            return redirect('/')
        else:
            session['login'] = False
            session['userid'] = None
            session['usersign'] = None
            return render_template('index.html', message=f"Login fehlgeschlagen, Benutzername und Passwort müssen korrekt ausgefüllt werden!")
    
    def showlogin(self):
        return render_template('index.html')
    
    def logout(self):
        session['login'] = False
        session['userid'] = None
        session['usersign'] = None
        return render_template('index.html', message=f"Logout erfolgreich!")
