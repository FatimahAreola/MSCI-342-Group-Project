<template>
	<div class="card">
		<div v-if="!active"></div>
		<div v-else-if="status">matched!</div>
		<div v-else class="card-info">{{ card.cardId }} {{ card.artName }}</div>
	</div>
</template>

<script>
export default {
	props: ["card", "active", "status"],
};
</script>

<style scoped>
.card {
	width: 100%;
	height: 100%;
}

.card-info {
	padding-top: 50%;
}
</style>