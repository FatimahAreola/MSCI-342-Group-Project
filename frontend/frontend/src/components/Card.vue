<template>
	<div>
		<div v-if="!active">{{ card.cardId }}</div>
		<div v-else>YO</div>
	</div>
</template>

<script>
export default {
	props: ["card", "active"],
};
</script>

<style scoped>
</style>