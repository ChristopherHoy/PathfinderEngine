
import listen from "./listeners"
import emitters from "./emitters"

export default {
    register(socket) {
        listen.listen_to_socket(socket)
        for (let [name, emitter] of Object.entries(emitters)) {
            emitter.register_socket(socket)
            this[name] = emitter
        }
    }
}
