<template>
    <div class="flex items-center w-full mt-24">
        <div class="flex-grow"></div>
        <div class="bg-sky-100 rounded-md">
            <div class="flex items-center py-8">
                <div class="flex-grow"></div>
                <p class="text-xl font-bold">Welcome!</p>
                <div class="flex-grow"></div>
            </div>
            <div class="flex items-center">
                <div class="flex-grow"></div>
                <div class="py-4 px-8">
                    <div class="mb-2">
                        <TextField label="Username" v-model:value="username" />
                    </div>
                    <div class="mb-2">
                        <TextField label="Password" :password="true" v-model:value="password" />
                    </div>
                    <div class="flex items-center pt-4">
                        <div class="flex-grow"></div>

                        <button
                            class="bg-sky-500 text-white p-2 rounded-md border-none shadow-sm text-sm"
                            @click.prevent="submit"
                        >
                            Log In
                        </button>
                        <button
                            class="bg-indigo-500 text-white p-2 rounded-md border-none shadow-sm text-sm ml-2"
                            @click.prevent="sign_up"
                        >
                            Sign Up
                        </button>
                    </div>
                </div>
                <div class="flex-grow"></div>
            </div>
        </div>
        <div class="flex-grow"></div>
    </div>
</template>

<script>
import TextField from "../components/Form/TextField.vue";
import Form from "../components/Form/Form.vue";
export default {
    name: "Login",

    components: { TextField, Form },

    props: {},

    data: function data() {
        return {
            username: "",
            password: "",
        };
    },

    mounted() {
        window.addEventListener("token", this.token_received);
    },

    methods: {
        submit() {
            emitters.login.emit(this.username, this.password);
        },

        token_received(data) {
            this.$router.push("Home");
        },

        sign_up() {},
    },

    beforeUnmount() {
        window.removeEventListener("token", this.token_received);
    },
};
</script>
