<template>
  <div id="app">
    <div class="container">
      <CouncilHeader />
      <GmapMap
        :center="{lat:-12.11, lng:-77.01}"
        :zoom="15"
        map-type-id="terrain"
        style="width: 100%; height: 700px;"
        @click="onEvent"
      >
        <GmapMarker
          v-for="(m,key) in markers"
          :position="m"
          :clickable="true"
          v-bind:key="key"
          :label="(key+1).toString()"
        ></GmapMarker>

        <GmapPolyline v-bind:path.sync="path" v-bind:options="{ strokeColor:'#0000FF'}"></GmapPolyline>
      </GmapMap>
      <CouncilFooter @calcRoute="calculateRoute" />
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import CouncilHeader from "./CouncilHeader.vue";
import CouncilFooter from "./CouncilFooter.vue";
// import axios from "axios";
export default Vue.extend({
  name: "LimaCovid",
  components: {
    CouncilHeader,
    CouncilFooter
  },
  data() {
    return {
      markers: [],
      path: []
    };
  },
  methods: {
    onEvent(event) {
      this.markers.push({
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      });
    },
    areFieldsValid() {
      return true;
    },
    calculateRoute(coldIndex, temperature, iteractions) {
      console.log(coldIndex, temperature, iteractions);
      if (!this.areFieldsValid()) {
        this.$bvToast.toast("Los campos ingresados no son validos.", {
          title: "Error",
          variant: "danger",
          solid: true
        });
        return;
      }
      this.path = this.markers;
      // axios({
      //   method: "POST",
      //   url: "http://localhost:5000/calculate_route",
      //   data: {
      //     cities: this.cities,
      //     eliteSize: this.eliteSize,
      //     initialPoblation: this.initialPoblation,
      //     generationNumber: this.generationNumber,
      //     mutationProbability: this.mutationProbability
      //   }
      // }).then(
      //   result => {
      //     console.log(result.data.route);
      //     this.results = result.data;
      //   },
      //   error => {
      //     console.error(error);
      //   }
      // );
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
