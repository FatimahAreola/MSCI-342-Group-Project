import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Home from './components/Home.vue'
import Game from './components/Game.vue'
import GameSummary from './components/GameSummary.vue'
import CreateAccount from './components/CreateAccount/CreateAccount.vue'
import Login from './components/Login.vue'
import Profile from './components/Profile.vue'
import SelectArtist from './components/SelectArtist.vue'

const routes = [
	{
		path: "/",
		component: Login
	},
	{
		path: "/game",
		component: Game
	},
	{
		path: "/gameSummary",
		name: 'GameSummary',
		component: GameSummary
	},
	{
		path: "/createAccount",
		name: 'createAccount',
		component: CreateAccount
	},
	{
		path: "/home",
		name: 'home',
		component: Home
	},
	{
		path: "/profile",
		name: 'profile',
		component: Profile
	},
	{
		path: "/selectArtist",
		name: 'selectArtist',
		component: SelectArtist
	}
];

const router = new VueRouter({
	mode: "history",
	routes,
});

export default router;