<template>
  <div class="legend-box position-absolute p-3 d-flex flex-column align-items-start">
    <h2 class="text-dark">Legend</h2>
    <div class="gradient-bar mt-2 w-100" :style="{ background: gradient }"></div>
    <div class="row justify-content-between mt-1 labels">
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
    },
    colors: { // Add this prop
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      gradient: ''
    }
  },
  watch: {
    colors(newColors) {
      this.gradient = `linear-gradient(to right, ${newColors.join(',')})`;
    }
  },
  mounted() {
    this.gradient = `linear-gradient(to right, ${this.colors.join(',')})`;
  }
}
</script>

<style scoped>
.legend-box {
  right: 20px;
  width: 250px;
  background-color: white;
  border-radius: 5px;
}

.gradient-bar {
  height: 12px;
}

.labels {
  width: 110% !important;
}
</style>