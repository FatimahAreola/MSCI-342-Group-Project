<template>
	<div class="home">
		<GlobalScore :topScores="topScores" />
		<br />
		<div id="v-model-radiobutton"  >
			<input
				type="radio"
				id="Easy"
				value="00:20:00"
				v-model="selectDifficulty"
			/>
			<label for="Easy">Easy</label>
			<input
				type="radio"
				id="Medium"
				value="00:03:00"
				v-model="selectDifficulty"
			/>
			<label for="Medium">Medium</label>
			<input
				type="radio"
				id="Hard"
				value="00:01:00"
				v-model="selectDifficulty"
				/>
			<label for="Hard">Hard</label>
		</div>
		<br /><br /><br />
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
		<br />
		<button v-on:click="logout" class="profile options">LOGOUT</button>
	</div>
</template>

<script>
import axios from "axios";
import GlobalScore from "./GlobalScore.vue";

export default {
	name: "HelloWorld",
	components: {
		GlobalScore,
	},
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

			selectDifficulty: "",
			topScores: [],
		};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
		this.getFavouritedArtists();
		this.getTopUserScores();
	},

	watch: {
		selectDifficulty() {
			this.$store.commit("setMaxTime", this.selectDifficulty);
			console.log(this.$store.state.maxTime);
		},
	},
	methods: {
		routeToGame: function () {
			this.$router.push({
				path: "/game",
				query: { artist: "random" },
			});
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
		getTopUserScores: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/topScores";
			axios.get(baseURI).then((response) => {
				this.topScores = response.data;
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
.radioButtons {
	display: flex;
	flex-direction: column;
	align-items: center;
	font-size: 20px;
	font-weight: bold;
	color: #FFFFFF;
}

.options {
	/* button */
	width: 350px;
	height: 45px;
	background-color: #ece281;
	/* text */
	font-size: 25px;
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
