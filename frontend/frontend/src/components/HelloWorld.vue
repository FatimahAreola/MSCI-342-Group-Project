<template>
	<div class="hello">
		<h1>{{ msg }}</h1>
		<p>
			For a guide and recipes on how to configure / customize this project,<br />
			check out the BQALHXSCWE
			<a href="https://cli.vuejs.org" target="_blank" rel="noopener"
				>vue-cli documentation</a
			>.
		</p>
		<button v-on:click="test_axios">Test Access To Flask App</button>
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
