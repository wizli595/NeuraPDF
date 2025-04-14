<script lang="ts">
	import { marked } from 'marked';
	import classnames from 'classnames';
	import { scoreConversation } from '$s/chat';
	import Icon from '$c/Icon.svelte';

	export let content = '';
	let score = 0;

	const klass = 'border rounded-full inline-block cursor-pointer hover:bg-slate-200';
	$: upKlass = classnames(klass, {
		'bg-slate-200': score === 1
	});
	$: downKlass = classnames(klass, {
		'bg-slate-200': score === -1
	});

	async function applyScore(_score: number) {
		if (score !== 0) {
			return;
		}
		score = _score;
		return scoreConversation(_score);
	}
</script>

<div class="flex flex-row items-center justify-between">
	<div
		class="message border rounded-md py-1.5 px-2.5 my-0.25 break-words self-start bg-blue-500 text-gray-100"
	>
		{@html marked(content, { breaks: true, gfm: true })}
	</div>
	<div class="flex flex-row items-start gap-3 justify-center mt-2">
		{#if score >= 0}
			<button
				on:click={() => applyScore(1)}
				class={`group relative flex items-center justify-center 
					w-10 h-10 rounded-full 
					transition-all duration-300 ease-in-out
					${score === 1 ? 'bg-blue-500 shadow-lg scale-105' : 'hover:bg-blue-500 bg-transparent'}`}
			>
				<Icon
					name="thumb_up"
					outlined
					classN={`transition-all duration-300 ease-in-out
						${score === 1 ? 'text-white' : 'text-blue-500 group-hover:text-white'} 
						group-hover:scale-125 group-hover:-rotate-6 group-active:scale-95`}
					size="20px"
				/>
			</button>
		{/if}

		{#if score <= 0}
			<button
				on:click={() => applyScore(-1)}
				class={`group relative flex items-center justify-center 
					w-10 h-10 rounded-full 
					transition-all duration-300 ease-in-out
					${score === -1 ? 'bg-red-500 shadow-lg scale-105' : 'hover:bg-red-500 bg-transparent'}`}
			>
				<Icon
					name="thumb_down"
					outlined
					classN={`transition-all duration-300 ease-in-out
						${score === -1 ? 'text-white' : 'text-red-500  group-hover:text-white'} 
						group-hover:scale-125 group-hover:rotate-6 group-active:scale-95`}
					size="20px"
				/>
			</button>
		{/if}
	</div>
</div>

<style>
	.message {
		max-width: 80%;
	}
</style>
