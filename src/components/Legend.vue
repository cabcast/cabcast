<template>
  <div class="legend-box position-absolute p-3 d-flex flex-column align-items-start">
    <h2 class="text-dark">Legend</h2>
    <div class="gradient-bar mt-2 w-100"></div>
    <div class="row justify-content-between mt-1 w-100">
      <div class="col text-center p-0" v-for="label in labels" :key="label">{{ label }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LegendBox',
  props: {
    labels: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>
.legend-box {
  top: 20px;
  right: 20px;
  width: 250px;
  background-color: white;
}

.gradient-bar {
  height: 12px;
  background: linear-gradient(to right, skyblue, lightblue, peachpuff, red);
}
</style>