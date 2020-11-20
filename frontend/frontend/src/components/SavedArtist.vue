<template>
	<div>
		<p>{{ artistName }}</p>
		<button v-on:click="savedArtist ? unsaveArtist() : saveArtist()">
			{{ savedArtist ? "UNSAVE" : "SAVE" }}
		</button>
	</div>
</template>

<script>
import axios from "axios";
export default {
	props: ["artistName"],
	data() {
		return {
			savedArtist: false,
		};
	},
	methods: {
		saveArtist: function () {
			const postData = {
				artistName: this.artistName,
				action: "save",
				userid: this.$store.state.timer,
			};
			const baseURI = process.env.VUE_APP_HOST_URL + "api/artist";
			axios
				.post(baseURI, postData)
				.then(() => {
					this.$notify({
						group: "foo",
						type: "success",
						title: "Success",
						text: "Saved Artist",
					});
				})
				.catch(() => {
					this.$notify({
						group: "foo",
						type: "success",
						title: "Success",
						text: "Saved Artist",
					});
				});
		},
		unsaveArtist: function () {
			alert("unsaving");
		},
	},
};
</script>

<style scoped>
</style>