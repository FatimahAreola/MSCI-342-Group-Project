<template>
	<div class="modal-mask">
		<div class="modal-wrapper">
			<div class="modal-container">
				<div class="modal-header">
					<slot name="header" v-if="result"> It's A Match!!</slot>
					<slot name="header" v-else>Try Again!</slot>
				</div>

				<div class="modal-body" v-if="!result">
					<div v-for="card in flipped" :key="card.cardId" class="art">
						<img style="width: 350px; height: 370px" :src="card.artUrl" />
					</div>
				</div>

				<div class="modal-body" v-else>
					<img style="width: 350px; height: 370px" :src="flipped[0].artUrl" />
					<div style="display: flex; flex-direction: column">
						<div>
							Art Name: <br />
							{{ flipped[0].artName }}
						</div>
						<br />
						<div>
							Artist: <br />
							{{ flipped[0].artistName }} <br />
							{{ flipped[0].birthYear }} - {{ flipped[0].deathYear }}
						</div>
						<br />
						<div>
							Period: <br />
							{{ flipped[0].artPeriod }} <br />
						</div>
						<br />
						<div>
							Culture: <br />
							{{ flipped[0].artCulture }} <br />
						</div>
					</div>
				</div>

				<div class="modal-footer">
					<slot name="footer">
						<button v-if="result" class="modal-default-button" @click="close">
							Continue Playing
						</button>
					</slot>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "MatchPopUp",
	props: ["flipped"],
	data() {
		return {
			result: null,
		};
	},
	watch: {
		flipped() {
			if (this.flipped.length >= 2) {
				if (this.flipped[0].artName == this.flipped[1].artName) {
					this.result = true;
				} else {
					this.result = false;
					setTimeout(() => {
						this.close();
					}, 1000);
				}
			}
		},
	},
	methods: {
		close() {
			this.$emit("close", { value: this.result });
			this.result = null;
		},
	},
};
</script>

<style scoped>
.modal-mask {
	position: fixed;
	z-index: 9998;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: table;
	transition: opacity 0.3s ease;
}

.modal-wrapper {
	display: table-cell;
	vertical-align: middle;
}

.modal-container {
	width: 800px;
	height: 500px;
	margin: 0px auto;
	padding: 20px 30px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	background-color: #ffe381;
	border-radius: 2px;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
	transition: all 0.3s ease;
	font-family: Helvetica, Arial, sans-serif;
}

.modal-header {
	margin-top: 0;
	height: 40px;
	line-height: 40px;
	font-weight: 600;
	font-size: 30px;
}

.modal-body {
	margin: 20px 0;
	display: flex;
	justify-content: space-around;
}

.art {
	width: 350px;
	height: 370px;
	background-color: #fff;
}

.modal-footer {
	display: flex;
	justify-content: center;
}

.modal-default-button {
	/* button */
	width: 200px;
	margin-top: 10px;
	display: block;
	height: 40px;
	border: 2px solid #e76f85;
	background-color: #f0899c;
	/* text */
	font-size: 15px;
	font-weight: bold;
	color: #ffe381;
	text-shadow: 2px 2px 4px #000000;
}
</style>