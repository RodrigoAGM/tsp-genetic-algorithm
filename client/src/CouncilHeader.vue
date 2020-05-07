<template>
  <div class="header">
    <img src="./../assets/limalogo.jpg" />
    <h1>Repartición de viveres para afectados por el Covid-19</h1>
  </div>
</template>

<style scoped>
img {
  width: 120px;
  height: 120px;
}
.header {
  display: flex;
}
</style>

<script>
import Vue from "vue";
export default Vue.extend({
  name: "CouncilHeader"
});
</script>