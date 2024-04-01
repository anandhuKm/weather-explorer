<script lang="ts">
	import Barchart from "$lib/components/Barchart.svelte";
	import StationsMap from "$lib/components/Map.svelte";
	import StationCard from "$lib/components/StationCard.svelte";
	import { loadStations, type Station } from "$lib/data";

	// the $state makes these variables reactive but they are still used as if they were just normal variables
	let stations = $state<Station[]>([]);
	let selected = $state<Station[]>([]);
	let stationSelected = $state<Station[]>([]);
	
	function countStationsPerState(stations: Station[]): [string, number][] {
		/* TODO
		Count the number of stations per unique state using the station data and replace the static values below.
		*/
		
		const stateCount:[string, number][] = [];
		let existingCheck
		stations.map(station =>{					 
			existingCheck = stateCount.findIndex(index => index[0] === station.state)
			existingCheck === -1 ? stateCount.push([station.state,1]) : //add station 
			stateCount[existingCheck][1]++;    // else increment state number

		}); 
		return stateCount

		/*return [
			["Bayern", 1],
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
		]; */
	}

	function toggleSelection(station: Station) {
		/* TODO
		Implement this function to toggle the selection of the given station and replace the code below.
		*/

		if(stationSelected) {
			const active = stationSelected.findIndex(index => index.id === station.id)
			stationSelected = active !== -1 ? stationSelected.filter(f => f.id !== station.id) :
			[...stationSelected,station];	
		} else {
			stationSelected = [station];	
		}
	}

	function selectStationsByState(state: string) {
		/* TODO
		Update the selected stations to the ones in the given state.
		*/

		selected = []; 
		stationSelected = [];
			stations.map(station =>{		
				station.state === state ? selected.push(station) : null 
			});
	}

	function resetSelection() {
		/* TODO
		Reset to the empty selection.
		*/
		selected = [];
		stationSelected = [];
	}

	function allSelection() {
		/* TODO
		Select all the stations in Germany to view multiple state sations.
		*/
		selected = [];
		stations.map(station =>{		
				selected.push(station)
			});
			
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
			<button  onclick={allSelection}>Select All</button>
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
			stations ={selected}
			bind:selected
			onselect={(station) => toggleSelection(station)}
		/>
	</section>

	{#each stationSelected ?? stations as station (station.id)}
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
