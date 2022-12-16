from utils.globals import globals
from flask_socketio import emit
from utils.auth_token import token_valid, login as token_login, validated
from utils.response import error, success
from flask import request


@globals.socketio.on('login')
def login(data):
    username = data.get("username")
    password = data.get("password")

    if username is not None and password is not None:
        token = token_login(username, password)
        if token is not None:
            return success(token)
    return error("Invalid username or password")
        
    


@globals.socketio.on('refresh_token')
@validated
def refresh_token(data):
    pass # We do nothing here, it is all handled by the wrapper