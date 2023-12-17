<template>
<!--  <nav>-->
<!--    <router-link to="/">Home</router-link> -->
<!--    <router-link to="/about">About</router-link>-->
<!--  </nav>-->
<!--  <router-view/>-->
  <main>
    <router-link to="/"></router-link>
    <router-view/>
  </main>

</template>

<style>
#app {

}
</style>



<script>
import axios from "axios";
import LoginView from "./views/LoginView.vue";


let url = "http://127.0.0.1:8000/patman/api/users/";

</script>