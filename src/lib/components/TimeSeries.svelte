<script lang="ts">
	import * as d3 from "d3";

	let {
		width = 500,
		height = 100,
		data
	}: {
		width: number;
		height: number;
		data: [Date, number][];
	} = $props();

	const marginLeft = 10;
	const marginTop = 10;
	const marginRight = 10;
	const marginBottom = 10;

	const minDate = $derived(d3.min(data, (d) => d[0]) ?? new Date());
	const maxDate = $derived(d3.max(data, (d) => d[0]) ?? new Date());

	const minValue = $derived(d3.min(data, (d) => d[1]) ?? 0);
	const maxValue = $derived(d3.max(data, (d) => d[1]) ?? 0);

	function linePath(data: [Date, number][]): string {
		/*
		TODO: Create the line as a sequence of SVG path commands; see
		https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
		Map time to the x-axis and the temperature to the y-axis. Respect the
		margins that are set above.
		Replace the return value below that simply draws a line from bottom left to top right.
		*/
		return `M ${marginLeft} ${height - marginBottom} L ${width - marginRight} ${marginTop}`;
	}
</script>

<svg {width} {height}>
	<path id="line" d={linePath(data)} />
</svg>

<style>
	#line {
		stroke: var(--primary-color);
		fill: none;
		stroke-width: 1.5;
	}
</style>
