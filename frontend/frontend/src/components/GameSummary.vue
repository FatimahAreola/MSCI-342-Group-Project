<template>
	<div>
		<h2> {{this.$route.params.gameWon==true? "Congratulations": "Better Luck Next Time!"  }}</h2>
		<h3> Time Stopped at: {{this.$route.params.timer }} </h3>
		<h3> Match Count: {{ this.$route.params.matches }} </h3>
		<button v-on:click="routeToHome">Home</button>

    </div>
</template>

<script>
export default {
	name: "GameSummary",
	data() {
		return {};
	},
	methods: {
		routeToHome: function () {
			this.$router.push('/');
		},
	}

};	
</script>

<style scoped>
</style>
