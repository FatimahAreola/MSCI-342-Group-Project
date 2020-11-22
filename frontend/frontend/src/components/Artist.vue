<template>
	<div>
		<h4>{{ artistName }}</h4>
		<p>{{ artistSummary }}</p>
	</div>
</template>

<script>
export default {
	props: ["artistName", "artistSummary"],
};
</script>

<style scoped>
</style>