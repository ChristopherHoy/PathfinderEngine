class Emitter {
    socket = null;

    callback = function () {
        console.log("Callback does not exist for this emitter")
    }

    set_callback(callback) {
        this.callback = callback
    }

    register_socket(socket) {
        this.socket = socket
    }

    emit(...args) {
        this.callback(...args)   
    }
}

var join_room = new Emitter()
join_room.callback = function (...args) {
    join_room.socket.emit("join_room", {
        room_name: args[0],
        username: args[1]
    });
}

var leave_room = new Emitter()
leave_room.callback = function () {
    leave_room.socket.emit("leave_room", {
        username: args[0]
    });
}

var login = new Emitter()
login.callback = function (...args) {
    login.socket.emit("login", {
        username: args[0],
        password: args[1]
    });
}


export default {
    join_room,
    leave_room,
    login
}
