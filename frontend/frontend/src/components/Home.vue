<template>
	<div class="home">
		<button v-on:click="test_axios">Test Access To Flask App</button>
		<br />
		<button v-on:click="routeToGame" class="play-button options">
			RANDOM PLAY
		</button>
		<button v-on:click="selectArtist" class="play-button options">
			ARTIST PLAY
		</button>
		<p></p>
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
	border: 2px solid #f5e55b;
	background-color: #f5e55b;
	/* text */
	font-size: 50px;
	font-weight: bold;
	color: #ffffff;
	text-shadow: 2px 2px 4px #000000;
}
.options:hover {
	background-color: #f57575;
}
.play-button:hover {
	background-color: #f57575;
}
.artist-button {
	/* button */
	width: 800px;
	height: 45px;
	border: 2px solid #f5e55b;
	background-color: #f5e55b;
	/* text */
	font-size: 25px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 1px 1px 2px #000000;
}
.artist-button:hover {
	background-color: #f57575;
}
</style>
