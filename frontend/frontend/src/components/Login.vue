<template>
	<div id="login" class="Login">
		<h1>Welcome to Art Match!</h1>
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
		<button class="create-button" @click="login">LOGIN</button>
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
					this.$store.commit("setUserIdForSession", result.data[0]);
					this.$store.commit("setCurrentUserBestTimeValue", result.data[1]);
					this.$router.push("/home");
				})
				.catch(() => {
					this.$notify({
						group: "foo",
						type: "error",
						title: "Invalid Username or Password",
						text: "The username or password you entered seems to be invalid.",
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
	width: 390px;
	margin-left: auto;
	margin-right: auto;
	padding-left: 10px;
	height: 30px;
	background-color: #f5e55b;
	border: 2px solid #1b1b1b;
	/* text */
	font-size: 20px;
	font-weight: bold;
	color: #f5e55b;
}

.create-button {
	/* button */
	width: 400px;
	height: 50px;
	border: 2px solid #f5e55b;
	background-color: #f5e55b;
	margin-left: auto;
	margin-right: auto;
	margin-top: 30px;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #ffffff;
	text-shadow: 2px 2px 4px #000000;
}

.create-button:hover {
	background-color: #f57575;
}
</style>