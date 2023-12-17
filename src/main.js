import './assets/main.css'


import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router/index.js'

createApp(App).use(router).mount('#app')

import axios from "axios";

let url = "http://127.0.0.1:8000/patman/api/";

axios.get(url)
.then(function(response){
    console.log(response);
})
.catch(function(response){
    console.log(response);
})