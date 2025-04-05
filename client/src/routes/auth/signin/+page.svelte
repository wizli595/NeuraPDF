<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import TextInput from '$c/TextInput.svelte';
	import Button from '$c/Button.svelte';
	import FormGroup from '$c/FormGroup.svelte';
	import { auth, signin, clearErrors } from '$s/auth';
	import Alert from '$c/Alert.svelte';

	let email = '';
	let password = '';

	function handleSubmit() {
		signin(email, password);
	}

	$: if ($auth.user) {
		goto('/');
	}

	beforeNavigate(clearErrors);
</script>

<!-- Page Wrapper: Ensures Full Page Centering -->
<div
	class="flex items-center justify-center p-5 bg-gray-100 dark:bg-gray-900 transition-all rounded-md"
>
	<!-- Sign-in Box -->
	<div
		class="w-full max-w-md p-8 bg-white dark:bg-gray-800 shadow-lg dark:shadow-xl rounded-xl border border-gray-200 dark:border-gray-700 transition-all"
	>
		<!-- Sign-in Header -->
		<div class="text-center">
			<h2 class="text-3xl font-extrabold text-gray-900 dark:text-white">Sign in to your account</h2>
			<p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
				Don't have an account?
				<a
					href="/auth/signup"
					class="font-medium text-primary-600 dark:text-primary-400 hover:text-primary-500"
				>
					Sign up
				</a>
			</p>
		</div>

		<!-- Sign-in Form -->
		<form class="mt-6 space-y-5" on:submit|preventDefault={handleSubmit}>
			<FormGroup label="Email address">
				<TextInput
					type="email"
					bind:value={email}
					className="dark:bg-gray-700 dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500"
				/>
			</FormGroup>

			<FormGroup label="Password">
				<TextInput
					type="password"
					bind:value={password}
					className="dark:bg-gray-700 dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500"
				/>
			</FormGroup>

			{#if $auth.error}
				<Alert type="error">{$auth.error}</Alert>
			{/if}

			<Button
				className="w-full bg-primary-600 dark:bg-primary-700 text-white py-3 rounded-md shadow-md hover:bg-primary-700 dark:hover:bg-primary-800 transition-all"
			>
				Sign in
			</Button>
		</form>
	</div>
</div>
