<script lang="ts">
	import classNames from 'classnames';
	export let type: string = 'text';
	export let value = '';
	export let className = '';

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<input
	use:typeAction
	bind:value
	class={classNames(
		'py-3 px-4 w-full border-none rounded-xl text-sm shadow-md bg-white/20 backdrop-blur-md text-gray-800 placeholder-gray-400 focus:ring-4 focus:ring-blue-400 focus:outline-none transition-all',
		className
	)}
	placeholder="Enter your {type}"
	required
/>
