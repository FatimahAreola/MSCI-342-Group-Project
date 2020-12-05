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
					{{ savedArtist ? "UNFAVOURITE" : "FAVOURITE" }}
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
export default {
	props: ["artistName"],
	mounted() {},
	data() {
		return {
			savedArtist: this.isArtistFavourited(),
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
		isArtistFavourited: function () {
			const favouritedArtistsInDB = [];
			this.$store.state.favouritedArtists.forEach((artist) => {
				favouritedArtistsInDB.push(artist.name);
			});
			const val_a = favouritedArtistsInDB.includes(this.artistName);
			this.savedArtist = val_a;
			return val_a;
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
	width: 400px;
}
.left {
	display: inline-block;
}
.right {
	display: inline-block;
	padding-left: 10px;
	padding-top: 12px;
}
.saveButton {
	/* button */
	margin-top: 7px;
	width: 130px;
	height: 30px;
	background-color: #ece281;
	/* text */
	font-size: 15px;
	font-weight: bold;
	color: #040563;
}
</style>
