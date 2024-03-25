<script lang="ts">
	import { loadStation, type Station } from "$lib/data";
	import TimeSeries from "./TimeSeries.svelte";

	let { station }: { station: Station } = $props();

	function formatCoordinates(longitude: number, latitude: number): string {
		/* TODO
		Format the geographic coordinates as a string.
		 */
		return "";
	}

	function formatHeight(height: number): string {
		/* TODO
		Format the station's height as a string.
		*/
		return "";
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
				height={100}
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
