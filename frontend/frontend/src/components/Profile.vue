<template>
	<div>
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
.back-button {
	position: absolute;
	left: 10px;
	top: 10px;
	/* button */
	margin-top: 2px;
	width: 200px;
	height: 75px;
	border: 2px solid #f5e55b;
	background-color: #f5e55b;
	/* text */
	font-size: 35px;
	font-weight: bold;
	color: #cf4985;
}
.back-button:hover {
	background-color: #f8da6c;
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
