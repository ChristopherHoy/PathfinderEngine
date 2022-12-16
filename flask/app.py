from flask import Flask
from flask_socketio import SocketIO
from utils.globals import globals

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

globals.new(users={}, rooms={}, socketio=socketio)

# Import websocket handlers
from web_sockets import auth, rooms, character

@socketio.on('connect')
def connect(data):
   return

if __name__ == '__main__':
    socketio.run(app, debug=True)