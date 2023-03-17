import { defineStore } from 'pinia'

export default {
    useStore: defineStore('default', {
        state: () => (
            { 
                token: window.localStorage.getItem("token"), 
            }
        ),
        getters: {
          getToken: (state) => state.token,
        },
        actions: {
          setToken(token) {
            this.token = token
            window.localStorage.setItem("token", token)
          },
        },
      })
}