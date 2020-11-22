<template>
	<div class="home">
		<button v-on:click="test_axios">Test Access To Flask App</button>
		<br />
		<h3>Select Artist to Include in Game</h3>
		<button
		v-on:click="selectArtist(artist[0], $event)"
		value="Paul Gauguin"
		class="artist-button"
		>
		Paul Gauguin
		</button>
		<button
		v-on:click="selectArtist(artist[1], $event)"
		value="Vincent van Gogh"
		class="artist-button"
		>
		Vincent van Gogh
		</button>
		<button
		v-on:click="selectArtist(artist[2], $event)"
		value="Rembrandt"
		class="artist-button"
		>
		Rembrandt
		</button>
		<button
		v-on:click="selectArtist(artist[3], $event)"
		value="Asher Brown Durand"
		class="artist-button"
		>
		Asher Brown Durand
		</button>
		<button
		v-on:click="selectArtist(artist[4], $event)"
		value="Albert Bierstadt"
		class="artist-button"
		>
		Albert Bierstadt
		</button>
		<button
		v-on:click="selectArtist(artist[5], $event)"
		value="Paul Cézanne"
		class="artist-button"
		>
		Paul Cézanne
		</button>
		<button
		v-on:click="selectArtist(artist[6], $event)"
		value="Auguste Edouart"
		class="artist-button"
		>
		Auguste Edouart
		</button>
		<button
		v-on:click="selectArtist(artist[7], $event)"
		value="Frederic Remington"
		class="artist-button"
		>
		Frederic Remington
		</button>
		<h3>Or</h3>
		<button v-on:click="routeToGame" class="play-button">Play Game</button>
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
	},
	methods: {
		routeToGame: function () {
			this.$router.push({ path: "/game", query: { artist: "random" } });
		},
		selectArtist: function (artist) {
			this.$router.push({ path: "/game", query: { artist } });
		},
		test_axios: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/hello";
			console.log(baseURI);
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
.home {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.play-button {
	/* button */
	width: 800px;
	height: 300px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 100px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}

.play-button:hover {
	background-color: #f8da6c;
}
.login-button {
	/* button */
	width: 800px;
	height: 300px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 100px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 2px 2px 4px #000000;
}
.login-button:hover {
	background-color: #f8da6c;
}
.artist-button {
	/* button */
	width: 800px;
	height: 45px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 25px;
	font-weight: bold;
	color: #d282a6;
	text-shadow: 1px 1px 2px #000000;
}
.artist-button:hover {
	background-color: #f8da6c;
}
</style>
