<template>
	<div id="login" class="Login">
		<h1>Login</h1>
		<input
			class="input"
			type="text"
			id="username"
			name="username"
			v-model="input.username"
			placeholder="Username"
		/>
		<input
			class="input"
			type="password"
			id="password"
			name="password"
			v-model="input.password"
			placeholder="Password"
		/>
		<button class="create-button" @click="login">Login</button>
		<createAcc />
	</div>
</template>

<script>
import axios from "axios";
import createAcc from "./CreateAccount/CreateButton.vue";

export default {
	name: "Login",
	components: {
		createAcc,
	},
	data() {
		return {
			input: {
				username: "",
				password: "",
			},
		};
	},
	methods: {
		login() {
			console.log(this.input.username);
			if (!this.input.username || !this.input.password) {
				this.$notify({
					group: "foo",
					title: "Empty Username or Password",
					text: "Please enter both an username and a password.",
				});
				return;
			}
			let postData = {
				username: this.input.username,
				password: this.input.password,
			};
			const baseURI = process.env.VUE_APP_HOST_URL + "api/Login";
			axios
				.post(baseURI, postData)
				.then((result) => {
					this.$notify({
						group: "foo",
						type: "success",
						title: "Successful Login",
						text: "Sucessful Login",
					});
					this.$store.commit("setUserIdForSession", result.data);
					this.$router.push("/home");
				})
				.catch(() => {
					this.$notify({
						group: "foo",
						type: "error",
						title: "Invalid Username or Password",
						text: "The username or password you enetered seems to be invalid.",
					});
				});
		},
	},
};
</script>

<style>
.Login {
	display: flex;
	flex-direction: column;
}
.input {
	margin: 10px 20px 10px 20px;
	width: 300px;
	margin-left: auto;
	margin-right: auto;
	padding-left: 10px;
	height: 20px;
	background-color: transparent;
	border: 1px solid #1b1b1b;
}

.create-button {
	/* button */
	width: 300px;
	height: 40px;
	border: 2px solid #d282a6;
	background-color: #e794b9;
	margin-left: auto;
	margin-right: auto;
	margin-top: 30px;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #f8da6c;
	text-shadow: 2px 2px 4px #000000;
}

.create-button:hover {
	background-color: #d282a6;
}
</style>