<template>
  <div id="app">
    <img src="https://www.localsolver.com/docs/last/_images/tsp.png" />
    <Main msg="Traveling Salesman Problem - Genetic Algorithm" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Main from "@/components/Main.vue";

@Component({
  components: {
    Main
  }
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
