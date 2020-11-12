import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		timer: 0,
		userId: null
	},
	mutations: {
		setCurrentTimerValue(state, newTime) {
			state.timer = newTime
		},
		setUserIdForSession(state, userId) {
			state.userId = userId
		}
	}
})