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

	// color encoding in circles
	const color = d3.scaleSequential().domain([0, 2500]).interpolator(d3.interpolateTurbo);

	const colors = d3.range(0, 2500, 10).map((x) => color(x));
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
				class:station
				r={5}
				fill={color(station.height)}
				onclick={() => {
					onselect && onselect(station);
				}}
				class:selected={selected.map((s) => s.id).includes(station.id)}
			>
				<title>{station.name}</title>
			</circle>
		</g>
	{/each}

	<!-- TURBOCOLOR gradient map -->
	<defs>
		<linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
			{#each colors as color, index}
				<stop offset="{(index / (colors.length - 1)) * 100}%" stop-color={color} />
			{/each}
		</linearGradient>
	</defs>
	<rect x={30} y={height - 5} width="480" height="20" fill="url(#gradient)" />
	<text x="30" y={height - 15} dy="0.32em" text-anchor="start">Minimum Height</text>
	<text x="510" y={height - 15} dy="0.32em" text-anchor="end">Maximum Height</text>
</svg>

<style>
	.state {
		fill: var(--light-color);
		stroke: white;
		stroke-width: 1.5px;
	}

	.station {
		opacity: 0.7;
		cursor: pointer;
	}

	.station:hover {
		fill: black;
		opacity: 0.7;
		cursor: pointer;
	}
</style>
