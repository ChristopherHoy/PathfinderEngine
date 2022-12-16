const listeners = {
    connect: () => {
        console.log(socket.id);
        console.log(socket.connected);
    },

    disconnect: () => {
        console.log(socket.id);
        console.log(socket.connected);
    },

    message: (data) => {
        console.log(data.text);
    },

    data: () => {
        console.log(data.text);
    },

    error: (data) => {
        console.log(data.text);
    },

    token: (data) => {
        window.dispatchEvent(new CustomEvent('token', {
            detail: data
        }));
        console.log(data);
    }
}

export default {
    listen_to_socket(socket) {
        for (let [name, func] of Object.entries(listeners)) {
            socket.on(name, func)
        }
    }
    
}