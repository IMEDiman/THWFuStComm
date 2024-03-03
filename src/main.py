from src.backend import *
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO

class Mainview:
    def __init__(self) -> None:
        pass

    def viewmainhtml(self):
        return render_template('main.html', usersign=session['usersign'])
