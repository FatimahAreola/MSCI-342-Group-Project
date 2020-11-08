<template>
    <div id="login">
        <h1>Login</h1>
        <input 
            type = "text"
            id = "username"
            name = "username"
            v-model = "input.username"
            placeholder = "Username"
        />
        <input
            type = "password"
            id = "password"
            name = "password" 
            v-model = "input.password"
            placeholder = "Password"
        />
        <button class="create-button" @click="login">Login</button>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: "",
                }
            };
        },
        methods: {
            login() {
                if(!this.input.username || !this.input.password) {
                    this.$notify({
                        group: "foo",
                        title: "Empty Username or Password",
                        text: "Please enter both an username and a password."
                    });
                    return;
                }
                if (this.input.username == this.$parent.testAccount.username && this.input.password == this.$parent.testAccount.password) {
                    const baseURI = "http://localhost:80/api/Login";
                    axios
                        .post(baseURI)
                        .then(() => {
                            this.$notify({
                                group: "foo",
                                type: "success",
                                title: "Successful Login",
                                text: "Sucessful Login",
                            });
                        })
                        .catch (() => {
                            this.$notify({
                                group: "foo",
                                type: "error",
                                title: "Invalid Username or Password",
                                text: "The username or password you enetered seems to be invalid."
                            });
                });
            }
        },
    }
    };
</script>

<style>

</style>