<template>
	<div>
		<h3>Top Players</h3>
		<table class="scoreBoard">
			<tr>
				<th>Place</th>
				<th>Username</th>
				<th>Time</th>
			</tr>
			<tr v-for="topScore in topScores" v-bind:key="topScore.userID">
				<th>{{ topScore.place }}</th>
				<th>{{ topScore.userName }}</th>
				<th>{{ topScore.time }}</th>
			</tr>
		</table>
	</div>
</template>

<script>
export default {
	props: ["topScores"],
};
</script>
<style scoped>
h3 {
	margin: 0 auto;
}
.scoreBoard {
	height: 150px;
	width: 400px;
	font-size: 20px;
	background-color: #ece281;
	margin: 5px;
	border-collapse: collapse;
	color: #040563;
}

tr {
	border-bottom: 1px solid #040563;
	border-top: 1px solid #040563;
}
</style>