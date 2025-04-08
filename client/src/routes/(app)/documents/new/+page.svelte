<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import Alert from '$c/Alert.svelte';
	import Button from '$c/Button.svelte';
	import Progress from '$c/Progress.svelte';
	import { documents , upload, clearErrors } from '$s/documents';
	import { fade, fly, scale, slide } from 'svelte/transition';
	import { elasticOut, cubicOut } from 'svelte/easing';
	import { UploadCloud, FileText, CheckCircle2, XCircle } from 'lucide-svelte';

	let files: FileList;
	let loading = false;
	let uploadComplete = false;
	let isDragOver = false;

	async function handleSubmit() {
		loading = true;
		await upload(files[0]);

		if (!$documents.error) {
			uploadComplete = true;
			setTimeout(() => {
				goto('/documents');
				loading = false;
			}, 2000);
		} else {
			loading = false;
		}
	}

	function handleDragOver(e: DragEvent) {
		e.preventDefault();
		isDragOver = true;
	}

	function handleDragLeave() {
		isDragOver = false;
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		isDragOver = false;
		if (e.dataTransfer?.files) {
			files = e.dataTransfer.files;
		}
	}

	beforeNavigate(clearErrors);
</script>

<!-- 🌟 Animated Background with Gradient -->
<div 
	class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-50 via-blue-50 to-slate-200 
	dark:from-gray-900 dark:via-blue-900/20 dark:to-gray-800 transition-all duration-500 relative overflow-hidden"
>
	<!-- 🎨 Animated Background Elements -->
	{#each Array(3) as _, i}
		<div
			in:scale={{
				duration: 1000,
				delay: i * 200,
				easing: elasticOut,
				start: 0.5
			}}
			class="absolute rounded-full mix-blend-multiply dark:mix-blend-soft-light filter blur-xl opacity-30 dark:opacity-20 animate-float"
			style="
				width: {200 + i * 100}px;
				height: {200 + i * 100}px;
				background: {['#60A5FA', '#818CF8', '#A78BFA'][i]};
				animation-delay: {i * -2}s;
				top: {30 + i * 20}%;
				left: {20 + i * 25}%;
			"
		/>
	{/each}

	<!-- 📥 Upload Card -->
	<div
		in:scale={{
			duration: 800,
			delay: 200,
			easing: cubicOut,
			start: 0.8
		}}
		class="w-full max-w-xl mx-4 p-10 rounded-3xl bg-white dark:bg-gray-800 shadow-2xl
		transition-all duration-300
		{isDragOver ? 'ring-4 ring-blue-400 dark:ring-blue-500 scale-[1.02]' : ''}"
		on:dragover={handleDragOver}
		on:dragleave={handleDragLeave}
		on:drop={handleDrop}
	>
		<!-- 🎯 Enhanced Header with Animated Icon -->
		<div 
			in:fly={{ y: -30, duration: 700, delay: 400 }} 
			class="text-center space-y-4 mb-12"
		>
			<div class="relative w-16 h-16 mx-auto">
				<div class="absolute inset-0 animate-ping-slow rounded-full bg-blue-400/20 dark:bg-blue-500/20" />
				<UploadCloud 
					class="w-16 h-16 mx-auto text-blue-600 dark:text-blue-400 relative animate-float" 
				/>
			</div>
			<h1 
				class="text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r 
				from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400 tracking-tight"
			>
				Upload a Document
			</h1>
			<p class="text-gray-500 dark:text-gray-400 text-sm max-w-md mx-auto">
				Drag & drop your file here or click to browse. We support PDF and Word formats. ✨
			</p>
		</div>

		<!-- 📥 Enhanced Form -->
		<form
			on:submit|preventDefault={handleSubmit}
			class="space-y-6"
			in:fade={{ duration: 500, delay: 600 }}
		>
			<!-- Improved File Input -->
			<div 
				in:fly={{ y: 20, duration: 600, delay: 800 }}
				class="group"
			>
				<label
					for="file-input"
					class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2 flex justify-center items-center gap-2
					group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-300"
				>
					<FileText class="w-5 h-5" /> Choose your file
				</label>

				<input
					bind:files
					type="file"
					id="file-input"
					accept=".pdf,.doc,.docx"
					class="w-full text-center file:mx-auto text-sm text-gray-700 dark:text-gray-300
					border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-xl shadow-inner
					bg-gray-50 dark:bg-gray-700 p-4
					file:px-4 file:py-2 file:rounded-full file:border-0 file:font-semibold
					file:bg-blue-100 file:text-blue-700 hover:file:bg-blue-200
					dark:file:bg-blue-900 dark:file:text-blue-300 dark:hover:file:bg-blue-800
					focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500
					hover:border-blue-400 dark:hover:border-blue-500
					transition-all duration-300 cursor-pointer"
				/>
			</div>

			<!-- 🟩 Enhanced Progress -->
			{#if loading && !$documents.error}
				<div in:slide={{ duration: 300 }}>
					<Progress progress={$documents.uploadProgress}>
						<Alert type="success">
							<div class="flex items-center gap-2">
								<CheckCircle2 class="w-5 h-5 text-green-500 animate-pulse" />
								<span class="font-medium">Upload complete! Redirecting...</span>
							</div>
						</Alert>
					</Progress>
				</div>
			{/if}

			<!-- 🟥 Enhanced Error -->
			{#if $documents.error}
				<div in:scale={{ duration: 400, easing: elasticOut }}>
					<Alert type="error">
						<div class="flex items-center gap-2">
							<XCircle class="w-5 h-5 text-red-500 animate-bounce" />
							<span class="font-medium">Error: {$documents.error}</span>
						</div>
					</Alert>
				</div>
			{/if}

			<!-- 🚀 Enhanced Submit Button -->
			{#if !loading}
				<div in:fly={{ y: 10, duration: 500, delay: 1000 }}>
					<Button
						className="w-full py-4 px-6 bg-gradient-to-r from-blue-600 to-indigo-600 
						hover:from-blue-500 hover:to-indigo-500 text-white text-lg font-semibold rounded-xl 
						shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 
						hover:scale-105 focus:ring-4 ring-blue-400/30 outline-none"
					>
						<div class="flex items-center justify-center gap-2">
							<UploadCloud class="w-6 h-6" />
							<span>Upload Now</span>
						</div>
					</Button>
				</div>
			{/if}
		</form>
	</div>
</div>

<style>
	@keyframes float {
		0% { transform: translateY(0px); }
		50% { transform: translateY(-20px); }
		100% { transform: translateY(0px); }
	}

	@keyframes ping-slow {
		75%, 100% {
			transform: scale(2);
			opacity: 0;
		}
	}

	:global(.animate-float) {
		animation: float 6s ease-in-out infinite;
	}

	:global(.animate-ping-slow) {
		animation: ping-slow 2s cubic-bezier(0, 0, 0.2, 1) infinite;
	}
</style>