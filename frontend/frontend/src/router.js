import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Home from './components/Home.vue'
import Game from './components/Game.vue'
import Profile from './components/Profile.vue'

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
		path: "/profile",
		name: 'profile',
		component: Profile
	}
];

const router = new VueRouter({
	mode: "history",
	routes,
});

export default router;