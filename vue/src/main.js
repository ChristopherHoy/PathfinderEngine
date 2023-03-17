import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { io } from "socket.io-client";
import router from "./routes";
import { createPinia } from 'pinia'
import store from "./store"

const socket = io("http://localhost:5000");
window.socket = socket;

import emitters from "./sockets"
emitters.register(socket)
window.emitters = emitters
window.router = router

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)
app.mount('#app')

window.store = store.useStore()