<template>
	<div>
		<Board :cardData="cards" />
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
				{ card: 1 },
				{ card: 2 },
				{ card: 3 },
				{ card: 4 },
				{ card: 5 },
				{ card: 6 },
				{ card: 7 },
				{ card: 8 },
				{ card: 9 },
				{ card: 10 },
				{ card: 11 },
				{ card: 12 },
				{ card: 13 },
				{ card: 14 },
				{ card: 15 },
				{ card: 16 },
			];
		},
	},
};
</script>

<style scoped>
</style>
