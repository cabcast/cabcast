<template>
  <div>
    <div id='map'></div>
    <div class='map-overlay' id='features'>
      <h4>Demand</h4>
      <div id='pd'>
        <p>Hover over a sub-county!</p>
      </div>
    </div>
    <div class='map-overlay' id='dtsel'>
      <div class="mt-3 text-left">
        <label for="slider">Hour of day</label>
        <input type="range" class="form-range custom-slider" id="slider" min="0" max="23" step="1" value="0">
        <div class="d-flex justify-content-between">
          <span v-for="hour in hours" :key="hour">{{ hour }}</span>
        </div>
      </div>
      <div class="mt-3 text-left">
        <label for="date">Date</label>
        <input type="date" class="form-control" id="date" placeholder="Date for forecast...">
      </div>
    </div>
    <div style="position: absolute; right: 0; top: 350px;">
      <LegendBox :labels="labels" :colors="colors" />
    </div>
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl'
import LegendBox from './Legend.vue'
export default {
  components: {
    LegendBox
  },
  data() {
    return {
      map: null,
      accessToken: 'pk.eyJ1Ijoia2FydGhpYzI1IiwiYSI6ImNsb2tpazRjdTBqNXoya3MyYmx3MWFlZXgifQ.D6Bxvtj4NhZ2U1Pt6kFMug',
      labels: [],
      colors: [],
      hours: [0, 5, 11, 17, 23]
    }
  },
  mounted() {
    mapboxgl.accessToken = this.accessToken
    this.map = new mapboxgl.Map({
      container: 'map',
      // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
      style: 'mapbox://styles/karthic25/clpmyzie900jp01p643bd13ls',
      center: [-87.6, 41.85],
      zoom: 10
    })

    this.map.on('load', () => {
      const layers = [
        '0',
        '2',
        '5',
        '10',
        '20',
        '50',
        '100+'
      ];
      this.labels = layers;
      const colors = [
        '#FFEDA0',
        '#FED976',
        '#FEB24C',
        '#FD8D3C',
        '#FC4E2A',
        '#E31A1C',
        '#BD0026',
      ];
      function hexToRgb(hex) {
        let r = parseInt(hex.slice(1, 3), 16);
        let g = parseInt(hex.slice(3, 5), 16);
        let b = parseInt(hex.slice(5, 7), 16);
        return `rgb(${r}, ${g}, ${b})`;
      }
      let rgbColors = colors.map(color => hexToRgb(color));
      this.colors = rgbColors;

      // update legend
      this.map.on('mousemove', (event) => {
        this.map.getCanvas().style.cursor = 'pointer';
        const subcounty = this.map.queryRenderedFeatures(event.point, {
          layers: ['Chicago']
        });
        document.getElementById('pd').innerHTML = subcounty.length
          ? `<h4>${subcounty[0].properties.name}</h4><p>${subcounty[0].properties.cartodb_id} calls per hour</p>`
          : `<p>Hover over a sub-county!</p>`;
      });
      this.map.on('mouseleave', 'Chicago', () => {
        this.map.getCanvas().style.cursor = '';
      });
    });
  }
}
</script>

<style scoped>
/**
* Create a position for the map
* on the page */
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}

/**
* Set rules for how the map overlays
* (information box and legend) will be displayed
* on the page. */
.map-overlay {
  position: absolute;
  bottom: 0;
  right: 0;
  background: #fff;
  margin-right: 20px;
  margin-top: 10px;
  font-family: Arial, sans-serif;
  border-radius: 3px;
  padding-left: 10px;
  padding-right: 10px;
}

#features {
  top: 0;
  margin-top: 20px;
  width: 250px;
  padding-bottom: 20px; /* Add some padding to the bottom */
  height: 100px !important;
}

#dtsel {
  top: 115px;
  margin-top: 20px;
  width: 250px;
  padding-bottom: 20px; /* Add some padding to the bottom */
  height: 200px !important;
}

.custom-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  background: grey;
  cursor: pointer;
}

.custom-slider::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: grey;
  cursor: pointer;
}
</style>