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
        <input type="range" class="form-range custom-slider" id="slider" min="0" max="23" step="1" value="0" v-model="hour">
        <div class="d-flex justify-content-between">
          <span v-for="hr in hours" :key="hr">{{ hr }}</span>
        </div>
      </div>
      <div class="mt-3 text-left" style="width: 50px; display: inline-block; padding-right: 5px;">
        <label for="day">Day</label>
        <select class="form-control" id="day" v-model="day">
          <option v-for="day in days" :key="day" :value="day">
            {{ day }}
          </option>
        </select>
      </div>
      <div class="mt-3 text-left" style="width: 50px; display: inline-block; padding-right: 5px;">
        <label for="month">Month</label>
        <select class="form-control" id="month" v-model="month" @change="updateDays">
          <option v-for="month in months" :key="month" :value="month">
            {{ month }}
          </option>
        </select>
      </div>
      <div class="mt-3 text-left" style="width: 75px; display: inline-block; padding-right: 5px;">
        <label for="year">Year</label>
        <select class="form-control" id="year" v-model="year">
          <option v-for="year in years" :key="year" :value="year">
            {{ year }}
          </option>
        </select>
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
      hours: [0, 5, 11, 17, 23],
      hour: 0,
      day: '16',
      month: '06',
      year: '2023',
      days: [],
      months: ['06', '07', '08'],
      years: ['2023']
    }
  },
  watch: {
    day() {
      this.updateMapSourceData();
    },
    month() {
      this.updateMapSourceData();
    },
    year() {
      this.updateMapSourceData();
    },
    hour() {
      this.updateMapSourceData();
    }
  },
  mounted() {
    mapboxgl.accessToken = this.accessToken
    this.map = new mapboxgl.Map({
      container: 'map',
      // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
      center: [-87.6, 41.85],
      zoom: 10,
      style: 'mapbox://styles/mapbox/dark-v11'
    })

    this.map.on('load', () => {
      this.map.addSource('chicago1', {
        type: 'geojson',
        data: '/Chicago_06_15_23_05.geojson' // initial data
      });

      this.map.addLayer({
        id: 'Chicago-1',
        type: 'fill', // replace with the type of your layer
        source: 'chicago1',
        // Add the rest of your layer options here
        paint: {
        'fill-color': [
          'case',
          ['==', ['get', 'cartodb_id'], null],
          'gold',
          [
            'interpolate',
            ['linear'],
            ['get', 'cartodb_id'],
            0, 'gold',
            20, 'red'
          ]
        ],
        'fill-opacity': 0.8
        }
      });
      
      const layers = [
        '0',
        '2',
        '5',
        '10',
        '20+'
      ];
      this.labels = layers;
      const colors = [
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
          layers: ['Chicago-1']
        });
        document.getElementById('pd').innerHTML = subcounty.length
          ? `<h4>${subcounty[0].properties.name}</h4><p>${subcounty[0].properties.cartodb_id || 0} calls per hour</p>`
          : `<p>Hover over a sub-county!</p>`;
      });
      this.map.on('mouseleave', 'Chicago-1', () => {
        this.map.getCanvas().style.cursor = '';
      });
      this.updateDays();
    });
  },
  methods: {
    updateDays() {
      const month = parseInt(this.month);
  let startDay, endDay;
  switch (month) {
    case 6:
      startDay = 16;
      endDay = 30;
      break;
    case 7:
      startDay = 1;
      endDay = 31;
      break;
    case 8:
      startDay = 1;
      endDay = 16;
      break;
  }
  this.days = Array.from({ length: endDay - startDay + 1 }, (_, i) => String(i + startDay).padStart(2, '0'));
  },
    updateMapSourceData() {
      if (this.day && this.month && this.year && this.hour !== null && this.map) {
        const mm = String(this.month).padStart(2, '0'); 
        const dd = String(this.day).padStart(2, '0');
        const yy = String(this.year).slice(-2);
        const formattedDate = `${mm}_${dd}_${yy}`;

        const hh = String(this.hour).padStart(2, '0');
        
        const geojsonUrl = `/Chicago_${formattedDate}_${hh}.geojson`;
        this.map.getSource('chicago1').setData(geojsonUrl);
      }
    }
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
  left: 50px;
  bottom: 0;
  width: calc(100% - 50px);
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