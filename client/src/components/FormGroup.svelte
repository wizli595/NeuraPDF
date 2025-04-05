<script lang="ts">
	export let label: string = '';
</script>

<div class="w-full">
	<div class="flex justify-between items-center mb-2">
		<label class="block text-sm font-semibold text-gray-700" for="">{label}</label>
	</div>
	<div class="relative">
		<slot />
	</div>
</div>
