<script lang="ts">
	import type { PageData } from './$types';
	import AuthGuard from '$c/AuthGuard.svelte';
	import { fade, fly, scale } from 'svelte/transition';
	import { elasticOut } from 'svelte/easing';

	export let data: PageData;

	const documents = data.documents || [];
	console.log(documents);
</script>

<AuthGuard />

<!-- Enhanced Header with Animations -->
<div
	class="flex flex-col md:flex-row justify-between items-center gap-6 my-8 max-w-6xl"
	in:fly={{ y: -20, duration: 800, delay: 200 }}
>
	<div class="flex items-center gap-4">
		<div class="relative" in:scale={{ duration: 600, delay: 400, easing: elasticOut }}>
			<div
				class="absolute inset-0 animate-ping-slow rounded-full bg-blue-400/20 dark:bg-blue-500/20"
			/>
			<div
				class="relative w-12 h-12 flex items-center justify-center rounded-xl bg-gradient-to-br from-blue-500 to-indigo-500 text-white shadow-lg"
			>
				📄
			</div>
		</div>
		<h2
			class="text-3xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400"
		>
			Your Documents
		</h2>
	</div>

	<div class="flex items-center gap-4">
		<a
			href="/documents/new"
			class="group relative px-6 py-3 font-semibold text-white rounded-xl
			bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500
			shadow-lg hover:shadow-xl hover:shadow-blue-500/20 dark:hover:shadow-blue-400/20
			transform hover:-translate-y-0.5 transition-all duration-300"
			in:fly={{ x: 20, duration: 800, delay: 600 }}
		>
			<span class="relative flex items-center gap-2">
				<span class="text-2xl group-hover:rotate-12 transition-transform duration-300">➕</span>
				<span>New Document</span>
			</span>
		</a>
	</div>
</div>

<!-- Enhanced Table with Animations -->
<div
	class="relative rounded-2xl overflow-hidden bg-white/80 dark:bg-gray-800/80 backdrop-blur-lg
	shadow-2xl border border-white/20 dark:border-gray-700/30 transition-all duration-300"
	in:fly={{ y: 20, duration: 800, delay: 400 }}
>
	<div class="overflow-x-auto">
		<table class="w-full">
			<thead>
				<tr class="border-b border-gray-200 dark:border-gray-700">
					<th class="px-6 py-4 text-left">
						<span
							class="text-xs font-semibold tracking-wider uppercase
						bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400
						bg-clip-text text-transparent"
						>
							Name
						</span>
					</th>
					<th class="px-6 py-4 text-left">
						<span
							class="text-xs font-semibold tracking-wider uppercase
						bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400
						bg-clip-text text-transparent"
						>
							ID
						</span>
					</th>
					<th class="px-6 py-4 text-right">
						<span
							class="text-xs font-semibold tracking-wider uppercase
						bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400
						bg-clip-text text-transparent"
						>
							Action
						</span>
					</th>
				</tr>
			</thead>
			<tbody class="divide-y divide-gray-200 dark:divide-gray-700">
				{#each documents as document, i (document.id)}
					<tr
						in:fly={{ y: 20, duration: 400, delay: 200 + i * 100 }}
						class="group hover:bg-blue-50/50 dark:hover:bg-blue-900/20 transition-all duration-300"
					>
						<td class="px-6 py-4">
							<div class="flex items-center gap-3">
								<div
									class="w-8 h-8 rounded-lg bg-blue-100 dark:bg-blue-900/50
								flex items-center justify-center text-blue-600 dark:text-blue-400
								group-hover:scale-110 transition-transform duration-300"
								>
									📄
								</div>
								<span class="font-medium text-gray-900 dark:text-gray-100">
									{document.name}
								</span>
							</div>
						</td>
						<td class="px-6 py-4">
							<span class="text-sm text-gray-600 dark:text-gray-400 font-mono">
								{document.id}
							</span>
						</td>
						<td class="px-6 py-4 text-right">
							<a
								href={`/documents/${document.id}`}
								class="inline-flex items-center gap-2 text-blue-600 hover:text-blue-800
								dark:text-blue-400 dark:hover:text-blue-300 font-medium
								group-hover:translate-x-1 transition-all duration-300"
							>
								View
								<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor">
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 5l7 7-7 7"
									/>
								</svg>
							</a>
						</td>
					</tr>
				{/each}
				{#if documents.length === 0}
					<tr in:scale={{ duration: 400, delay: 200 }} class="relative">
						<td colspan="3" class="py-16 text-center">
							<div class="flex flex-col items-center gap-4">
								<div class="text-6xl animate-bounce">📭</div>
								<p class="text-lg text-gray-500 dark:text-gray-400">No documents found yet</p>
								<a
									href="/documents/new"
									class="mt-2 px-6 py-2 text-sm font-medium text-blue-600 hover:text-blue-800
									dark:text-blue-400 dark:hover:text-blue-300
									border-2 border-blue-600 dark:border-blue-400 rounded-full
									hover:bg-blue-50 dark:hover:bg-blue-900/20
									transition-all duration-300"
								>
									Create your first document
								</a>
							</div>
						</td>
					</tr>
				{/if}
			</tbody>
		</table>
	</div>
</div>

<style>
	@keyframes ping-slow {
		75%,
		100% {
			transform: scale(2);
			opacity: 0;
		}
	}

	:global(.animate-ping-slow) {
		animation: ping-slow 2s cubic-bezier(0, 0, 0.2, 1) infinite;
	}
</style>
