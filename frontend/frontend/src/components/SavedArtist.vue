<template>
	<div class="artists">
		<div class="left">
			<p>{{ artistName }}</p>
		</div>
		<div class="left">
			<button
				class="saveButton"
				v-on:click="
					savedArtist
						? updateArtistRelationship('remove')
						: updateArtistRelationship('save')
				"
			>
				{{ savedArtist ? "UNSAVE" : "SAVE" }}
			</button>
		</div>
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
		updateArtistRelationship: function (action) {
			const postData = {
				artistName: this.artistName,
				action: action,
				userID: this.$store.state.userId,
			};
			const baseURI = process.env.VUE_APP_HOST_URL + "api/artist";
			axios.post(baseURI, postData).then(() => {
				this.savedArtist = this.savedArtist ? false : true;
			});
		},
	},
};
</script>

<style scoped>
.left {
	display: inline-block;
	padding-left: 10px;
}
.saveButton {
	/* button */
	width: 55px;
	height: 20px;
	border: 2px solid #ffe381;
	background-color: #ffe381;
	/* text */
	font-size: 10px;
	font-weight: bold;
	color: #d282a6;
}
</style>