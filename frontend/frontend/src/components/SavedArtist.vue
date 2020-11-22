<template>
	<div class="artists">
<div class="artist-bin">
		<div class="left">
			<p>{{ artistName }}</p>
		</div>
		<div class="right">
			<button
				class="saveButton"
				v-on:click="
					savedArtist
						? updateArtistRelationship('remove')
						: updateArtistRelationship('save')
				"
			>
				{{ savedArtist ? "UNFAVOURITE" : "FAVOUTIRE" }}
			</button>
		</div>
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
.artists {
	display: flex;
	margin: auto;
	justify-content: space-around;
}
.artist-bin {
	display: flex;
	justify-content: space-between;
	width: 300px;
}
.left {
	display: inline-block;
	padding-left: 10px;
}
.right {
	display: inline-block;
	padding-left: 10px;
	padding-top: 12px;
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
