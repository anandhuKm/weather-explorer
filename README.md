# Weather Explorer

A web application for the exploration of German weather data provided by the [DWD](https://opendata.dwd.de/).

## Development

- install dependencies: `pnpm install` or `npm install`
- run the dev server: `pnpm dev` or `npm run dev`

## Tasks

1. Implement the function `countStationsPerState` in `src/routes/+page.svelte` to count the number of weather stations for each unique state.
2. Implement the function `computeBarWidth` in `src/lib/components/Barchart.svelte` to compute the width for the bars in the bar chart with respect to the respective value.
3. Implement the functions `toggleSelection`, `selectStationsByState`, and `resetSelection` in `src/routes/+page.svelte` to enable selections of the weather stations.
4. Highlight selected stations in `src/lib/components/Map.svelte` using CSS.
5. Implement the functions `formatCoordinates` and `formatHeight` in `src/lib/components/StationCard.svelte` to format the respective values in a sensible manner.
6. Implement the function `linePath` in `src/lib/components/TimeSeries.svelte` to draw a line chart of a station's temperature measurements over time.
7. Add a dot for the minimum and maximum temperature in the time series in `src/lib/components/TimeSeries.svelte` and add a text label to each with the respective temperature value.

## Further Improvements

Here are some ideas for optional and more advanced improvements to the app:

- Hover and select stations in the map based on proximity of the cursor. Always highlight the station that is closest to the cursor and toggle its selection on a click. Hint: [Voronoi diagrams](https://d3js.org/d3-delaunay/voronoi) are useful for that.
- Allow zooming to a state in the map by clicking it. Make sure to provide a way to reset the view to the whole of Germany.
- Encode each station's height in the color of the circle in the map. See [d3's chromatic scales](https://d3js.org/d3-scale-chromatic).
- Improve the performance of data loading and use more data by updating the data loading script `data/load-data.py`. Possible options are either using a better suited binary format for the data or setting up a small data backend that provides interfaces for data access.
- Add advanced filtering using a newly implemented component, e.g. by state, height range, name.
- Allow the selection of states also in the map component, for example a circular or rectangular selection.
