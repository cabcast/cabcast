# Demand Forecasting Dashboard
This project is a demand forecasting dashboard built with Node.js, Vue.js, Bootstrap, and Mapbox GL.

## Overview
The dashboard provides a visual representation of demand forecasts. It allows users to select a specific hour of the day and a date for the forecast.

The main Vue component, `HeatMap.vue`, includes a map and two overlays. The first overlay displays information about the demand in a specific sub-county when the user hovers over it. The second overlay contains a slider and a date input for selecting the hour of the day and the date for the forecast.

The data is displayed on a map using Mapbox GL.

## Installation
1. Clone the repository:
`git clone`

2. Install the dependencies:
`cd npm install`

3. Start the server:
`npm start`

## Usage

Open your browser and navigate to `http://localhost:3000` to view the dashboard.

Use the slider to select the hour of the day and the date input to select the date for the forecast. The map will update to display the forecast for the selected hour and date.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
