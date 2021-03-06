import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		timer: 0,
		maxTime: '20:00:00',
		userId: null,
		userBestTime: null,
		favouritedArtists: []
	},
	mutations: {
		setCurrentTimerValue(state, newTime) {
			state.timer = newTime
		},
		setUserIdForSession(state, userId) {
			state.userId = userId
		},
		setCurrentUserBestTimeValue(state, bestTime) {
			state.userBestTime = bestTime
		},
		setFavouritedArtists(state, favouritedArtists) {
			state.favouritedArtists = favouritedArtists
		},
		setMaxTime(state, maxTime) {
			state.maxTime = maxTime
		},
	}
})
