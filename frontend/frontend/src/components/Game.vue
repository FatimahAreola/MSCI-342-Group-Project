<template>
	<div class="board">
		<div class="summary">
			<h2>Matched: {{ this.countMatched }}</h2>
			<Timer :state="timerState" />
			<br />
			<button class="summaryButton" @click="stopGame">STOP GAME</button>
			<button class="summaryButton" @click="returnHome">HOME</button>
		</div>
		<div class="board-wrapper">
			<Board :cardData="shuffled" @updateActive="updateActive" />
		</div>
		<Match
			ref="match"
			v-show="showMatchModal"
			:flipped="flipped"
			@close="completeMatch"
		/>
	</div>
</template>

<script>
import _ from "lodash";
import axios from "axios";
import Board from "./Board.vue";
import Timer from "./Timer.vue";

import Match from "./MatchPopup.vue";

export default {
	name: "Game",
	components: {
		Board,
		Match,
		Timer,
	},
	mounted() {
		let artist = this.$route.query.artist;

		let data = {
			selectedArtist: artist,
		};

		axios.post("/api/MetAPI", data).then((response) => {
			this.cards = response.data;
		});
	},
	data() {
		return {
			timerState: "running",
			cards: [],
			countMatched: 0,
			countFlipped: 0,
			flipped: [],
			showMatchModal: false,
		};
	},
	computed: {
		shuffled() {
			return _.shuffle(this.cards);
		},
	},
	watch: {
		countMatched() {
			if (this.countMatched >= this.cards.length / 2) {
				this.stopGame(true);
			}
		},
		countFlipped() {
			if (this.countFlipped == 2) {
				this.showMatchModal = true;
				this.timerState = "stopped";
			}
		},
	},
	methods: {
		completeMatch({ value }) {
			this.showMatchModal = false;
			if (value) {
				this.cards[this.flipped[0].cardId - 1].status = true;
				this.cards[this.flipped[1].cardId - 1].status = true;
				this.countMatched = this.countMatched + 1;
			} else {
				this.cards[this.flipped[0].cardId - 1].active = false;
				this.cards[this.flipped[1].cardId - 1].active = false;
			}
			this.countFlipped = 0;
			this.flipped = [];
			this.timerState = "run";
		},
		returnHome() {
			this.$router.push("/home");
		},
		updateActive({ value }) {
			this.cards.forEach((card) => {
				if (card.cardId == value.cardId) {
					if (card.active) {
						this.countFlipped = this.countFlipped - 1;
						this.flipped = this.flipped.filter(
							(item) => item.cardId != value.cardId
						);
					} else {
						this.countFlipped = this.countFlipped + 1;
						this.flipped.push(value);
					}
					card.active = !card.active;
				}
			});
		},
		setTimerState() {
			this.timerState = "stopped";
		},
		async stopGame(gameWon = false) {
			await this.setTimerState();
			await this.$router.push({
				name: "GameSummary",
				params: {
					matches: this.countMatched,
					gameWon: gameWon,
					cardSet: this.cards,
				},
			});
		},
		routeToHome: function () {
			this.$router.push("/home");
		},
	},
};
</script>

<style scoped>
.board {
	height: 100%;
	display: flex;
	align-content: space-between;
}

.timer {
	width: 200px;
	height: 70px;
}

.summary {
	margin-left: 200px;
	/* text */
	font-size: 20px;
	font-weight: bold;
	color: #ffffff;
}

.board-wrapper {
	width: 825px;
	margin-left: 200px;
	height: 860px;
	background-color: #ffffff;
	border: 2px solid rgb(224, 224, 224);
	top: 20%;
}

.summaryButton {
	/* button */
	width: 200px;
	margin-top: 10px;
	display: block;
	height: 75px;
	background-color: #ece281;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #040563;
}
.summaryButton:hover {
	background-color: #84c078;
}
</style>
