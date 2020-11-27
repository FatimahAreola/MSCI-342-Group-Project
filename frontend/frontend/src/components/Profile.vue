<template>
	<div>
		<button v-on:click="routeToHome" class="back-button">HOME</button>
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
}
.sub-title {
	font-size: 40px;
}
.best-time {
	width: 300px;
	height: 100px;
	background-color: rgba(255, 238, 0, 0.938);
	margin: auto;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	border-radius: 10px;
}

.artist-container {
	height: 570px;
	overflow: scroll;
	background-color: #dddddd;
	margin: 0px 10px 10px 10px;
	border-radius: 5px;
}

.back-button {
	position: absolute;
	left: 10px;
	top: 10px;
	/* button */
	margin-top: 2px;
	width: 200px;
	height: 50px;
	border: 2px solid rgba(255, 238, 0, 0.938);
	background-color: rgba(255, 238, 0, 0.938);
	border-radius: 10px;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #cf4985;
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
