<template>
	<div id="clock">
  
  		<span class="time">{{ time }}</span>
  		<button @click="play">Play</button>
  		<button @click="pause">Pause</button>
  		<button @click="reset"Reset</button>
  
</div>

</template>

<script>
export default {
  		el: '#clock',
  		data: {
    		time: '00:00:00.000',
    		timeBegan = null,
    		timeStoppped = null,
    		stopppedDuration = 0,
    		started = null,
    		running = false,
        }
  methods: {
  	play () {
  	if(running) return;
  
  	if (timeBegan === null) {
    reset();
    timeBegan = new Date();
  }

  if (timeStopped !== null) {
    stoppedDuration += (new Date() - timeStopped);
  }

  started = setInterval(clockRunning, 10);	
  running = true;

  	}

  	pause () {
  	running = false;
  	timeStopped = new Date();
  	clearInterval(started);
}


	reset() {
  	running = false;
  	clearInterval(started);
  	stoppedDuration = 0;
  	timeBegan = null;
  	timeStopped = null;
  	clock.time = "00:00:00.000";
}

	clockRunning(){
  	var currentTime = new Date()
  , timeElapsed = new Date(currentTime - timeBegan - stoppedDuration)
  , hour = timeElapsed.getUTCHours()
  , min = timeElapsed.getUTCMinutes()
  , sec = timeElapsed.getUTCSeconds()
  , ms = timeElapsed.getUTCMilliseconds();

  clock.time = 
    zeroPrefix(hour, 2) + ":" + 
    zeroPrefix(min, 2) + ":" + 
    zeroPrefix(sec, 2) + "." + 
    zeroPrefix(ms, 3);
};

	zeroPrefix(num, digit) {
  	var zero = '';
  		for(var i = 0; i < digit; i++) {
    		zero += '0';
  		}
  	return (zero + num).slice(-digit);
	}
  }
});

}
</script>

<style>

</style>
