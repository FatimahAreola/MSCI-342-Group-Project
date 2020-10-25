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
      // Initializing variables
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
      // Start timer if state changes to run, else pause timer
      if (this.state == "run") {
        this.play();
      } else if (this.state == "pause") {
        this.pause();
      }
    },
  },
  methods: {
    // Play method sets timer to 0 and starts, else stops timer and updates time
    play() {
      if (this.startTime === null) {
        this.restart();
        this.startTime = new Date();
      }
      if (this.endTime !== null) {
        this.runTime += new Date() - this.endTime;
      }
      if (this.running) return;
      this.started = setInterval(this.timerRunning, 10);
      this.running = true;
    },
    // Pause method stops timer at current time
    pause() {
      this.running = false;
      this.endTime = new Date();
      clearInterval(this.started);
    },
    // Restart method resets variables to initial value
    restart() {
      this.running = false;
      clearInterval(this.started);
      this.startTime = null;
      this.endTime = null;
      this.runTime = 0;
      this.time = "00:00:00";
    },
    // timerRunning method sets up timer to show zeros for empty time
    TimerRunning() {
      var currentTime = new Date(),
        timeElapsed = new Date(currentTime - this.timeBegan - this.stoppedDuration),
        hours = timeElapsed.getUTCHours(),
        minutes = timeElapsed.getUTCMinutes(),
        seconds = timeElapsed.getUTCSeconds();

      this.time = this.placeHolder(hours, 2) + ":" + this.placeHolder(minutes, 2) + ":" + this.placeHolder(seconds, 2);
    },
    // placeHolder method counts up by seconds when timer is running
    placeHolder(num, num2) {
      var zero = "";
        for(var i = 0; i < num2; i++){
          zero += "0";
        }
      return (zero + num).slice(-num2);
    },
  },
};
</script>
// no styling done
<style>
</style>