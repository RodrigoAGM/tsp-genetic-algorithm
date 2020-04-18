<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <Map :cities="cities" :results="results" @addCity="addCity" />
    <b-button @click="calculateRoute" variant="primary">Calcular ruta</b-button>
    <Result :results="results" />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Map from "./Map.vue";
import Result from "./Result.vue";
import axios from "axios";

@Component({
  components: {
    Map,
    Result
  }
})
export default class Main extends Vue {
  @Prop() private msg!: string;

  private fetching = false;
  private cities: Array<object> = [];
  private results: object = {
    route: [],
    distance: 0,
    time: 0
  };

  public calculateRoute() {
    axios({
      method: "POST",
      url: " http://0.0.0.0:5000/calculate_route",
      data: this.cities
    }).then(
      result => {
        console.log(result.data.cities);
      },
      error => {
        console.error(error);
      }
    );
  }

  public clearMap() {
    this.fetching = false;
  }
  public addCity(city: object) {
    console.log(city);
    this.cities.push(city);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
