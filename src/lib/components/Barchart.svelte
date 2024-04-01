<script lang="ts">
	let {
		width = 600,
		height = 600,
		gap = 2,
		data,
		onselect
	}: {
		width: number;
		height: number;
		gap: number;
		data: [string, number][];
		onselect?: (name: string, value: number) => void;
	} = $props();

	const marginLeft = 10;
	const marginTop = 10;
	const marginRight = 120;
	const marginBottom = 10;

	let barHeight = $derived(
		(height - marginTop - marginBottom - (data.length - 1) * gap) / data.length
	);

	function computeBarWidth(value: number): number {
		/*
		TODO
		Compute the width of the bar for the given value and replace the dummy return value below.
		*/
		// barwidth = value / max value * available width
		return (value / 100 ) * ( width - marginLeft - marginRight )

	}
</script>

<svg {width} {height}>
	{#each data as [name, value], ix (name)}
		{@const barWidth = computeBarWidth(value)}
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<!-- svelte-ignore a11y-no-static-element-interactions -->
		<g
			transform="translate({marginLeft},{marginTop + (barHeight + gap) * ix})"
			onclick={() => (onselect ? onselect(name, value) : undefined)}
		>
			<rect width={barWidth} height={barHeight} />
			<text x={barWidth} y={barHeight / 2} dx="0.2em" dy="0.3em">
				<tspan class="name">{name}</tspan> <tspan class="value">({value})</tspan>
			</text>
		</g>
	{/each}
</svg>

<style>
	g {
		color: var(--primary-color);
	}

	rect {
		fill: currentColor;
	}

	text {
		fill: currentColor;
		user-select: none;
	}

	g:hover {
		color: var(--highlight-color);
		cursor: pointer;
	}

	tspan.value {
		opacity: 0.5;
		color: black;
	}
	tspan.name:hover {
		color: black;
	}
</style>
