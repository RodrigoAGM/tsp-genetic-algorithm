<template>
  <div>
    <p>Shortest route: {{results.route}}</p>
    <p>Distance travelled: {{results.distance}}</p>
    <p>Caculation time: {{results.time}}</p>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Result extends Vue {
  @Prop() private results!: Array<string>;
}
</script>