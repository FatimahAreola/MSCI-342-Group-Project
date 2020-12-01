<template>
	<button class="create-button" @click="routeToCreateAccount">
		CREATE AN ACCOUNT
	</button>
</template>

<script>
export default {
	methods: {
		routeToCreateAccount() {
			this.$router.push("/createAccount");
		},
	},
};
</script>

<style scoped>
.create-button {
	/* button */
	width: 400px;
	height: 50px;
	background-color: #84c078;
	/* text */
	font-size: 30px;
	color: #040563;
}

.create-button:hover {
	background-color: #ece281;
}
</style>
