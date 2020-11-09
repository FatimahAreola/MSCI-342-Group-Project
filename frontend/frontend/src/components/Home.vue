<template>
	<div class="home">
		<button v-on:click="test_axios">Test Access To Flask App</button>
		<br />
		<button v-on:click="routeToGame" class="play-button">PLAY</button>
		<br />
		<button v-on:click="routeToLogin" class="login-button">LOGIN</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "HelloWorld",
	components: {},
	data() {
		return {};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
	},
	methods: {
		routeToGame: function () {
			this.$router.push("/game");
		},
		routeToLogin: function () {
			this.$router.push("/login");
		},
		test_axios: function () {
			const baseURI = process.env.VUE_APP_HOST_URL+"api/hello";
			console.log(baseURI)
			axios
				.get(baseURI)
				.then((result) => {
					console.log(result);
				})
				.catch(function (error) {
					console.log(error);
				});
		},
	},
};
</script>

<style>
.home {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.play-button {
	/* button */
	width: 800px;
	height: 300px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 100px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}

.play-button:hover {
	background-color: #f8da6c;
}
.login-button {
	/* button */
	width: 800px;
	height: 300px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 100px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}
.login-button:hover {
	background-color: #f8da6c;
}
</style>
