<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import * as pdfjs from 'pdfjs-dist';
	pdfjs.GlobalWorkerOptions.workerSrc =
		'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

	export let url = '';

	let canvasContainer: HTMLDivElement;
	let pdfDoc: pdfjs.PDFDocumentProxy;
	let currentPage = 1;
	let totalPages = 0;
	let destroyed = false;

	async function renderCurrentPage() {
		if (!pdfDoc) return;
		const page = await pdfDoc.getPage(currentPage);
		const viewport = page.getViewport({ scale: 1.2 });

		// Clear previous
		canvasContainer.innerHTML = '';

		// Setup wrapper
		const wrapper = document.createElement('div');
		wrapper.classList.add('pdf-page-wrapper');

		const canvas = document.createElement('canvas');
		const ctx = canvas.getContext('2d');
		if (!ctx) return;

		canvas.width = viewport.width;
		canvas.height = viewport.height;
		canvas.className = 'pdf-canvas';

		wrapper.appendChild(canvas);
		canvasContainer.appendChild(wrapper);

		await page.render({ canvasContext: ctx, viewport }).promise;
	}

	function goToNextPage() {
		if (currentPage < totalPages) {
			currentPage++;
			renderCurrentPage();
		}
	}

	function goToPreviousPage() {
		if (currentPage > 1) {
			currentPage--;
			renderCurrentPage();
		}
	}

	onMount(async () => {
		pdfDoc = await pdfjs.getDocument(url).promise;
		totalPages = pdfDoc.numPages;
		if (!destroyed) {
			await renderCurrentPage();
		}
	});

	onDestroy(() => {
		destroyed = true;
	});
</script>

<!-- PDF Container -->
<div class="pdf-container">
	<!-- Navigation -->
	<div class="pdf-nav">
		<button on:click={goToPreviousPage} disabled={currentPage === 1}>← Previous</button>
		<span class="page-info">Page {currentPage} of {totalPages}</span>
		<button on:click={goToNextPage} disabled={currentPage === totalPages}>Next →</button>
	</div>

	<!-- Canvas -->
	<div bind:this={canvasContainer} class="pdf-wrapper" />
</div>

<style>
	.pdf-container {
		width: 100%;
		height: 100%;
		padding: 2rem;
		box-sizing: border-box;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
		gap: 2rem;
		scroll-behavior: smooth;
	}

	.pdf-wrapper {
		width: 100%;
		max-width: 100%;
		display: flex;
		justify-content: center;
		align-items: flex-start;
	}

	:global(.pdf-page-wrapper) {
		position: relative;
		background: white;
		border-radius: 1.5rem;
		overflow: hidden;
		box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
		transition: transform 0.2s ease;
	}

	:global(.pdf-canvas) {
		width: 100%;
		height: auto;
		display: block;
		background: white;
		border-radius: 1.5rem;
	}

	.pdf-nav {
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 1rem;
	flex-wrap: wrap;
	}

	.pdf-nav button {
		background-color: #3b82f6;
		color: white;
		padding: 0.3rem 0.7rem;
		font-size: 0.875rem;
		border: none;
		border-radius: 0.375rem;
		font-weight: 500;
		cursor: pointer;
		transition: background 0.2s ease;
	}

	.pdf-nav button:hover:enabled {
		background-color: #2563eb;
	}

	.pdf-nav button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.page-info {
		font-size: 0.875rem;
		color: #94a3b8;
		font-weight: 500;
	}

</style>
