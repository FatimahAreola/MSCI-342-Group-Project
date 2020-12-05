<template>
	<div class="gameSummary">
		<h2>
			{{
				this.$route.params.gameWon == true
					? "Congratulations"
					: "Better Luck Next Time!"
			}}
		</h2>
		<h3>Total Game Play Time: {{ this.$store.state.timer }}</h3>
		<h3>Best Game Play Time: {{ bestTime }}</h3>
		<h3>Match Count: {{ this.$route.params.matches }}</h3>
		<h3>Artists in Game</h3>
		<SavedArtist
			v-for="name in artistNames"
			:artistName="name"
			v-bind:key="name"
		/>
		<br /><br />
		<button class="homeButton" v-on:click="routeToHome">HOME</button>
	</div>
</template>

<script>
import SavedArtist from "./SavedArtist";
import axios from "axios";

export default {
	components: {
		SavedArtist,
	},
	name: "GameSummary",
	data() {
		return {
			artistNames: this.artistsList(),
			favouritedArtists: this.$store.state.favouritedArtists,
		};
	},
	computed: {
		isWon() {
			if (this.$route.params.matches == 8) {
				return true;
			} else {
				return false;
			}
		},
		bestTime() {
			if (this.isWon) {
				if (this.$store.state.userBestTime == "00:00:00") {
					this.$store.commit(
						"setCurrentUserBestTimeValue",
						this.$store.state.timer
					);
					// send new best time to database
					this.updateBestTime();
					return this.$store.state.timer;
				}
				if (this.$store.state.timer < this.$store.state.userBestTime) {
					this.$store.commit(
						"setCurrentUserBestTimeValue",
						this.$store.state.timer
					);
					// send new best time to database
					this.updateBestTime();
					return this.$store.state.timer;
				} else {
					return this.$store.state.userBestTime;
				}
			} else {
				if (this.$store.state.userBestTime == "00:00:00") {
					return "None";
				}
				return this.$store.state.userBestTime;
			}
		},
	},
	methods: {
		artistsList: function () {
			var artistNames = [];
			var cardSet = this.$route.params.cardSet;
			cardSet.forEach((card) => {
				artistNames.push(card.artistName);
			});
			const uniq_artist_names = [...new Set(artistNames)];
			var filtered = uniq_artist_names.filter(function (el) {
				return el != null;
			});
			return filtered;
		},
		routeToHome: function () {
			this.$router.push("/home");
		},
		updateBestTime() {
			let formData = {
				userId: this.$store.state.userId,
				bestTime: this.$store.state.timer,
			};
			alert("will update best time", this.$store.state.timer);
			const baseURI = process.env.VUE_APP_HOST_URL + "api/updateBestTime";
			axios
				.post(baseURI, formData)
				.then(() => {})
				.catch(() => {});
		},
	},
};
</script>

<style scoped>
.gameSummary {
	display: flex;
	flex-direction: column;
	/* text */
	font-size: 20px;
	font-weight: bold;
	color: #ffffff;
}
.homeButton {
	/* button */
	margin-left: auto;
	margin-right: auto;
	width: 150px;
	height: 60px;
	background-color: #ece281;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #040563;
}
.homeButton:hover {
	background-color: #84c078;
}
</style>
