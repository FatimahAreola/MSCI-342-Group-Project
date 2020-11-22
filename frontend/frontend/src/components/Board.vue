<template>
	<div>
		<div class="board">
			<div
				class="card-slot"
				v-for="card in cardData"
				:key="card.cardId"
				v-on:click="emitChange(card, $event)"
				:class="{ disabled: card.status }"
			>
				<Card :card="card" :active="card.active" :status="card.status" />
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
		return {};
	},
	methods: {
		emitChange(card) {
			this.$emit("updateactive", { value: card });
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

.disabled {
	pointer-events: none;
}
</style>