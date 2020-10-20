<template>
	<div class="home">
		<button v-on:click="test_axios">Test Access To Flask App</button>
		<br />
		<button v-on:click="routeToGame">go to game</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "HelloWorld",
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
			console.log("yo");
			this.$router.push("/game");
		},
		test_axios: function () {
			console.log("Hey how are you");
			const baseURI = "http://localhost:80/api/hello";
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
	margin: 40px 0 0;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}
</style>
