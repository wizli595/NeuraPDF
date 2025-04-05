<script lang="ts">
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store';

	let darkMode = writable(false);

	// Load theme from localStorage on mount
	onMount(() => {
		const isDark = localStorage.getItem('theme') === 'dark';
		darkMode.set(isDark);
		document.documentElement.classList.toggle('dark', isDark);
	});

	// Function to toggle dark mode
	function toggleDarkMode() {
		darkMode.update((prev) => {
			const newMode = !prev;
			localStorage.setItem('theme', newMode ? 'dark' : 'light');
			document.documentElement.classList.toggle('dark', newMode);
			return newMode;
		});
	}
</script>

<!-- Dark Mode Toggle Button -->
<button on:click={toggleDarkMode}>
	{#if $darkMode}
		<!-- Heroicons Sun -->
		<svg class="w-6 h-6 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
			<circle cx="12" cy="12" r="5" stroke-width="2" fill="none" />
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M12 2v2m0 16v2m8-10h-2m-12 0H2m15.071-7.071l-1.414 1.414M6.343 6.343L4.929 4.929m12.728 12.728l1.414 1.414M6.343 17.657l-1.414 1.414"
			/>
		</svg>
	{:else}
		<!-- Heroicons Moon -->
		<svg
			class="w-6 h-6 text-gray-900 dark:text-gray-100"
			fill="none"
			stroke="currentColor"
			viewBox="0 0 24 24"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M21 12.79A9 9 0 0112.79 3 7 7 0 1021 12.79z"
			/>
		</svg>
	{/if}
</button>
