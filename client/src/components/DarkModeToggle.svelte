<script lang="ts">
	import { onMount, tick } from 'svelte';
	import { writable } from 'svelte/store';
	import { scale, fade } from 'svelte/transition';
	import { cubicOut, elasticOut } from 'svelte/easing';
	import { Sun, Moon, Monitor } from 'lucide-svelte';

	const darkMode = writable(false);

	let isAnimating = false;
	let showRipple = false;
	let rippleX = 0;
	let rippleY = 0;

	let userPrefersDark = false;
	let systemPrefersDark = false;

	onMount(() => {
		const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
		systemPrefersDark = mediaQuery.matches;

		mediaQuery.addEventListener('change', (e) => {
			systemPrefersDark = e.matches;
			if (!userPrefersDark) {
				darkMode.set(systemPrefersDark);
				applyTheme(systemPrefersDark);
			}
		});

		const storedTheme = localStorage.getItem('theme');
		if (storedTheme) {
			userPrefersDark = true;
			const isDark = storedTheme === 'dark';
			darkMode.set(isDark);
			applyTheme(isDark);
		} else {
			darkMode.set(systemPrefersDark);
			applyTheme(systemPrefersDark);
		}
	});

	function applyTheme(isDark: boolean) {
		document.documentElement.classList.toggle('dark', isDark);
		const metaThemeColor = document.querySelector('meta[name="theme-color"]');
		if (metaThemeColor) {
			metaThemeColor.setAttribute('content', isDark ? '#1f2937' : '#ffffff');
		}
		document.documentElement.style.setProperty('--text-primary', isDark ? '#f3f4f6' : '#1f2937');
		document.documentElement.style.setProperty('--bg-primary', isDark ? '#1f2937' : '#ffffff');
	}

	async function toggleDarkMode(event: MouseEvent) {
		if (isAnimating) return;
		isAnimating = true;
		userPrefersDark = true;

		const button = event.currentTarget;
		const rect = (button as HTMLButtonElement).getBoundingClientRect();
		rippleX = event.clientX - rect.left;
		rippleY = event.clientY - rect.top;
		showRipple = true;

		await tick();
		setTimeout(() => {
			darkMode.update((prev) => {
				const newMode = !prev;
				localStorage.setItem('theme', newMode ? 'dark' : 'light');
				applyTheme(newMode);
				return newMode;
			});

			setTimeout(() => {
				showRipple = false;
				isAnimating = false;
			}, 600);
		}, 150);
	}

	function resetToSystemPreference() {
		userPrefersDark = false;
		localStorage.removeItem('theme');
		darkMode.set(systemPrefersDark);
		applyTheme(systemPrefersDark);
	}
</script>

<div class="theme-toggle-wrapper">
	<button
		on:click={toggleDarkMode}
		class="theme-toggle-button"
		aria-label={$darkMode ? 'Switch to light mode' : 'Switch to dark mode'}
		title={$darkMode ? 'Switch to light mode' : 'Switch to dark mode'}
	>
		<div class="toggle-icon-container">
			{#if $darkMode}
				<div in:scale={{ duration: 500, delay: 150, easing: elasticOut }}>
					<Sun class="toggle-icon sun-icon text-white" />
				</div>
			{:else}
				<div in:scale={{ duration: 500, delay: 150, easing: elasticOut }}>
					<Moon class="toggle-icon moon-icon" />
				</div>
			{/if}
		</div>

		{#if showRipple}
			<div
				class="ripple"
				style="left: {rippleX}px; top: {rippleY}px"
				in:scale={{ duration: 600, easing: cubicOut }}
			/>
		{/if}
	</button>

	{#if userPrefersDark}
		<button
			on:click={resetToSystemPreference}
			class="system-preference-button text-black dark:text-white"
			title="Use system preference"
			aria-label="Use system preference"
		>
			<div in:fade={{ duration: 200 }}>
				<Monitor class="system-icon" />
			</div>
		</button>
	{/if}
</div>

<style>
	.theme-toggle-wrapper {
		position: relative;
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
	}

	.theme-toggle-button {
		position: relative;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 42px;
		height: 42px;
		border-radius: 50%;
		background-color: var(--toggle-bg, transparent);
		border: 2px solid var(--toggle-border, rgba(0, 0, 0, 0.1));
		overflow: hidden;
		cursor: pointer;
		transition: all 0.3s ease;
		color: black;
	}

	:global(.dark) .theme-toggle-button {
		--toggle-border: rgba(255, 255, 255, 0.2);
		box-shadow: 0 0 10px rgba(255, 215, 0, 0.2);
	}

	.theme-toggle-button:hover {
		transform: scale(1.05);
		box-shadow: 0 0 15px var(--toggle-glow, rgba(0, 0, 0, 0.1));
	}

	:global(.dark) .theme-toggle-button:hover {
		--toggle-glow: rgba(255, 215, 0, 0.3);
	}

	.toggle-icon-container {
		position: relative;
		width: 24px;
		height: 24px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	/* 
	.toggle-icon {
		width: 24px;
		height: 24px;
	}

	.sun-icon {
		color: #fbbf24;
	}

	.moon-icon {
		color: #4b5563;
	}

	:global(.dark) .moon-icon {
		color: #e5e7eb;
	} */

	.ripple {
		position: absolute;
		border-radius: 50%;
		background: var(--ripple-color, rgba(251, 191, 36, 0.4));
		transform-origin: center;
		width: 120px;
		height: 120px;
		margin-left: -60px;
		margin-top: -60px;
		pointer-events: none;
	}

	:global(.dark) .ripple {
		--ripple-color: rgba(229, 231, 235, 0.3);
	}

	.system-preference-button {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 32px;
		height: 32px;
		border-radius: 50%;
		background-color: transparent;
		border: 1px solid var(--system-border, rgba(0, 0, 0, 0.1));
		cursor: pointer;
		transition: all 0.2s ease;
	}

	:global(.dark) .system-preference-button {
		--system-border: rgba(255, 255, 255, 0.2);
	}

	.system-preference-button:hover {
		transform: scale(1.05);
		background-color: var(--system-hover, rgba(0, 0, 0, 0.05));
	}

	:global(.dark) .system-preference-button:hover {
		--system-hover: rgba(255, 255, 255, 0.1);
	}
	/* 
	.system-icon {
		width: 16px;
		height: 16px;
		color: var(--system-color, #6b7280);
	}

	:global(.dark) .system-icon {
		--system-color: #9ca3af;
	} */

	@media (prefers-reduced-motion) {
		.theme-toggle-button:hover {
			transform: none;
		}

		.ripple {
			display: none;
		}
	}
</style>
