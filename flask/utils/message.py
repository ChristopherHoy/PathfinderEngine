from flask import request
from flask_socketio import emit
from utils.globals import globals
from utils.auth_token import refresh_token

class Message:
    def __init__(self) -> None:
        self.from_sid = request.sid

    def send(self, message: str, room=None, user=None):
        if room is not None and room in globals.rooms.keys():
            to = room
        elif user is not None and user in globals.users.keys():
            to = globals.users[user]["sid"]
        else:
            emit("error", {
                "text": "Failed to send messagem user / room not specified"
            }, to=request.sid)
            return

        emit("message", {
            "text": message,
            }, to=to
        )


        
        