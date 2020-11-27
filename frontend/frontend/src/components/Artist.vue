<template>
	<div class="artist-slot">
		<div class="left-side">
			<h4>{{ artistName }}</h4>
			<img
				style="width: 325px; height: 235px; object-fit: contain"
				:src="artistWork[0]"
			/>
		</div>
		<div class="right-side">
			<p>{{ artistSummary }}</p>
		</div>
	</div>
</template>

<script>
export default {
	props: ["artistName", "artistSummary", "artistWork"],
};
</script>

<style scoped>
h4 {
	margin: 5px 0px 2px 0px;
}
.artist-slot {
	height: 300px;
	display: flex;
	flex-direction: row;
	background-color: rgb(255, 255, 255);
	margin: 10px;
}

.left-side {
	width: 350px;
	margin-right: 10px;
}

.right-side {
	width: 1000px;
	height: 280px;
	overflow: scroll;
}
</style>