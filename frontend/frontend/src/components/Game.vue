<template>
	<div class="board">
		<div class="board-wrapper">
			<Board :cardData="cards" />
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
		return {};
	},
	computed: {
		cards() {
			return [
				{ cardId: 1, artName: "art1", artUrl: "" },
				{ cardId: 2, artName: "art2", artUrl: "" },
				{ cardId: 3, artName: "art3", artUrl: "" },
				{ cardId: 4, artName: "art4", artUrl: "" },
				{ cardId: 5, artName: "art5", artUrl: "" },
				{ cardId: 6, artName: "art6", artUrl: "" },
				{ cardId: 7, artName: "art7", artUrl: "" },
				{ cardId: 8, artName: "art8", artUrl: "" },
				{ cardId: 9, artName: "art9", artUrl: "" },
				{ cardId: 10, artName: "art10", artUrl: "" },
				{ cardId: 11, artName: "art11", artUrl: "" },
				{ cardId: 12, artName: "art12", artUrl: "" },
				{ cardId: 13, artName: "art13", artUrl: "" },
				{ cardId: 14, artName: "art14", artUrl: "" },
				{ cardId: 15, artName: "art15", artUrl: "" },
				{ cardId: 16, artName: "art16", artUrl: "" },
			];
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
