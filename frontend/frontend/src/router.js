import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Home from './components/Home.vue'
import Game from './components/Game.vue'
import GameSummary from './components/GameSummary.vue'

const routes = [
	{
		path: "/",
		component: Home
	},
	{
		path: "/game",
		component: Game
	},
	{
		path: "/gameSummary",
		name: 'GameSummary',
		component: GameSummary
	}
];

const router = new VueRouter({
	mode: "history",
	routes,
});

export default router;