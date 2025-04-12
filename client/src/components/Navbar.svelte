<script lang="ts">
	import AuthLinks from '$c/auth/AuthLinks.svelte';
	import { auth } from '$s/auth';
	import DarkModeToggle from '$c/DarkModeToggle.svelte';
	import { fly } from 'svelte/transition';
	import { page } from '$app/stores';
	import { derived } from 'svelte/store';
	import { goto } from '$app/navigation';

	$: user = $auth.user;
	const isSignupPage = derived(page, ($page) => $page.url.pathname === '/auth/signup');
	const isSigninPage = derived(page, ($page) => $page.url.pathname === '/auth/signin');

	const altAuthHref = derived(isSignupPage, ($isSignupPage) =>
		$isSignupPage ? '/auth/signin' : '/auth/signup'
	);
	const altAuthLabel = derived(isSignupPage, ($isSignupPage) =>
		$isSignupPage ? 'Sign In' : 'Sign Up'
	);
</script>

<header class="bg-white dark:bg-gray-900 shadow-sm transition-all">
	<nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
		<div class="flex justify-between h-16">
			<div class="flex items-center">
				<a href="/">
					<div
						class="text-2xl font-bold tracking-tight text-black flex items-center gap-2 dark:text-white"
					>
						<span class="material-icons text-yellow-300">auto_awesome</span>
						Neura<span class="text-yellow-300">PDF</span>
					</div>
				</a>

				<div class="hidden sm:ml-6 sm:flex sm:space-x-8">
					<a
						href="/"
						class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 dark:text-gray-200 border-b-2 border-transparent hover:border-primary-500 hover:text-primary-600 transition-colors"
					>
						Home
					</a>

					{#if user}
						<a
							href="/scores"
							class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 dark:text-gray-200 border-b-2 border-transparent hover:border-primary-500 hover:text-primary-600 transition-colors"
						>
							Scores
						</a>
						<a
							href="/documents"
							class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 dark:text-gray-200 border-b-2 border-transparent hover:border-primary-500 hover:text-primary-600 transition-colors"
						>
							Documents
						</a>
					{/if}
				</div>
			</div>

			<div class="flex items-center space-x-4">
				<!-- Dark Mode Toggle Button -->
				<DarkModeToggle />

				<div class="auth-buttons-container">
					{#if user}
						<button
							class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors"
							in:fly={{ y: -20, duration: 300 }}
							out:fly={{ y: 20, duration: 300 }}
							on:click={() => {
								goto('/auth/signout');
							}}
						>
							Sign Out
						</button>
					{:else}
						<a
							href={$altAuthHref}
							class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors"
							in:fly={{ y: -20, duration: 300 }}
							out:fly={{ y: 20, duration: 300 }}
						>
							{$altAuthLabel}
						</a>
					{/if}
				</div>
			</div>
		</div>
	</nav>
</header>

<style>
	.auth-buttons-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
	}

	.auth-buttons-container button,
	.auth-buttons-container a {
		transition: all 0.3s ease;
	}
</style>
