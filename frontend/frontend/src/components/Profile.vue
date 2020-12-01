<template>
	<div>
		<button v-on:click="routeToHome" class="back-button">BACK</button>
		<div class="title">Profile</div>
		<div class="sub-title">Best Time</div>
		<div class="best-time">
			<div style="font-size: 50px; font-weight: bold">
				{{ this.$store.state.userBestTime }}
			</div>
		</div>
		<br />
		<div class="sub-title">Your Favourite Artists</div>
		<h3 v-if="artists.length == 0">No artists favourited yet</h3>
		<div v-else class="artist-container">
			<Artist
				v-for="artist in artists"
				:artistName="artist.name"
				:artistSummary="artist.summary"
				v-bind:key="artist.artistName"
			/>
		</div>
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
	methods: {
		routeToHome: function () {
			this.$router.push("/home");
		},
	},
};
</script>

<style scoped>
.title {
	font-size: 100px;
	font-weight: bold;
	color: #ffffff;
}
.sub-title {
	font-size: 30px;
	font-weight: bold;
	color: #ffffff;
}
.best-time {
	width: 300px;
	height: 100px;
	background-color: #ece281;
	font-size: 50px;
	font-weight: bold;
	color: #040563;
	margin: auto;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	border-radius: 10px;
}

.artist-container {
	height: 570px;
	overflow: scroll;
	background-color: #ece281;
	margin: 0px 10px 10px 10px;
	border-radius: 5px;
}

.savedArtists {
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
	border: 2px solid #84c078;
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
