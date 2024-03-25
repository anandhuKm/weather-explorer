<script lang="ts">
	import Barchart from "$lib/components/Barchart.svelte";
	import StationsMap from "$lib/components/Map.svelte";
	import StationCard from "$lib/components/StationCard.svelte";
	import { loadStations, type Station } from "$lib/data";

	// the $state makes these variables reactive but they are still used as if they were just normal variables
	let stations = $state<Station[]>([]);
	let selected = $state<Station[]>([]);

	function countStationsPerState(stations: Station[]): [string, number][] {
		/* TODO
		Count the number of stations per unique state using the station data and replace the static values below.
		*/
		return [
			["Bayern", 100],
			["Baden-Württemberg", 61],
			["Niedersachsen", 44],
			["Nordrhein-Westfalen", 42],
			["Hessen", 36],
			["Sachsen", 29],
			["Thüringen", 28],
			["Rheinland-Pfalz", 25],
			["Mecklenburg-Vorpommern", 25],
			["Schleswig-Holstein", 25],
			["Brandenburg", 24],
			["Sachsen-Anhalt", 24],
			["Saarland", 7],
			["Berlin", 5],
			["Hamburg", 4],
			["Bremen", 2]
		];
	}

	function toggleSelection(station: Station) {
		/* TODO
		Implement this function to toggle the selection of the given station and replace the code below.
		*/
		selected = [station];
	}

	function selectStationsByState(state: string) {
		/* TODO
		Update the selected stations to the ones in the given state.
		*/
	}

	function resetSelection() {
		/* TODO
		Reset to the empty selection.
		*/
	}

	// this runs initially when the page loads
	$effect(() => {
		loadStations().then((data) => (stations = data));
	});
</script>

<main>
	<section>
		<h1>German Weather Stations</h1>
		<div id="selection">
			<p>{selected.length} of {stations.length} selected</p>
			<button disabled={selected.length === 0} onclick={resetSelection}>Reset</button>
		</div>
		<Barchart
			width={600}
			height={600}
			gap={2}
			data={countStationsPerState(stations)}
			onselect={(state) => selectStationsByState(state)}
		/>
	</section>

	<section id="map">
		<StationsMap
			width={600}
			height={800}
			{stations}
			bind:selected
			onselect={(station) => toggleSelection(station)}
		/>
	</section>

	{#each selected ?? stations as station (station.id)}
		<StationCard {station} />
	{/each}
</main>

<style>
	main {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
		gap: 1rem;
		max-width: 1280px;
		margin: 0 auto;
		padding: 1rem;
	}

	h1 {
		font-size: 2.6rem;
		text-align: center;
	}

	h2 {
		font-size: 2rem;
	}

	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-content: center;
		align-items: center;
		gap: 0.2rem;
	}

	#selection {
		display: flex;
		flex-direction: row;
		gap: 1rem;
		align-items: center;
	}
</style>
