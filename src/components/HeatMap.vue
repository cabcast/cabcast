<template>
  <div>
    <div id="map"></div>
    <LegendBox :labels="labels" />
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl'
import LegendBox from './Legend.vue'
export default {
  components: {
    LegendBox
  },
  methods: {
    generateLabels(min, max) {
      const range = max - min;
      const step = range / 4;
      const labels = [min, min + step, min + 2 * step, min + 3 * step, max];
      return labels.map(label => Math.round(label / 2) * 2);
    }
  },
  data() {
    return {
      map: null,
      accessToken: 'pk.eyJ1Ijoia2FydGhpYzI1IiwiYSI6ImNsb2tpazRjdTBqNXoya3MyYmx3MWFlZXgifQ.D6Bxvtj4NhZ2U1Pt6kFMug',
      labels: []
    }
  },
  mounted() {
    mapboxgl.accessToken = this.accessToken
    this.map = new mapboxgl.Map({
      container: 'map',
      // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
      style: 'mapbox://styles/mapbox/dark-v11',
      center: [-87.6, 41.85],
      zoom: 10
    })

    fetch('/Chicago.geojson')
      .then(response => response.json())
      .then(data => {
        const values = data.features.map(feature => feature.properties.cartodb_id);
        const min = Math.min(...values);
        const max = Math.max(...values);
        this.labels = this.generateLabels(min, max);
      });

    this.map.on('load', () => {
      // Add a geojson point source.
      // Heatmap layers also work with a vector tile source.
      this.map.addSource('demand', {
        'type': 'geojson',
        'data': '/Chicago.geojson'
      });

      this.map.addLayer(
        {
          'id': 'demand-choropleth',
          'type': 'fill',
          'source': 'demand',
          'layout': {},
          'maxzoom': 9,
          'paint':{
      'fill-color': [
        'interpolate',
        ['linear'],
        ['get', 'cartodb_id'],
        1,
        '#f1eef6',
        2,
        '#bdc9e1',
        3,
        '#74a9cf',
        4,
        '#2b8cbe',
        5,
        '#045a8d'
      ],
      'fill-opacity': 0.8
    } 
  });

      const popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: false
      });

      this.map.on('mouseenter', 'demand-choropleth', (e) => {
        // Change the cursor style as a UI indicator.
        this.map.getCanvas().style.cursor = 'pointer';

        // Copy coordinates array.
        const coordinates = e.features[0].geometry.coordinates[0][0];
        const description = "<p>" + e.features[0].properties.cartodb_id + "</p>";
        // const description = "Demand = <b>" + Math.ceil(Math.exp(e.features[0].properties.cartodb_id)) + "</b><br>Latitude = <b>" + Math.round(e.features[0].geometry.coordinates[1] * 100) / 100 + "</b><br>Longitude = <b>" + Math.round(e.features[0].geometry.coordinates[0] * 100) / 100 + "</b>";

        // Populate the popup and set its coordinates
        // based on the feature found.
        popup.setLngLat(coordinates).setHTML(description).addTo(this.map);
      });

      this.map.on('mouseleave', 'demand-choropleth', () => {
        this.map.getCanvas().style.cursor = '';
        popup.remove();
      });
    });
  }
}
</script>

<style scoped>
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
  z-index: -1;
}

.mapboxgl-popup {
  max-width: 400px;
  font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
}
</style>