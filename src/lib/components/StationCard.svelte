<script lang="ts">
	import { loadStation, type Station } from "$lib/data";
	import TimeSeries from "./TimeSeries.svelte";

	let { station }: { station: Station } = $props();

	function formatCoordinates(longitude: number, latitude: number): string {
		/* TODO
		Format the geographic coordinates as a string.
		 */
		function convertion(coords: number, type: string): string {
			const positiveCord = Math.abs(coords); //convert to positive for easier calculation
			const degrees = Math.floor(positiveCord);
			const minutes = Math.floor((positiveCord - degrees) * 60);
			// to get second, multiply the remaining by 3600(60 minutes in degree & 60 in minutes) and fix it to max 2 decimal place
			const seconds = ((positiveCord - degrees - minutes / 60) * 3600).toFixed(2);
			const direction = type === "longitude" ? (coords >= 0 ? "E" : "W") : coords >= 0 ? "N" : "S"; //check for negative or positive coords
			return degrees + "° " + minutes + "' " + seconds + "'' " + direction;
		}
		let longitudeString = convertion(longitude, "longitude");
		let latitudeString = convertion(latitude, "latitude");

		return latitudeString + "," + longitudeString;
	}

	function formatHeight(height: number): string {
		/* TODO
		Format the station's height as a string.
		*/

		return height.toString() + " meters";
	}
</script>

<div id="card">
	<h2>{station.name} ({station.id})</h2>
	<p id="description">
		In the state of <span>{station.state}</span> at coordinates
		<span id="coords">{formatCoordinates(station.longitude, station.latitude)}</span> and a height
		of
		<span id="height">{formatHeight(station.height)}</span>.
	</p>
	<div id="temperature-chart">
		{#await loadStation(station.id) then data}
			<TimeSeries
				width={500}
				height={300}
				data={data.map((d) => [d.date, d.temperatureAirMean200])}
			/>
		{/await}
	</div>
</div>

<style>
	#card {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		justify-items: center;
		align-items: center;
		background-color: #f1f5f9;
		border-radius: 10px;
		padding: 1rem;
	}

	h2 {
		margin: 0;
		grid-column: 1 / -1;
	}

	#description span {
		font-weight: bold;
		white-space: nowrap;
	}

	#coords,
	#height {
		font-feature-settings: tnum;
	}
</style>
