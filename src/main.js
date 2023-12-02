import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGlobeAmericas, faChartSimple } from '@fortawesome/free-solid-svg-icons'

import App from './App.vue'
import HeatMap from './components/HeatMap.vue'
import PredPlots from './components/PredPlots.vue'

library.add(faGlobeAmericas, faChartSimple);

const routes = [
  { path: '/', component: HeatMap },
  { path: '/plots', component: PredPlots }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon);
app.config.productionTip = false;
app.use(router).mount('#app');
