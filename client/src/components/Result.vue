<template>
  <div>
    <p>Shortest route: {{results.route.map(x => x.id)}}</p>
    <p>Distance travelled: {{results.distance}} km</p>
    <p>Caculation time: {{results.time}} s</p>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Result extends Vue {
  @Prop() private results!: Array<string>;
}
</script>


<style scoped>
  #route{
    margin: 2rem 2rem 1rem 2rem;
  }
</style>