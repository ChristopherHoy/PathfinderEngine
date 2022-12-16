from cryptography.fernet import Fernet
from utils.globals import globals
from utils.response import success, error
from datetime import datetime, timedelta
import json
from utils.db import connect as db
import bcrypt
from flask import request
from flask_socketio import emit


globals.new(
    key=Fernet.generate_key(), 
    token_duration = 30 * 60
)


def create_token(user_id: str) -> str:
    fernet = Fernet(globals.key)

    token = {
        "user_id": user_id,
        "valid_until": (datetime.now() + timedelta(minutes=globals.token_duration)).strftime("%d/%m/%Y, %H:%M:%S")
    }

    token = json.dumps(token)
    token = fernet.encrypt(token.encode()).decode()

    return token


def login(username: str, password: str) -> bool:
    conn = db()
    curr = conn.cursor(dictionary=True)

    sql = "SELECT id, password from pathfinder.user where username=%(username)s"
    curr.execute(sql, {"username": username})
    rows = curr.fetchall()

    for row in rows:
        if bcrypt.checkpw(password.encode(), row["password"].encode()):
            return create_token(row["id"])
        break
    return None


def decrypt_token(token: str) -> dict:
    fernet = Fernet(globals.key)    
    token = fernet.decrypt(token.encode()).decode()
    token = json.loads(token)
    return token


def token_valid(token: str) -> tuple[bool, str]:
    try: 
        token = decrypt_token(token)
        return True, token
    except Exception as e:
        return False, None


def refresh_token(token: str):
    valid, token =  token_valid(token)
    
    if valid:
        return create_token(token["user_id"])
    return None


def validated(func):
    def wrapper(*args, **kwargs):
        data = args[0]

        if data is None:
            return func(*args, **kwargs)

        # if "token" in data.keys():
        #     valid, token_data = token_valid(data["token"])
        #     if valid:
        #         emit("token", refresh_token(data["token"]), to=request.sid) # Update the token
        return func(*args, **kwargs) # Run the handler after performing token maintenance

        emit("token", "", to=request.sid) # Clear the token
        return error("Token is not provided or is invalid")
    return wrapper