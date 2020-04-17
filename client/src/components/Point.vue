<template>
  <div>
    <g>
      <text :x="x - radius" :y="y- radius-2">{{id}}</text>
      <circle :id="id" :cx="x" :cy="y" :r="radius" class="city-circle" />
    </g>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "Point",
  props: {
    x: Number,
    y: Number,
    id: String
  },
  data() {
    return {
      radius: 10
    };
  },
  created() {
    console.log(this.id, this.x, this.y);
  }
});
</script>

<style>
.city-circle {
  stroke: #000;
}
</style>