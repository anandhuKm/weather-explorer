<script lang="ts">
	import * as d3 from "d3";
	import type { Station } from "$lib/data";
	import germanyGeoJson from "$lib/assets/germany.geo.json";

	const germany = germanyGeoJson as GeoJSON.FeatureCollection;

	let {
		width = 600,
		height = 800,
		stations = [],
		selected = [],
		onselect
	}: {
		width: number;
		height: number;
		stations: Station[];
		selected: Station[];
		onselect: (station: Station) => void;
	} = $props();

	const padding = 10;

	const computeProjection = () => {
		const [[left, bottom], [right, top]] = d3.geoBounds(germany);
		const rotation = -(right + left) / 2;
		return d3
			.geoConicEqualArea()
			.parallels([bottom, top])
			.translate([width / 4, height / 2])
			.rotate([rotation, 0, 0])
			.fitExtent(
				[
					[padding, padding],
					[width - padding, height - padding]
				],
				germany
			);
	};

	let projection = $derived(computeProjection());
	let path = $derived(d3.geoPath().projection(projection));
</script>

<svg role="img" {width} {height}>
	{#each germany.features as feature (feature.properties?.id)}
		<path class="state" d={path(feature)} />
	{/each}

	{#each stations as station (station.id)}
		<g transform="translate({projection([station.longitude, station.latitude])!.join(',')})">
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<!-- svelte-ignore a11y-no-static-element-interactions -->
			<circle
				class="station"
				r={5}
				onclick={() => onselect && onselect(station)}
				class:selected={selected.map((s) => s.id).includes(station.id)}
			>
				<title>{station.name}</title>
			</circle>
		</g>
	{/each}
</svg>

<style>
	.state {
		fill: var(--light-color);
		stroke: white;
		stroke-width: 1.5px;
	}

	.station {
		fill: var(--primary-color);
		opacity: 0.7;
	}
</style>
