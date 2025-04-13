<script lang="ts">
	import type { PageData } from './$types';
	import BarChart from '$c/BarChart.svelte';
	import AuthGuard from '$c/AuthGuard.svelte';
	import { fade, scale } from 'svelte/transition';

	export let data: PageData;
	console.log(data.scores);

	$: llmScores = data.scores && data.scores['llm'];
	$: retrieverScores = data.scores && data.scores['retriever'];
	$: memoryScores = data.scores && data.scores['memory'];
	console.log(llmScores);
	function fadeAndScale(node: Element, params: any) {
		const f = fade(node, params);
		const s = scale(node, params);

		return {
			delay: params?.delay || 0,
			duration: params?.duration || 400,
			css: (t: number) => `${f.css?.(t, params) || ''} ${s.css?.(t, params) || ''}`
		};
	}
</script>

<AuthGuard />

<div class="flex flex-col items-center gap-10 p-6 max-w-6xl mx-auto">
	<div
		in:fadeAndScale={{ duration: 500 }}
		class="w-full md:w-3/4 bg-white shadow-lg rounded-2xl p-6"
	>
		<h2 class="text-3xl font-bold text-gray-800 mb-4">LLM Scores</h2>
		{#if llmScores}
			<BarChart startingColor={{ r: 0, g: 99, b: 132 }} data={llmScores} />
		{/if}
	</div>

	<div
		in:fadeAndScale={{ duration: 500, delay: 100 }}
		class="w-full md:w-3/4 bg-white shadow-lg rounded-2xl p-6"
	>
		<h2 class="text-3xl font-bold text-gray-800 mb-4">Retriever Scores</h2>
		{#if retrieverScores}
			<BarChart startingColor={{ r: 255, g: 99, b: 132 }} data={retrieverScores} />
		{/if}
	</div>

	<div
		in:fadeAndScale={{ duration: 500, delay: 200 }}
		class="w-full md:w-3/4 bg-white shadow-lg rounded-2xl p-6"
	>
		<h2 class="text-3xl font-bold text-gray-800 mb-4">Memory Scores</h2>
		{#if memoryScores}
			<BarChart startingColor={{ r: 30, g: 200, b: 60 }} data={memoryScores} />
		{/if}
	</div>
</div>
