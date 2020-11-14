<template>
	<div>
		<h2> {{this.$route.params.gameWon==true? "Congratulations": "Better Luck Next Time!"  }}</h2>
		<h3> Total Game Play Time: {{this.$store.state.timer }} </h3>
		<h3> Match Count: {{ this.$route.params.matches }} </h3>
		<h3> Artists in Game: {{this.$oute.ArtistName}} </h3>
		<button class="homeButton" v-on:click="routeToHome">Home</button>

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
			this.$router.push('/home');
		},
	}

};	
</script>

<style scoped>
.homeButton {
	/* button */
	width: 150px;
	height: 60px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}
</style>
