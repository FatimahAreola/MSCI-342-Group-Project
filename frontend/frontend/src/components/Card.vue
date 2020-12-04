<template>
	<div class="card">
		<div v-if="!active"></div>
		<div v-else-if="status">
			<img style="height: 200px; width: 190px" :src="card.artUrl" />
		</div>
		<div v-else class="card-info">
			<img style="height: 200px; width: 190px" :src="card.artUrl" />
		</div>
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
	height: 200px;
	width: 200px;
}
</style>
