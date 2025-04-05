<script lang="ts">
	import { onMount } from 'svelte';
	import { errorStore, reset } from '$s/errors';
	import ErrorMessage from '$c/ErrorMessage.svelte';

	// Close modal on Escape key press
	const listener = (event: KeyboardEvent) => {
		if (event.key === 'Escape') {
			reset();
		}
	};

	// Add & remove event listener for Escape key
	onMount(() => {
		window.addEventListener('keydown', listener);
		return () => window.removeEventListener('keydown', listener);
	});
</script>

{#if $errorStore.errors.length}
	<!-- Dark Mode Overlay -->
	<button
		on:click={reset}
		on:keydown={(event) => (event.key === 'Enter' || event.key === ' ') && reset()}
		class="fixed inset-0 bg-black/50 dark:bg-black/60 backdrop-blur-sm z-40 transition-opacity"
		aria-label="Close overlay"
	/>

	<!-- Error Modal -->
	<div
		class="fixed right-0 top-0 bottom-0 w-full max-w-xl bg-white dark:bg-gray-800 shadow-2xl z-50 transform transition-transform animate-slide-in"
	>
		<div class="flex flex-col h-full">
			<!-- Modal Header -->
			<header class="p-6 bg-primary-600 dark:bg-primary-700">
				<div class="flex items-center justify-between">
					<h2 class="text-2xl font-semibold text-white">Error Details</h2>
					<button
						on:click={reset}
						class="text-white hover:text-gray-300 dark:hover:text-gray-400 transition-colors"
					>
						<!-- Close Icon -->
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-6 w-6"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				</div>
			</header>

			<!-- Error Messages -->
			<div class="flex-1 overflow-y-auto p-6">
				{#each $errorStore.errors as error}
					<div
						class="mb-4 p-4 bg-red-50 dark:bg-red-900 border border-red-200 dark:border-red-600 rounded-lg"
					>
						<p class="text-red-700 dark:text-red-300">{error.message}</p>
					</div>
				{/each}
			</div>
		</div>
	</div>
{/if}

<!-- Animations -->
<style>
	@keyframes slide-in {
		from {
			transform: translateX(100%);
			opacity: 0;
		}
		to {
			transform: translateX(0);
			opacity: 1;
		}
	}
	.animate-slide-in {
		animation: slide-in 0.3s ease-out;
	}
</style>
