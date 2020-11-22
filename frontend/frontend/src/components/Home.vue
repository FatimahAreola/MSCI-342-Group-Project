<template>
	<div class="home">
		<button v-on:click="test_axios">Test Access To Flask App</button>
		<br />
		<button v-on:click="routeToGame" class="play-button options">PLAY</button>
		<p></p>
		<button v-on:click="routeToProfile" class="profile options">PROFILE</button>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "HelloWorld",
	components: {},
	data() {
		return {};
	},
	props: {
		msg: String,
	},
	mounted() {
		this.test_axios();
		this.getFavouritedArtists();
	},
	methods: {
		routeToGame: function () {
			this.$router.push("/game");
		},
		routeToProfile: function () {
			this.$router.push("/profile");
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
		getFavouritedArtists: function () {
			const baseURI = process.env.VUE_APP_HOST_URL + "api/artist/saved";
			const postData = { userID: this.$store.state.userId };
			axios.post(baseURI, postData).then((response) => {
				this.$store.commit("setFavouritedArtists", response.data);
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

.options {
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
</style>
