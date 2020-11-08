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
	height: 40px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 30px;
	color: #d282a6;
	text-shadow: 1px 1px 1px #000000;
}

.create-button:hover {
	background-color: #f8da6c;
}
</style>