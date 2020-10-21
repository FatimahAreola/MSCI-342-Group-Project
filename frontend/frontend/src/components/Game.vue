<template>
	<div class="board">
		<div class="board-wrapper">
			<Board :cardData="cards" @updateActive="updateActive" />
		</div>
		<div class="timer">timer</div>
	</div>
</template>

<script>
import Board from "./Board.vue";

export default {
	name: "Game",
	components: {
		Board,
	},
	data() {
		return {
			cards: [
				{ cardId: 1, artName: "art1", artUrl: "", active: false },
				{ cardId: 2, artName: "art2", artUrl: "", active: false },
				{ cardId: 3, artName: "art3", artUrl: "", active: false },
				{ cardId: 4, artName: "art4", artUrl: "", active: false },
				{ cardId: 5, artName: "art5", artUrl: "", active: false },
				{ cardId: 6, artName: "art6", artUrl: "", active: false },
				{ cardId: 7, artName: "art7", artUrl: "", active: false },
				{ cardId: 8, artName: "art8", artUrl: "", active: false },
				{ cardId: 9, artName: "art9", artUrl: "", active: false },
				{ cardId: 10, artName: "art10", artUrl: "", active: false },
				{ cardId: 11, artName: "art11", artUrl: "", active: false },
				{ cardId: 12, artName: "art12", artUrl: "", active: false },
				{ cardId: 13, artName: "art13", artUrl: "", active: false },
				{ cardId: 14, artName: "art14", artUrl: "", active: false },
				{ cardId: 15, artName: "art15", artUrl: "", active: false },
				{ cardId: 16, artName: "art16", artUrl: "", active: false },
			],
		};
	},
	computed: {},
	methods: {
		updateActive({ value }) {
			this.cards.forEach((card) => {
				if (card.cardId == value) {
					card.active = !card.active;
				}
			});
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

.board-wrapper {
	width: 825px;
	height: 860px;
	background-color: #ffffff;
	border: 2px solid rgb(224, 224, 224);
}
</style>
