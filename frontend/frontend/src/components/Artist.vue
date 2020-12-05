<template>
	<div class="artist-slot">
		<div class="left-side">
			<div class="container">
				<h4>{{ artistName }}</h4>
				<img
					v-if="artistName == 'Auguste Edouart'"
					src="@/assets/AugusteEdouart.png"
				/>
				<img
					v-if="artistName == 'Vincent van Gogh'"
					src="@/assets/VincentVanGogh.png"
				/>
				<img
					v-if="artistName == 'Rembrandt (Rembrandt van Rijn)'"
					src="@/assets/Rembrandt (Rembrandt van Rijn).png"
				/>
				<img
					v-if="artistName == 'Paul Gauguin'"
					src="@/assets/PaulGauguin.png"
				/>
				<img
					v-if="artistName == 'Asher Brown Durand'"
					src="@/assets/AsherBrownDurand.png"
				/>
				<img
					v-if="artistName == 'Albert Bierstadt'"
					src="@/assets/AlbertBierstadt.png"
				/>
				<img
					v-if="artistName == 'Frederic Remington'"
					src="@/assets/FredericRemington.png"
				/>
				<img
					v-if="artistName == 'Paul Cézanne'"
					src="@/assets/PaulCezanne.png"
				/>
				<div class="overlay" @click="sendToGame">
					<div class="text">PLAY WITH {{ artistName }}</div>
				</div>
				<p>psst... hover over me!</p>
			</div>
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
	methods: {
		sendToGame() {
			this.$router.push({ path: "/game", query: { artist, selectDifficulty: maxTime} });
		},
	},
};
</script>

<style scoped>
h4 {
	margin: 5px 0px 5px 0px;
}

.container {
	position: relative;
	height: 100%;
}

img {
	border: 5px solid black;
}

.overlay {
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	height: 100%;
	width: 100%;
	opacity: 0;
	transition: 0.5s ease;
	background-color: #84c078;
	margin-top: -5px;
}

.container:hover .overlay {
	opacity: 0.95;
}

.text {
	color: white;
	font-size: 20px;
	font-weight: bold;
	position: absolute;
	top: 50%;
	left: 50%;
	-webkit-transform: translate(-50%, -50%);
	-ms-transform: translate(-50%, -50%);
	transform: translate(-50%, -50%);
	text-align: center;
}

.artist-slot {
	height: 315px;
	display: flex;
	flex-direction: row;
	background-color: rgb(251, 243, 216);
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