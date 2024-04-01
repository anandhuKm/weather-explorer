<script lang="ts">
	import * as d3 from "d3";
	import { Date } from "svelte/reactivity";

	let {
		width = 500,
		height = 100,
		data
	}: {
		width: number;
		height: number;
		data: [Date, number][];
	} = $props();

	const marginLeft = 40;
	const marginTop = 10;
	const marginRight = 10;
	const marginBottom = 20;

	const minDate = $derived(d3.min(data, (d) => d[0]) ?? new Date());
	const maxDate = $derived(d3.max(data, (d) => d[0]) ?? new Date());

	const minValue = $derived(d3.min(data, (d) => d[1]) ?? 0);
	const maxValue = $derived(d3.max(data, (d) => d[1]) ?? 0);

	const minTempDate = data.find(d => d[1] == minValue);
	const maxTempDate = data.find(d => d[1] == maxValue);

	const timeScale = d3.scaleLinear()
        	.domain([minDate,maxDate])
    		.range([marginLeft, width - marginRight]);

	const tempScale = d3.scaleLinear()
       		.domain([minValue, maxValue])
        	.range([height - marginBottom-5, marginTop]);
	
	function linePath(data: [Date, number][]): string {
		/*
		TODO: Create the line as a sequence of SVG path commands; see
		https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
		Map time to the x-axis and the temperature to the y-axis. Respect the
		margins that are set above.
		Replace the return value below that simply draws a line from bottom left to top right.
		*/
    	const pathCommands = data.map(([date, value]) => {
        	const x = timeScale(date)
        	const y = tempScale(value);
        	return `${x},${y}`;
   		 });
    	const path = `M${pathCommands.join('L')}`;
    	return path;
		//return `M ${marginLeft} ${height - marginBottom} L ${width - marginRight} ${marginTop}`;
	}
</script>

<svg {width} {height}>
	
    <!-- X-axis -->
    <g transform="translate(0, ${height})">
        <line x1="{marginLeft-10}" y1="{height-marginBottom}" x2={width} y2="{height-marginBottom}" class="axis" />

		<g transform="translate(0, -5)">
            <text x={timeScale(minDate)} y="{height}" text-anchor="start">{d3.timeFormat("%b %Y")(minDate)}</text>
			<text x={timeScale(maxDate)} y="{height}" text-anchor="end">{d3.timeFormat("%b %Y")(maxDate)}</text>
        </g>
    </g>

    <!-- Y-axis -->
    <g transform="translate(30, 0)">
        <line x1="{0}" y1="0" x2="{0}" y2={height-marginBottom} class="axis" />

        <g transform="translate(0, 0)">
            {#each tempScale.ticks() as tick}
			<line x1="-5" y1={tempScale(tick)} x2="0" y2={tempScale(tick)} id="axis" />
                <text x="-5" y={tempScale(tick)} dy="0.32em" text-anchor="end">{tick}</text>
            {/each}
        </g>
    </g>

    <!-- Line path -->
	<path id="line" d="{linePath(data)}"/>

	<!-- Minimum and Maximum temperature -->
	<circle cx={timeScale(minTempDate[0])} cy={tempScale(minValue)} r="3" fill="red" ></circle>
	<text x={timeScale(minTempDate[0])+5} y={tempScale(minValue)}>{minValue}</text>

	<circle cx={timeScale(maxTempDate[0])} cy={tempScale(maxValue)} r="3" fill="red" ></circle>
	<text x={timeScale(maxTempDate[0])+5} y={tempScale(maxValue)+5}>{maxValue}</text>

</svg>


<style>
	#line {
		stroke: var(--primary-color);
		fill: none;
		stroke-width: 1.5;
	}
	.axis {
		stroke:black;
		stroke-width:1;
	}
</style>
