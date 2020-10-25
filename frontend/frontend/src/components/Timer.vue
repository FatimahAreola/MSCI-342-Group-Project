<template>
  <div>
    <span>{{ time }}</span>
  </div>
</template>

<script>
export default {
  mounted() {
    this.play();
  },
  props: ["state"],
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
    state() {
      if (this.state == "run") {
        this.play();
      } else if (this.state == "end") {
        this.end();
      }
    },
  },
  methods: {
    play() {
      if (this.running) return;
      if (this.startTime === null) {
        this.reset();
        this.startTime = new Date();
      }
      if (this.endTime !== null) {
        this.runTime += new Date() - this.endTime;
      }
      this.started = setInterval(this.clockRunning, 10);
      this.running = true;
    },
    end() {
      this.running = false;
      this.endTime = new Date();
      clearInterval(this.started);
    },
    reset() {
      this.running = false;
      clearInterval(this.started);
      this.runTime = 0;
      this.startTime = null;
      this.endTime = null;
      this.time = "00:00:00";
    },
    clockRunning() {
      var currentTime = new Date(),
        timeElapsed = new Date(
          currentTime - this.startTime - this.runTime
        ),
        hour = timeElapsed.getUTCHours(),
        min = timeElapsed.getUTCMinutes(),
        sec = timeElapsed.getUTCSeconds();

      this.time =
        this.zeroPrefix(hour, 2) +
        ":" +
        this.zeroPrefix(min, 2) +
        ":" +
        this.zeroPrefix(sec, 2);
    },
    zeroPrefix(num, digit) {
      var zero = "";
      for (var i = 0; i < digit; i++) {
        zero += "0";
      }
      return (zero + num).slice(-digit);
    },
  },
};
</script>

<style>
</style>