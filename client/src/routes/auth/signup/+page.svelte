<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import TextInput from '$c/TextInput.svelte';
	import Button from '$c/Button.svelte';
	import FormGroup from '$c/FormGroup.svelte';
	import { auth, signup, clearErrors } from '$s/auth';
	import Alert from '$c/Alert.svelte';

	let email = '';
	let password = '';
	let passwordConfirm = '';

	function handleSubmit() {
		if (password !== passwordConfirm) {
			return alert('Passwords do not match');
		}
		signup(email, password);
	}

	$: if ($auth.user) {
		goto('/');
	}

	beforeNavigate(clearErrors);
</script>

<div class="w-full flex items-center justify-center">
	<div
		class="w-full max-w-md p-8 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 shadow-lg rounded-2xl transition-all"
	>
		<div class="text-center">
			<h1 class="text-3xl font-extrabold text-gray-900 dark:text-white">Create an Account</h1>
			<p class="mt-2 text-gray-600 dark:text-gray-400">
				Already have an account?
				<a href="/auth/signin" class="text-blue-600 font-medium hover:underline">Sign In</a>
			</p>
		</div>

		<div class="mt-6">
			<form on:submit|preventDefault={handleSubmit} class="space-y-5">
				<FormGroup label="Email">
					<TextInput
						bind:value={email}
						type="email"
						className="focus:ring-blue-500 focus:border-blue-500"
					/>
				</FormGroup>

				<FormGroup label="Password">
					<TextInput
						bind:value={password}
						type="password"
						className="focus:ring-blue-500 focus:border-blue-500"
					/>
				</FormGroup>

				<FormGroup label="Confirm Password">
					<TextInput bind:value={passwordConfirm} type="password" />
				</FormGroup>

				{#if $auth.error}
					<Alert>Error: {$auth.error}</Alert>
				{/if}

				<Button>Sign Up</Button>
			</form>
		</div>
	</div>
</div>
