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
	border: 2px solid #f57575;
	background-color: #f57575;
	/* text */
	font-size: 30px;
	color: #ffffff;
	text-shadow: 2px 2px 4px #000000;
}

.create-button:hover {
	background-color: #f8da6c;
}
</style>