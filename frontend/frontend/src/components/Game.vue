<template>
	<div>You are here
		<button v-on:click="routeToProfile">Stop Game</button>
	</div>
</template>

<script>
export default {
	name: "Game",
	data() {
		return {};
	},
	
	methods: {
		routeToProfile: function () {
			this.$router.push({ name: 'profile', params: { timer: '50', matches: 10 } });
		},
	},		
};
</script>

<style scoped>
</style>
