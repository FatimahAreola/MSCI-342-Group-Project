<template>
	<div class="home">
		<br />
		<button v-on:click="routeToGame" class="play-button options">
			RANDOM PLAY
		</button>
		<br />
		<button v-on:click="selectArtist" class="play-button options">
			ARTIST PLAY
		</button>
		<br /><br /><br />
		<button v-on:click="routeToProfile" class="profile options">
			MY PROFILE
		</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "HelloWorld",
	components: {},
	data() {
		return {
			artist: [
				"Paul Gauguin",
				"Vincent van Gogh",
				"Rembrandt",
				"Asher Brown Durand",
				"Albert Bierstadt",
				"Paul Cézanne",
				"Auguste Edouart",
				"Frederic Remington",
			],
		};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
		this.getFavouritedArtists();
	},
	methods: {
		routeToGame: function () {
			this.$router.push("/game");
		},
		selectArtist: function () {
			this.$router.push("/selectArtist");
		},
		routeToProfile: function () {
			this.$router.push("/profile");
		},
		test_axios: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/hello";
			axios
				.get(baseURI)
				.then((result) => {
					console.log(result);
				})
				.catch(function (error) {
					console.log(error);
				});
		},
		getFavouritedArtists: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/artist/saved";
			const postData = { userID: this.$store.state.userId };
			axios.post(baseURI, postData).then((response) => {
				this.$store.commit("setFavouritedArtists", response.data);
			});
		},
	},
};
</script>

<style scoped>
.home {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.options {
	/* button */
	width: 800px;
	height: 100px;
	background-color: #ece281;
	/* text */
	font-size: 50px;
	font-weight: bold;
	color: #040563;
}
.options:hover {
	background-color: #84c078;
}
.play-button:hover {
	background-color: #84c078;
}
</style>
