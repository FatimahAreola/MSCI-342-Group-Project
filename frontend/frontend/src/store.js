import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		timer: 0
	},
	mutations: {
		setCurrentTimerValue(state, newTime) {
			state.timer = newTime
		}
	}
})