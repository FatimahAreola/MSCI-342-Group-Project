<template>
	<div class="create-wrapper">
		<h1>Create An Account</h1>
		<span class="feild-name">Enter Username:</span>
		<input
			class="input"
			type="text"
			id="username"
			name="username"
			v-model="username"
			placeholder="Ex. ArtLover123"
		/>
		<br />
		<span class="feild-name">Enter Password:</span>
		<input
			class="input"
			type="password"
			id="password"
			name="password"
			v-model="password1"
		/>
		<br />
		<span class="feild-name">Confirm Password:</span>
		<input
			class="input"
			type="password"
			id="password2"
			name="password2"
			v-model="password2"
		/>
		<button class="create-button" @click="createAcc">CREATE</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "CreateAccount",
	data() {
		return {
			username: "",
			password1: "",
			password2: "",
		};
	},
	methods: {
		createAcc() {
			if (this.username && this.password1 && this.password2) {
				let formData = {};
				if (this.password2 == this.password1) {
					formData = {
						username: this.username,
						password: this.password1,
					};
				} else {
					this.$notify({
						group: "foo",
						title: "Passwords Don't Match",
						text: "Please make sure you give the same password!",
					});
					return;
				}
				const baseURI = process.env.VUE_APP_HOST_URL + "api/createAccount";
				axios
					.post(baseURI, formData)
					.then(() => {
						this.$notify({
							group: "foo",
							type: "success",
							title: "Account created",
							text: "You're all set!",
						});
						this.$router.push("/");
					})
					.catch(() => {
						this.$notify({
							group: "foo",
							type: "error",
							title: "Username Already Exists",
							text: "Looks like that username has been taken!",
						});
					});
			} else {
				this.$notify({
					group: "foo",
					type: "warn",
					title: "Missing Information",
					text: "It looks like you're missing some account details!",
				});
			}
		},
	},
};
</script>

<style scoped>
.create-wrapper {
	margin: auto;
	margin-top: 20px;
	display: flex;
	flex-direction: column;
	width: 600px;
	height: 600px;
	background-color: #ece281;
	border: 2px solid #ece281;
	color: #040563;
}

.feild-name {
	text-align: left;
	padding-left: 20px;
	font-size: 30px;
	font-weight: bold;
	color: #040563;
}

.input {
	margin: 10px 20px 10px 20px;
	padding-left: 10px;
	height: 40px;
	width: 540px;
	background-color: transparent;
	border: 1px solid #000;
}

.create-button {
	/* button */
	width: 300px;
	height: 75px;
	background-color: #84c078;
	margin-left: auto;
	margin-right: auto;
	margin-top: 30px;
	/* text */
	font-size: 40px;
	font-weight: bold;
	color: #040563;
}

.create-button:hover {
	background-color: #f7e43c;
}
</style>
