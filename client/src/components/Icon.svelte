<script lang="ts">
	import c from 'classnames';

	export let name = '';
	export let outlined = false;
	export let size = '16px';
	export let klass = '';
	export let classN: string = '';

	const klasses = c(
		{
			'material-icons-outlined': outlined,
			'material-icons': !outlined
		},
		klass,
		classN
	);
</script>

<span on:click on:keydown class={klasses} style:font-size={size}>{name}</span>
