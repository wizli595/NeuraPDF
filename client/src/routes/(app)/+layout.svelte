<script lang="ts">
	import '../../app.css';
	import 'material-icons/iconfont/material-icons.css';
	import { onMount } from 'svelte';
	import Navbar from '$c/Navbar.svelte';
	import ErrorModal from '$c/ErrorModal.svelte';
	import { getUser, auth } from '$s/auth';
	import { writable } from 'svelte/store';
	import { fade, fly } from 'svelte/transition';

	$: user = $auth.user;

	onMount(() => {
		if (user === null) {
			getUser();
		}
	});

	let darkMode = writable(false);
	onMount(() => {
		const isDark = localStorage.getItem('theme') === 'dark';
		darkMode.set(isDark);
		document.documentElement.classList.toggle('dark', isDark);
	});
</script>

<ErrorModal />

<div class="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 via-gray-100 to-gray-200 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 transition-all duration-500">

	<div in:fly={{ y: -20, duration: 800 }}>
		<Navbar />
	</div>

	<main in:fade={{ duration: 500, delay: 200 }} class="flex-grow  p-6 overflow-hidden">
		{#each Array(3) as _, i}
			<div
				class="absolute rounded-full mix-blend-multiply dark:mix-blend-soft-light filter blur-3xl opacity-[0.15] dark:opacity-[0.07] animate-float"
				style="
					width: {300 + i * 100}px;
					height: {300 + i * 100}px;
					background: {['#60A5FA', '#818CF8', '#A78BFA'][i]};
					animation-delay: {i * -3}s;
					top: {20 + i * 25}%;
					left: {15 + i * 20}%;
					z-index: 0;
				"
			/>
		{/each}

		<div class="w-full max-w-4xl mx-auto relative z-10 " in:fly={{ y: 20, duration: 800, delay: 400 }}>
			<div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-lg shadow-2xl rounded-2xl 
				border border-white/20 dark:border-gray-700/30 transition-all duration-300
				hover:shadow-blue-500/5 dark:hover:shadow-blue-400/5 p-5">
				<slot />
			</div>
		</div>
	</main>

	<footer class="bg-gray-900 text-gray-400 border-t border-gray-700 px-4 py-6">
		<div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
			<div class="text-sm">© {new Date().getFullYear()} Your Company. All rights reserved.</div>
			<div class="flex space-x-6">
				<a href="/about" class="hover:text-white transition">About</a>
				<a href="/privacy" class="hover:text-white transition">Privacy</a>
				<a href="/terms" class="hover:text-white transition">Terms</a>
			</div>
		</div>
	</footer>
</div>

<style>
	@keyframes float {
		0% { transform: translateY(0px) scale(1); }
		50% { transform: translateY(-20px) scale(1.05); }
		100% { transform: translateY(0px) scale(1); }
	}
	:global(.animate-float) {
		animation: float 15s ease-in-out infinite;
	}
</style>
