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
		<div id="v-model-radiobutton">
			<input
				type="radio"
				id="Easy"
				value="20:00:00"
				v-model="selectDifficulty"
			/>
			<label for="Easy">Easy</label>
			<input
				type="radio"
				id="Medium"
				value="03:00:00"
				v-model="selectDifficulty"
			/>
			<label for="Medium">Medium</label>
			<input
				type="radio"
				id="Challenging"
				value="01:00:00"
				v-model="selectDifficulty"
			/>
			<label for="Challenging">Challenging</label>
		</div>
		<br /><br /><br />
		<button v-on:click="routeToProfile" class="profile options">
			MY PROFILE
		</button>
		<br />
		<button v-on:click="logout" class="profile options">
			LOGOUT
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

			selectDifficulty: ''
		};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
		this.getFavouritedArtists();
	},

	watch: {
		selectDifficulty() {
			this.$store.commit("setMaxTime", this.selectDifficulty);
			console.log(this.$store.state.maxTime);
		},
	},
	methods: {
		routeToGame: function () {
			this.$router.push({ path: "/game", query: { artist: "random" });
		},
		selectArtist: function () {
			this.$router.push({ path: "/selectArtist" });
		},
		routeToProfile: function () {
			this.$router.push({ path: "/profile" });
		},
		logout: function () {
			this.$router.push("/");
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
