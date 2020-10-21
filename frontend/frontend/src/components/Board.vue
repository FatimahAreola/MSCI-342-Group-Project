<template>
	<div class="board">
		<div class="card-slot" v-for="card in cardData" :key="card.card">
			<Card :card="card" />
		</div>
	</div>
</template>

<script>
import Card from "./Card.vue";

export default {
	components: {
		Card,
	},
	props: ["cardData"],
	data() {
		return {};
	},
};
</script>

<style>
.board {
	display: grid;
	grid-template-columns: repeat(4, 200px);
	padding: 10px;
}

.card-slot {
	margin: 5px;
	background-color: #f1d6d6;
	height: 200px;
}
</style>