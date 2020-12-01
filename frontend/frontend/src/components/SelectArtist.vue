<template>
	<div class="selectArtist">
        <br />
		<button v-on:click="routeToHome" class="back-button">BACK</button>
		<h1>Select An Artist To Play</h1>
		<button
			v-on:click="selectArtist(artist[0], $event)"
			value="Paul Gauguin"
			class="artist-button"
		>
			Paul Gauguin
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[1], $event)"
			value="Vincent van Gogh"
			class="artist-button"
		>
			Vincent van Gogh
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[2], $event)"
			value="Rembrandt"
			class="artist-button"
		>
			Rembrandt
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[3], $event)"
			value="Asher Brown Durand"
			class="artist-button"
		>
			Asher Brown Durand
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[4], $event)"
			value="Albert Bierstadt"
			class="artist-button"
		>
			Albert Bierstadt
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[5], $event)"
			value="Paul Cézanne"
			class="artist-button"
		>
			Paul Cézanne
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[6], $event)"
			value="Auguste Edouart"
			class="artist-button"
		>
			Auguste Edouart
		</button>
		<br />
        <button
			v-on:click="selectArtist(artist[7], $event)"
			value="Frederic Remington"
			class="artist-button"
		>
			Frederic Remington
		</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "HelloWorld",
	components: {},
	data() {
		return {
			artist: [
				"Paul Gauguin",
				"Vincent van Gogh",
				"Rembrandt",
				"Asher Brown Durand",
				"Albert Bierstadt",
				"Paul Cézanne",
				"Auguste Edouart",
				"Frederic Remington",
			],
		};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
		this.getFavouritedArtists();
	},
	methods: {
		routeToHome: function () {
			this.$router.push("/home");
		},
		routeToGame: function () {
			this.$router.push({ path: "/game", query: { artist: "random" } });
		},
		selectArtist: function (artist) {
			this.$router.push({ path: "/game", query: { artist } });
		},
		test_axios: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/hello";
			axios
				.get(baseURI)
				.then((result) => {
					console.log(result);
				})
				.catch(function (error) {
					console.log(error);
				});
		},
	},
};
</script>

<style>
.selectArtist {
	display: flex;
	flex-direction: column;
	/* text */
	font-size: 20px;
	font-weight: bold;
	color: #ffffff;
}
.back-button {
	position: absolute;
	left: 10px;
	top: 10px;
	/* button */
	margin-top: 2px;
	width: 200px;
	height: 75px;
	background-color: #ece281;
	/* text */
	font-size: 40px;
	font-weight: bold;
	color: #040563;
}
.back-button:hover {
	background-color: #84c078;
}
.artist-button {
	/* button */
	margin-left: auto;
	margin-right: auto;
	width: 800px;
	height: 60px;
	background-color: #ece281;
	/* text */
	font-size: 30px;
	font-weight: bold;
	color: #040563;
}
.artist-button:hover {
	background-color: #84c078;
}
</style>
