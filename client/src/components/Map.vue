<template>
  <div>
    <svg id="map" width="800" height="600" @click="drawPoint">
      <g v-for="c in cities" v-bind:key="c.id">
        <text :x="c.x - 10" :y="c.y - 10 - 2">{{c.id}}</text>
        <circle id="c.id" :cx="c.x" :cy="c.y" :r="10" style="stroke:#000" />
      </g>
      <!-- <line key="id" :x1="1" :y1="12" :x2="323" :y2="212" style="stroke: #000" /> -->
    </svg>
  </div>
</template>

<script lang="ts">
import Point from "./Point.vue";
import Vue from "vue";

export default Vue.extend({
  name: "Map",
  components: {
    // Point
  },
  props: {
    cities: Array
  },
  data() {
    return {
      points: []
    };
  },
  methods: {
    drawPoint(event: any) {
      const numberOfCities = this.cities.length;
      const rect = event.target.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      console.log(x, y);
      const newCityIdentifier = "City " + (numberOfCities + 1).toString();
      const newCity = { id: newCityIdentifier, x: x, y: y };
      this.$emit("addCity", newCity);
    }
  }
});
</script>

<style>
#map {
  margin: 20px;
  border: 1px solid #000;
}
</style>