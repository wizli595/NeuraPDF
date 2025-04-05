<script lang="ts">
	import classNames from 'classnames';
	export let disabled = false;
	export let className = '';
</script>

<button
	type="submit"
	class={classNames(
		'py-3 px-6 w-full rounded-xl border border-transparent font-semibold bg-gradient-to-r from-blue-500 to-indigo-500 text-white shadow-lg hover:from-blue-600 hover:to-indigo-600 active:scale-95 focus:outline-none focus:ring-4 focus:ring-blue-300 transition-all duration-300',
		className
	)}
	{disabled}><slot /></button
>
