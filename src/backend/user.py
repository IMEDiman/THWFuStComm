#!/bin/env python3

import random

class User:
    INVALID_USER_ID = -1

    ROLE_INVALID = -1
    ROLE_GUEST = 0
    ROLE_FUNKER = 1
    ROLE_LDF = 2
    ROLE_SICHTER = 3
    ROLE_S1 = 4
    ROLE_S2 = 5
    ROLE_S3 = 6
    ROLE_S4 = 7
    ROLE_S5 = 8
    ROLE_S6 = 9
    ROLE_LEITERFUEST = 10
    ROLE_FABE = 11
    ROLE_VERBP = 12
    ROLE_BEOBACHTER = 13

    def __init__(self):
        pass
    
    def login(self, usersign, userpw):
        #Diese Funktion muss nacher eine eindeutige ID für jeden Nutzer zurückgeben wenn der Login efolgreich war.
        #Wenn der Login fehlschlägt dann muss INVALID_USER_ID zurückgegeben werden. Kein Niutezr darf diese ID haben.
        if random.random() > 0.5:
            return 1
        else:
            return User.INVALID_USER_ID
    
    #Diese Funktion soll aus einem Usersign die eindeutige ID zurückgeben oder wenn nicht existiert INVALID_USER_ID
    def getId(self, usersign):
        if random.random() > 0.5:
            return 1
        else:
            return User.INVALID_USER_ID

    #gebe alle Daten zu einem Nutzer (außer das Passwort) als Dictionary zurück
    def getUserInfo(self, id):
        return {'id': id, 'usersign': "USn", 'userrole': User.ROLE_GUEST}
    
    #erstelle ein User Account und gebe die dazugehörige ID zurück, INVALID_USER_ID bei Fehler.
    def createUserAccount(self, usersign, userpw, userrole):
        return User.INVALID_USER_ID
    
    #Ändere die Rolle eines Nutzers, gebe True zurück wenn erfolgreich sonst False
    def changeUserrole(self, id, userrole):
        return True
    
    #Ändere das Passwort eines Nutzers wenn sein altes Passwort stimmt. Bei erfolg return True, sonst False
    def changePassword(self, id, oldpasswd, newpasswd):
        return True

    #Ändere das Passwort eines Nutzers als Manager (also ohne altes PW). Bei erfolg return True, sonst False
    def changePasswordManager(self, id, newpassword):
        return True
    
    #Rechte überprüfen:
    def canUserManageUsers(self, id):
        if random.random() > 0.5:
            return True
        else:
            return False

