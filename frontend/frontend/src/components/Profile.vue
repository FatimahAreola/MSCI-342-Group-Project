<template>
	<div>
		<h1>Profile</h1>
		<h2>Your Favourite Artists</h2>
		<Artist
			v-for="artist in artists"
			:artistName="artist.name"
			:artistSummary="artist.summary"
			v-bind:key="artist.artistName"
		/>
	</div>
</template>

<script>
import axios from "axios";
import Artist from "./Artist";
export default {
	components: {
		Artist,
	},
	data() {
		return {
			artists: [],
		};
	},
	mounted() {
		const baseURI = process.env.VUE_APP_HOST_URL + "api/artist/saved";
		const postData = { userID: this.$store.state.userId };
		axios.post(baseURI, postData).then((response) => {
			this.artists = response.data;
			console.log(this.artists);
		});
	},
};
</script>

<style scoped>
.card {
	width: 100%;
	height: 100%;
}

.card-info {
	height: 200px;
	width: 200px;
}
</style>
