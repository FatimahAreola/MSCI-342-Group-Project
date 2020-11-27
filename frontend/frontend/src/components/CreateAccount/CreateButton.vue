<template>
	<button class="create-button" @click="routeToCreateAccount">
		Create an Account
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
	width: 300px;
	height: 50px;
	border: 2px solid #f5e55b;
	background-color: #f5e55b;
	/* text */
	font-size: 30px;
	color: #f75151;
	text-shadow: 1px 1px 1px #000000;
}

.create-button:hover {
	background-color: #f8da6c;
}
</style>