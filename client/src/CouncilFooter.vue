<template>
  <div class="footer">
    <b-row>
      <b-col sm="2">
        <label># Iteraciones</label>
      </b-col>
      <b-col sm="2">
        <b-form-input v-model="iteractions" type="number"></b-form-input>
      </b-col>
      <b-col sm="2">
        <label>Temperatura</label>
      </b-col>
      <b-col sm="2">
        <b-form-input v-model="temperature" type="number"></b-form-input>
      </b-col>
      <b-col sm="2">
        <label>Indice de enfriamiento</label>
      </b-col>
      <b-col sm="2">
        <b-form-input v-model="coldIndex" type="number"></b-form-input>
      </b-col>
    </b-row>
    <b-row class="footer">
      <b-col sm="7">
        <b-button
          @click="$emit('calcRoute', coldIndex, temperature, iteractions)"
          variant="primary"
        >Calcular la ruta</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Vue from "vue";
export default Vue.extend({
  name: "CouncilFooter",
  data() {
    return {
      coldIndex: null,
      temperature: null,
      iteractions: null
    };
  }
});
</script>

<style  scoped>
.footer {
  margin-top: 20px;
}
</style>