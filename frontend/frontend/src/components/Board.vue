<template>
	<div>
		<div class="board">
			<div
				class="card-slot"
				v-for="card in cardData"
				:key="card.cardId"
				v-on:click="emitChange(card.cardId, $event)"
			>
				<Card :card="card" :active="isActive[card.cardId - 1]" />
			</div>
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
		return {
			isActive: [
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
				false,
			],
		};
	},
	methods: {
		emitChange(id) {
			console.log(id);
			this.isActive[id - 1] = true;
		},
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
	align-content: center;
	text-align: center;
}
</style>