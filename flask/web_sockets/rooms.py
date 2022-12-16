from utils.globals import globals
from utils.message import Message
from flask_socketio import join_room, leave_room
from utils.auth_token import validated
from flask import request


@globals.socketio.on('join_room')
@validated
def on_join(data):
    username =  data['username']
    room_name = data['room_name']
    
    if username not in globals.users.keys():
        globals.users[username] = {"room_name": ""}
    globals.users[username]["room_name"] = room_name

    if room_name not in globals.rooms.keys():
        globals.rooms[room_name] = {"users": set()}
    globals.rooms[room_name]["users"].add(username)

    join_room(room_name)

    message = Message()
    message.send(username + ' has entered the game.', room=room_name)


@globals.socketio.on('leave_room')
@validated
def on_leave(data):
    username =  ['username']
    room_name = globals.users[username]["room_name"]

    globals.users.pop(username)
    if room_name not in globals.rooms.keys():
        globals.rooms[room_name] = {"users": set()}
    globals.rooms[room_name]["users"].remove(username)

    leave_room(room_name)

    message = Message()
    message.send(username + ' has left the game.', room=room_name)


@globals.socketio.on('direct_message')
@validated
def direct_message(data):
    message = Message()
    message.send(data["message"], room=data["username"])