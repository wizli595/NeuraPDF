<script lang="ts">
	import AuthLinks from '$c/auth/AuthLinks.svelte';
	import { auth } from '$s/auth';
	import DarkModeToggle from '$c/DarkModeToggle.svelte';

	$: user = $auth.user;
</script>

<header class="bg-white dark:bg-gray-900 shadow-sm transition-all">
	<nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
		<div class="flex justify-between h-16">
			<div class="flex items-center">
				<a href="/" class="flex-shrink-0 flex items-center">
					<span class="text-2xl font-bold text-primary-600 dark:text-white">NeuraPDF </span>
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

				{#if user}
					<button
						class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors"
					>
						Sign Out
					</button>
				{:else}
					<a
						href="/auth/signin"
						class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors"
					>
						Sign In
					</a>
				{/if}
			</div>
		</div>
	</nav>
</header>
