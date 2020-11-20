<template>
	<div>
		<h2>
			{{
				this.$route.params.gameWon == true
					? "Congratulations"
					: "Better Luck Next Time!"
			}}
		</h2>
		<h3>Total Game Play Time: {{ this.$store.state.timer }}</h3>
		<SavedArtist
			v-for="name in artistNames"
			:artistName="name"
			v-bind:key="name"
		/>
		<h3>Best Game Play Time: {{ bestTime }}</h3>
		<h3>Match Count: {{ this.$route.params.matches }}</h3>
		<button class="homeButton" v-on:click="routeToHome">Home</button>
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
	mounted() {
		console.log(this.artistsList());
	},
	data() {
		return {
			artistNames: this.artistsList(),
			savedArtists: [],
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
		routeToHome: function () {
			this.$router.push("/home");
		},
		updateBestTime() {
			let formData = {
				userId: this.$store.state.userId,
				bestTime: this.$store.state.timer,
			};
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
.homeButton {
	/* button */
	width: 150px;
	height: 60px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}
</style>
