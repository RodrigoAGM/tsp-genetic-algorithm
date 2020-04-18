<template>
  <div>
    <h1>{{ msg }}</h1>
    <Map :cities="cities" :results="results" @addCity="addCity" />
    <b-button @click="calculateRoute" variant="primary">Calcular ruta</b-button>
    <b-button @click="clearMap" variant="danger">Limpiar mapa</b-button>
    <br />
    <div class="input-ga">
      <b-form-input placeholder="Number of generations" v-model="generationNumber" type="number"></b-form-input>
      <b-form-input
        placeholder="Mutation probability (%)"
        v-model="mutationProbability"
        type="number"
      ></b-form-input>
      <b-form-input placeholder="Initial poblation" v-model="initialPoblation" type="number"></b-form-input>
      <b-form-input placeholder="Elite size" v-model="eliteSize" type="number"></b-form-input>
    </div>
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

  private generationNumber: number;
  private mutationProbability: number;
  private initialPoblation: number;
  private eliteSize: number;
  private fetching = false;
  private cities: Array<object> = [];
  private results: object = {
    route: [],
    distance: 0,
    time: 0
  };

  public showErrorModal(title: string, description: string) {
    this.$bvModal
      .msgBoxOk(description, {
        title: title,
        buttonSize: "sm",
        okVariant: "danger",
        headerClass: "p-2 border-bottom-0",
        footerClass: "p-2 border-top-0",
        centered: true
      })
      .then(value => {
        console.log(value);
      })
      .catch(err => {
        // An error occurred
      });
  }

  private areFieldsValid(): boolean {
    if (this.cities.length < 2) {
      console.log("erro");
      this.showErrorModal(
        "There is not enough cities",
        "You have to enter more than 2 cities to run the optimitazion search algorithm."
      );
      return false;
    }
    if (
      this.eliteSize <= 0 ||
      this.generationNumber <= 0 ||
      this.initialPoblation <= 0 ||
      this.mutationProbability <= 0
    ) {
      this.showErrorModal(
        "Error on input data",
        "all fields must have a value bigger than 0"
      );
      return false;
    } else if (this.eliteSize > this.initialPoblation) {
      this.showErrorModal(
        "Error on input data",
        "The elite size can't be greater than the initila poblation"
      );
      return false;
    }
    return true;
  }

  public calculateRoute() {
    if (!this.areFieldsValid()) {
      return;
    }

    axios({
      method: "POST",
      url: " http://localhost:5000/calculate_route",
      data: {
        cities: this.cities,
        eliteSize: this.eliteSize,
        initialPoblation: this.initialPoblation,
        generationNumber: this.generationNumber,
        mutationProbability: this.mutationProbability
      }
    }).then(
      result => {
        console.log(result.data.route);
        this.results = result.data;
      },
      error => {
        console.error(error);
      }
    );
  }

  public clearMap() {
    this.fetching = false;
    this.cities = [];
    this.results = {
      route: [],
      distance: 0,
      time: 0
    };
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
  margin: 20px 0 0;
}
.input-ga {
  display: flex;
  align-items: center;
  margin-left: 25%;
  margin-right: 25%;
}
</style>
