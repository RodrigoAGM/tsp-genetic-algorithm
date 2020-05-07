<template>
  <div id="app">
    <CustomHeader />
    <GmapMap
      :center="{lat:-12.11, lng:-77.01}"
      :zoom="15"
      map-type-id="terrain"
      style="width: 100%; height: 800px;"
      @click="onEvent"
    >
      <GmapMarker
        v-for="(m,key) in markers"
        :position="m"
        :clickable="true"
        v-bind:key="key"
        :label="key"
      ></GmapMarker>

      <GmapPolyline v-bind:path.sync="markers" v-bind:options="{ strokeColor:'#0000FF'}"></GmapPolyline>
    </GmapMap>
  </div>
</template>

<script>
import Vue from "vue";
import CustomHeader from "./CustomHeader.vue";
export default Vue.extend({
  name: "Lima Covid",
  components: {
    CustomHeader
  },
  data() {
    return {
      markers: [
        {
          lat: -12.11,
          lng: -77.01
        },
        {
          lat: -12.12,
          lng: -77.03
        },
        {
          lat: -12.13,
          lng: -77.02
        }
      ]
    };
  },
  methods: {
    onEvent(event) {
      console.log(event.latLng.lat(), event.latLng.lng());
      this.markers.push({
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      });
    }
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 10px;
}
</style>
