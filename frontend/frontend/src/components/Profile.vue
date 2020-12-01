<template>
	<div class="savedArtists">
		<button v-on:click="routeToHome" class="back-button">BACK</button>
		<h1>Profile</h1>
		<h2>Your Favourite Artists</h2>
		<h3 v-if="artists.length == 0">No artists favourited yet</h3>
		<Artist
			v-for="artist in artists"
			:artistName="artist.name"
			:artistSummary="artist.summary"
			v-bind:key="artist.artistName"
		/>
	</div>
</template>

<script>
import Artist from "./Artist";
export default {
	components: {
		Artist,
	},
	data() {
		return {
			artists: this.$store.state.favouritedArtists,
		};
	},
	mounted() {},
	methods: {
		routeToHome: function () {
			this.$router.push("/home");
		},
	},
};
</script>

<style scoped>
.savedArtists{
	display: flex;
	flex-direction: column;
	/* text */
	font-size: 20px;
	font-weight: bold;
	color: #ffffff;	
}
.back-button {
	position: absolute;
	left: 10px;
	top: 10px;
	/* button */
	margin-top: 2px;
	width: 200px;
	height: 75px;
	background-color: #ece281;
	/* text */
	font-size: 40px;
	font-weight: bold;
	color: #040563;
}
.back-button:hover {
	background-color: #84c078;
}
.card {
	width: 100%;
	height: 100%;
}

.card-info {
	height: 200px;
	width: 200px;
}
</style>
