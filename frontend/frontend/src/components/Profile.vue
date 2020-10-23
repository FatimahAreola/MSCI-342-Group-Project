<template>
	<div>
        <h2> Timer Stopped at </h2>
		<h3> {{this.$route.params.timer }} </h3>
		<h2> Number of Matches Achieved </h2>
		<h3> {{this.$route.params.matches }} </h3>

    </div>
</template>

<script>
export default {
	name: "Profile",
	data() {
		return {};
	},
	
	methods: {
		displayParams: function () {
            console.log("Hey")
			console.log(this.$route.params)
		},
	},		
};
</script>

<style scoped>
</style>
