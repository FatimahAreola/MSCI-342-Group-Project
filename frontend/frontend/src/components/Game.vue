<template>
	<div class="board">
		<div class="summary">
		<h2> Matched: {{this.countMatched}}</h2>
			<button @click="routeToProfile">Stop Game</button>
			<button @click="returnHome">Home</button>
		</div>
		<div class="board-wrapper">
			<Board :cardData="shuffled" @updateActive="updateActive" />
		</div>
	</div>
</template>

<script>
import _ from "lodash";

import Board from "./Board.vue";

export default {
	name: "Game",
	components: {
		Board,
	},
	data() {
		return {
			cards: [
				{
					cardId: 1,
					artName: "art1",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 2,
					artName: "art2",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 3,
					artName: "art3",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 4,
					artName: "art4",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 5,
					artName: "art5",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 6,
					artName: "art6",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 7,
					artName: "art7",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 8,
					artName: "art8",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 9,
					artName: "art1",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 10,
					artName: "art2",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 11,
					artName: "art3",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 12,
					artName: "art4",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 13,
					artName: "art5",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 14,
					artName: "art6",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 15,
					artName: "art7",
					artUrl: "",
					active: false,
					status: false,
				},
				{
					cardId: 16,
					artName: "art8",
					artUrl: "",
					active: false,
					status: false,
				},
			],
			countMatched: 0,
			countFlipped: 0,
			flipped: [],
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
				this.routeToProfile(true);
			}
		},
		countFlipped() {
			if (this.countFlipped == 2) {
				setTimeout(() => {
					this.assertMatch();
				}, 300);
			}
		},
	},
	methods: {
		assertMatch() {
			if (this.flipped[0].artName == this.flipped[1].artName) {
				this.cards[this.flipped[0].cardId - 1].status = true;
				this.cards[this.flipped[1].cardId - 1].status = true;
				this.countMatched = this.countMatched + 1;
			} else {
				this.cards[this.flipped[0].cardId - 1].active = false;
				this.cards[this.flipped[1].cardId - 1].active = false;
			}
			this.countFlipped = 0;
			this.flipped = [];
		},
		returnHome() {
			this.$router.push("/");
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
		routeToProfile: function (gameWon=false) {
			this.$router.push({ name: 'GameSummary', params: { timer: '50', matches: this.countMatched, gameWon: gameWon } });
		},
		routeToHome: function () {
			this.$router.push('/');
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
	position: absolute;
	margin-left: 200px;
	margin-right: auto;
}

.board-wrapper {
	width: 825px;
	margin-left: 200px;
	height: 860px;
	background-color: #ffffff;
	border: 2px solid rgb(224, 224, 224);
	top: 20%;
}
</style>
