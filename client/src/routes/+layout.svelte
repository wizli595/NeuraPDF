<script lang="ts">
	import '../app.css';
	import 'material-icons/iconfont/material-icons.css';
	import { onMount } from 'svelte';
	import Navbar from '$c/Navbar.svelte';
	import ErrorModal from '$c/ErrorModal.svelte';
	import { getUser, auth } from '$s/auth';
	import { writable } from 'svelte/store';

	export const ssr = false;

	$: user = $auth.user;

	onMount(() => {
		if (user === null) {
			getUser();
		}
	});

	// Dark Mode State
	let darkMode = writable(false);

	// Load theme from localStorage
	onMount(() => {
		const isDark = localStorage.getItem('theme') === 'dark';
		darkMode.set(isDark);
		document.documentElement.classList.toggle('dark', isDark);
	});
</script>

<ErrorModal />

<!-- Standardized Page Layout with Dark Mode Support -->
<div class="min-h-screen flex flex-col bg-gray-100 dark:bg-gray-900 transition-all">
	<!-- Navigation -->
	<Navbar />

	<!-- Main Content -->
	<main class="flex-grow flex items-center justify-center">
		<div
			class="w-full max-w-4xl p-6 sm:p-10 bg-white dark:bg-gray-800 shadow-lg rounded-xl border border-gray-200 dark:border-gray-700 transition-all"
		>
			<div class="text-center mb-6">
				<h1 class="text-4xl font-extrabold text-gray-900 dark:text-white">Welcome</h1>
				<p class="text-gray-600 dark:text-gray-400 mt-2">Your modern application layout</p>
			</div>

			<div class="mt-6">
				<slot />
			</div>
		</div>
	</main>

	<!-- Footer -->
	<footer
		class="w-full text-center py-4 text-gray-500 dark:text-gray-300 text-sm bg-white dark:bg-gray-800 border-t dark:border-gray-700 transition-all"
	>
		© {new Date().getFullYear()} Your Company. All rights reserved.
	</footer>
</div>
