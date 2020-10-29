<template>
	<div class="create-wrapper">
		<br /><br />
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
		<button class="create-button" @click="createAcc">Create</button>
	</div>
</template>

<script>
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
			console.log(this.username, this.password1, this.password2);
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
	width: 500px;
	height: 600px;
	background-color: #fae59a;
	border: 2px solid #f8da6c;
}

.feild-name {
	text-align: left;
	padding-left: 20px;
	font-size: 30px;
	font-weight: bold;
}

.input {
	margin: 10px 20px 10px 20px;
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