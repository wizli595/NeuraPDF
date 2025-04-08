<script lang="ts">
	import type { PageData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import PdfViewer from '$c/PdfViewer.svelte';
	import ChatPanel from '$c/chat/ChatPanel.svelte';
	import { fly } from 'svelte/transition';

	export let data: PageData;
	let currentTab: 'pdf' | 'chat' = 'pdf';

	const document = data.document;
	const documentUrl = data.documentUrl;

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming, documentId: document.id });
	}

	beforeNavigate(resetAll);
</script>

{#if data.error}
	<div
		in:fly={{ y: 20, duration: 400 }}
		class="w-full p-4 mb-6 rounded-xl bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 
		text-red-700 dark:text-red-300 shadow-lg"
	>
		<div class="flex items-center gap-3">
			<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
					d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
				/>
			</svg>
			<span class="font-medium">{data.error}</span>
		</div>
	</div>
{/if}

{#if document}
	<div class="h-full flex flex-col gap-4">
		<!-- Header -->
		<div class="flex justify-between items-center">
			<h1 class="text-xl font-semibold">{document.title || 'Document'}</h1>
			
			<!-- Switch Tabs -->
			<div class="inline-flex bg-gray-200 dark:bg-gray-700 rounded-md overflow-hidden">
				<button
					class="px-4 py-1 text-sm transition-colors duration-200"
					class:selected={currentTab === 'pdf'}
					on:click={() => currentTab = 'pdf'}
					class:bg-blue-500={currentTab === 'pdf'}
					class:text-white={currentTab === 'pdf'}
				>
					PDF
				</button>
				<button
					class="px-4 py-1 text-sm transition-colors duration-200"
					class:selected={currentTab === 'chat'}
					on:click={() => currentTab = 'chat'}
					class:bg-blue-500={currentTab === 'chat'}
					class:text-white={currentTab === 'chat'}
				>
					Chat
				</button>
			</div>
		</div>

		<!-- Panel Content -->
		<div class="flex-1 overflow-hidden rounded-lg shadow-md bg-white dark:bg-gray-800">
			{#if currentTab === 'pdf'}
				{#if documentUrl}
					<PdfViewer url={documentUrl} />
				{:else}
					<div class="p-6 text-center">Loading document...</div>
				{/if}
			{:else if currentTab === 'chat'}
				<ChatPanel onSubmit={handleSubmit} documentId={document.id} />
			{/if}
		</div>
	</div>
{/if}

<style>
	/* button.selected {
		@apply bg-blue-500 text-white;
	} */
</style>
