<template>
	<div>
		<span>{{ maxTime - time }}</span>
	</div>
</template>

<script>
export default {
	mounted() {
		this.play();
	},
	props: ["state", "maxTime"],
	data() {
		return {
			time: "00:00:00",
			startTime: null,
			endTime: null,
			runTime: 0,
			started: null,
			running: false,
		};
	},
	watch: {
		state: {
			immediate: true,
			deep: true,
			handler(newValue) {
				if (newValue == "run") {
					this.play();
				} else if (newValue == "stopped") {
					this.end();
				}
			},
		




		},
	},
	methods: {
		// Play method sets timer to 0 and starts, else stops timer and updates time
		play() {
			if (this.running) return;
			if (this.startTime === null) {
				this.restart();
				this.startTime = new Date();
			}
			if (this.endTime !== null) {
				this.runTime += new Date() - this.endTime;
			}
			this.started = setInterval(this.timerRunning, 10);
			this.running = true;
		},
		// End method stops timer at current time
		end() {
			this.$store.commit("setCurrentTimerValue", this.time);
			this.running = false;
			this.endTime = new Date();
			clearInterval(this.started);
		},
		// Restart method resets variables to initial values
		restart() {
			this.running = false;
			clearInterval(this.started);
			this.runTime = 0;
			this.startTime = null;
			this.endTime = null;
			this.time = "00:00:00";
		},
		// timerRunning method counts up by seconds when timer is running
		timerRunning() {
			var currentTime = new Date(),
				timeElapsed = new Date(currentTime - this.startTime - this.runTime),
				hours = timeElapsed.getUTCHours(),
				minutes = timeElapsed.getUTCMinutes(),
				seconds = timeElapsed.getUTCSeconds();

			this.time =
				this.placeHolder(hours) +
				":" +
				this.placeHolder(minutes) +
				":" +
				this.placeHolder(seconds);
		},
		// placeHolder method sets up timer to show zeros for empty time
		placeHolder(num) {
			var zero = "";
			for (var i = 0; i < 2; i++) {
				zero += "00";
			}
			return (zero + num).slice(-2);
		},
	},
};
</script>

<style>
</style>