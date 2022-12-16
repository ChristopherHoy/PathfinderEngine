import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { io } from "socket.io-client";
import router from "./routes";

const socket = io("http://localhost:5000");
socket.

window.socket = socket;

import emitters from "./sockets"
emitters.register(socket)
window.emitters = emitters
window.router = router

const app = createApp(App)

app.use(router)

app.mount('#app')