<!-- ChatPanel.svelte -->
<script lang="ts">
	import { onMount } from 'svelte';
	import {
		store,
		resetError,
		fetchConversations,
		createConversation,
		getActiveConversation
	} from '$s/chat';
	import Alert from '$c/Alert.svelte';
	import ChatInput from '$c/chat/ChatInput.svelte';
	import ChatList from '$c/chat/ChatList.svelte';
	import ConversationSelect from '$c/chat/ConversationSelect.svelte';

	export let onSubmit: (text: string, useStreaming: boolean) => void;
	export let documentId: number;

	let useStreaming = !!localStorage.getItem('streaming');

	$: localStorage.setItem('streaming', useStreaming ? 'true' : '');
	$: activeConversation = $store.activeConversationId ? getActiveConversation() : null;

	function handleSubmit(event: CustomEvent<string>) {
		if (onSubmit) {
			onSubmit(event.detail, useStreaming);
		}
	}

	function handleNewChat() {
		createConversation(documentId);
	}

	onMount(() => {
		fetchConversations(documentId);
	});
</script>

<!-- Panel Container -->
<div
	class="flex flex-col h-full rounded-xl border text-black dark:text-white border-white/20 dark:border-slate-700/40
	bg-white/80 dark:bg-slate-900/70 backdrop-blur-md shadow-2xl overflow-hidden
	transition-all duration-300 hover:shadow-blue-500/5 dark:hover:shadow-blue-400/5"
>
	<!-- Header -->
	<header
		class="flex justify-between items-center px-4 py-3 border-b border-white/20 dark:border-slate-700/40"
	>
		<!-- <div class="flex items-center gap-2 opacity-70">
			<input id="chat-type" type="checkbox" bind:checked={useStreaming} />
			<label for="chat-type" class="italic">Streaming</label>
		</div> -->

		<label class="relative inline-flex items-center cursor-pointer group select-none">
			<input id="chat-type" type="checkbox" class="sr-only peer" bind:checked={useStreaming} />

			<div
				class="w-11 h-6 bg-gray-300 peer-focus:ring-2 peer-focus:ring-blue-400 dark:peer-focus:ring-blue-500 rounded-full peer dark:bg-gray-700 peer-checked:bg-blue-600 transition-all duration-300"
			/>

			<span
				class="absolute left-0.5 top-0.5 w-5 h-5 bg-white border border-gray-300 rounded-full transition-transform duration-300 peer-checked:translate-x-5 shadow"
			/>

			<span
				class="ml-3 text-sm italic text-gray-700 dark:text-gray-300 group-hover:text-blue-500 transition"
			>
				Streaming
			</span>
		</label>
		<div class="flex gap-2 items-center">
			<ConversationSelect conversations={$store.conversations} />
			<button
				class="border border-blue-500 text-xs px-2 py-1 rounded hover:bg-blue-100 dark:hover:bg-blue-900 transition"
				on:click={handleNewChat}
			>
				New Chat
			</button>
		</div>
	</header>

	<!-- Messages -->
	<section class="flex-1 overflow-y-auto px-4 py-3 space-y-3 custom-scrollbar">
		<ChatList messages={activeConversation?.messages || []} />
		{#if $store.error && $store.error.length < 200}
			<Alert type="error" onDismiss={resetError} />
		{/if}
	</section>

	<!-- Footer / Input -->
	<footer
		class="border-t border-white/20 dark:border-slate-700/40 px-4 py-3 text-black dark:text-white"
	>
		<ChatInput on:submit={handleSubmit} />
	</footer>
</div>

<style>
	.custom-scrollbar::-webkit-scrollbar {
		width: 6px;
	}
	.custom-scrollbar::-webkit-scrollbar-track {
		background: transparent;
	}
	.custom-scrollbar::-webkit-scrollbar-thumb {
		background-color: rgba(100, 100, 100, 0.3);
		border-radius: 10px;
	}
</style>
