<template>
	<div class="artist-slot">
		<div class="left-side">
			<h4>{{ artistName }}</h4>
			<img
				v-if="artistName == 'Auguste Edouart'"
				src="@/assets/AugusteEdouart.png"
			/>
			<img
				v-if="artistName == 'Vincent Van Gogh'"
				src="@/assets/VincentVanGogh.png"
			/>
			<img v-if="artistName == 'Rembrandt'" src="@/assets/Rembrandt.png" />
			<img v-if="artistName == 'Paul Gauguin'" src="@/assets/PaulGauguin.png" />
			<img
				v-if="artistName == 'Asher Brown Durand'"
				src="@/assets/AsherBrownDurand.png"
			/>
			<img
				v-if="artistName == 'Albert Bierstadt'"
				src="@/assets/AugusteEdouart.png"
			/>
			<img
				v-if="artistName == 'Frederic Remington'"
				src="@/assets/FredericRemington.png"
			/>
			<img v-if="artistName == 'Paul Cézanne'" src="@/assets/PaulCezanne.png" />
		</div>
		<div class="right-side">
			<p>{{ artistSummary }}</p>
		</div>
	</div>
</template>

<script>
export default {
	props: ["artistName", "artistSummary"],
	computed: {
		artLink() {
			if (this.artistName == "Auguste Edouart") {
				return "@/assets/AugusteEdouart.png";
			} else {
				return "@/assets/AugusteEdouart.png";
			}
		},
	},
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
	width: 25%;
	margin-right: 10px;
}

.right-side {
	width: 70%;
	height: 280px;
	overflow: scroll;
}
</style>