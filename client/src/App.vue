<template>
  <div id="app">
    <img id="logo" src="https://www.localsolver.com/docs/last/_images/tsp.png" />
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

<style >
#logo {
  width: 150px;
  height: 150px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
