<script lang="ts">
	import { onMount, tick } from 'svelte';
	import { goto } from '$app/navigation';
	import { fly, fade, scale } from 'svelte/transition';
	import { spring } from 'svelte/motion';
	import { cubicOut, cubicInOut } from 'svelte/easing';

	// Animation controls
	let showHero = false;
	let showIcons = false;
	let showFeatures = false;
	let typingText = '';
	const fullText = 'Talk to your PDFs like never before.';
	let currentSection = 'hero';

	// Interactive demo controls
	let demoStep = 0;
	let demoMessages: { text: string; type: 'user' | 'assistant' }[] = [
		{ text: 'Summarize the key findings in this research paper.', type: 'user' },
		{
			text: 'The paper identifies three main findings: 1) AI-assisted document analysis improves comprehension by 47%, 2) Interactive querying reduces research time by 68%, and 3) Contextual understanding increases accuracy by 34% compared to traditional search methods.',
			type: 'assistant'
		},
		{ text: 'What methodology did they use?', type: 'user' },
		{
			text: 'The research employed a mixed-methods approach with a quantitative analysis of 2,450 user interactions and qualitative feedback from 215 participants across various professional backgrounds including academia, legal, and healthcare sectors.',
			type: 'assistant'
		}
	];
	let visibleMessages: { text: string; type: 'user' | 'assistant' }[] = [];

	// Intersection Observer for scroll animations
	let featuresSection: HTMLElement;
	let contactSection: HTMLElement;

	// Smooth scrolling coordinates
	const coords = spring(
		{ y: 0 },
		{
			stiffness: 0.1,
			damping: 0.7
		}
	);

	onMount(async () => {
		// Initial animations sequence
		setTimeout(() => (showHero = true), 300);
		await tick();
		setTimeout(() => typeIt(), 800);
		setTimeout(() => (showIcons = true), 1500);
		setTimeout(() => startDemoAnimation(), 2000);

		// Setup intersection observers
		setupScrollObservers();

		// Listen for scroll events
		window.addEventListener('scroll', handleScroll);

		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});

	function setupScrollObservers() {
		const featureOptions = {
			root: null,
			rootMargin: '0px',
			threshold: 0.2
		};

		const featureObserver = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					showFeatures = true;
					currentSection = 'features';
				}
			});
		}, featureOptions);

		const contactObserver = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					currentSection = 'contact';
				}
			});
		}, featureOptions);

		if (featuresSection) featureObserver.observe(featuresSection);
		if (contactSection) contactObserver.observe(contactSection);
	}

	function handleScroll() {
		// Update for parallax effects if needed
		const scrollY = window.scrollY;
		coords.update(($coords) => ({ y: scrollY * 0.2 }));
	}

	function typeIt(index = 0) {
		if (index < fullText.length) {
			typingText += fullText[index];
			const delay = fullText[index] === '.' ? 200 : 35;
			setTimeout(() => typeIt(index + 1), delay);
		}
	}

	async function startDemoAnimation() {
		// Show demo messages one by one
		for (let i = 0; i < demoMessages.length; i++) {
			await new Promise((resolve) => setTimeout(resolve, 1500));
			visibleMessages = [...visibleMessages, demoMessages[i]];
		}
	}

	function handleGetStarted() {
		goto('/documents');
	}

	function smoothScrollTo(id: string) {
		const element = document.getElementById(id);
		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

<div class="page-wrapper">
	<!-- Enhanced Navbar -->
	<nav
		class="fixed top-0 w-full z-50 bg-transparent backdrop-blur-sm transition-all duration-300 px-6 py-4 flex items-center justify-between text-white"
		class:bg-opacity-90={currentSection !== 'hero'}
		class:bg-gray-900={currentSection !== 'hero'}
	>
		<div class="text-2xl font-bold tracking-tight flex items-center gap-2">
			<span class="material-icons text-yellow-300">auto_awesome</span>
			Neura<span class="text-yellow-300">PDF</span>
		</div>
		<div class="hidden sm:flex gap-8 text-lg font-medium">
			<a
				on:click|preventDefault={() => smoothScrollTo('hero')}
				href="#hero"
				class="hover:text-yellow-300 transition-colors">Home</a
			>
			<a
				on:click|preventDefault={() => smoothScrollTo('features')}
				href="#features"
				class="hover:text-yellow-300 transition-colors">Features</a
			>
			<a
				on:click|preventDefault={() => smoothScrollTo('contact')}
				href="#contact"
				class="hover:text-yellow-300 transition-colors">Contact</a
			>
		</div>
		<div class="block sm:hidden">
			<span class="material-icons text-2xl">menu</span>
		</div>
	</nav>

	<!-- Improved Hero Section with Interactive Demo -->
	<div
		id="hero"
		class="min-h-screen bg-landing text-white flex flex-col items-center justify-center p-6 pt-28 relative overflow-hidden"
	>
		<!-- Background Gradients -->
		<div class="absolute inset-0 -z-10">
			<div
				class="absolute top-0 right-0 w-1/2 h-1/2 bg-purple-600 rounded-full opacity-20 blur-3xl transform translate-x-1/4 -translate-y-1/4"
			/>
			<div
				class="absolute bottom-0 left-0 w-3/4 h-1/2 bg-blue-600 rounded-full opacity-20 blur-3xl transform -translate-x-1/4 translate-y-1/4"
			/>
		</div>

		{#if showHero}
			<div in:fly={{ y: -40, duration: 800, easing: cubicOut }} class="text-center max-w-4xl px-4">
				<div class="flex justify-center items-center mb-2">
					<span class="material-icons text-yellow-300 text-4xl animate-pulse">auto_awesome</span>
				</div>
				<h1 class="text-5xl sm:text-7xl font-extrabold tracking-tight mb-4">
					Neura<span class="text-yellow-300">PDF</span>
				</h1>
				<p
					class="text-xl sm:text-2xl text-white/90 mb-8 min-h-[3rem]"
					in:fade={{ duration: 800, delay: 400 }}
				>
					{typingText}
				</p>

				<!-- Interactive PDF Chat Demo -->
				<div
					class="max-w-lg mx-auto my-8 border border-white/20 bg-gray-900/70 backdrop-blur-sm rounded-xl shadow-2xl overflow-hidden"
				>
					<div class="border-b border-white/20 px-4 py-3 flex items-center">
						<div class="flex space-x-2">
							<div class="w-3 h-3 rounded-full bg-red-500" />
							<div class="w-3 h-3 rounded-full bg-yellow-500" />
							<div class="w-3 h-3 rounded-full bg-green-500" />
						</div>
						<span class="ml-4 text-white/70 text-sm">PDF Chat Assistant</span>
					</div>

					<div class="p-4 h-80 overflow-y-auto" style="scrollbar-width: none;">
						<div class="flex items-center mb-4">
							<span class="material-icons text-sm text-yellow-300 mr-2">insert_drive_file</span>
							<span class="text-white/70 text-sm">research-findings-2025.pdf • 18 pages</span>
						</div>

						<!-- Demo Chat Messages -->
						{#each visibleMessages as message, i}
							<div
								class="mb-4 {message.type === 'user' ? 'flex justify-end' : 'flex'}"
								in:fly={{ y: 20, duration: 400, delay: 100 }}
							>
								<div
									class="max-w-[80%] {message.type === 'user'
										? 'bg-blue-600'
										: 'bg-gray-700'} rounded-lg px-4 py-2 text-left"
								>
									<p class="text-sm">{message.text}</p>
								</div>
							</div>
						{/each}

						<!-- Typing indicator -->
						{#if visibleMessages.length < demoMessages.length}
							<div class="flex items-center mb-4">
								<div class="bg-gray-700 rounded-lg px-4 py-2">
									<div class="flex space-x-1">
										<div
											class="w-2 h-2 rounded-full bg-gray-400 animate-bounce"
											style="animation-delay: 0ms;"
										/>
										<div
											class="w-2 h-2 rounded-full bg-gray-400 animate-bounce"
											style="animation-delay: 150ms;"
										/>
										<div
											class="w-2 h-2 rounded-full bg-gray-400 animate-bounce"
											style="animation-delay: 300ms;"
										/>
									</div>
								</div>
							</div>
						{/if}
					</div>
				</div>

				<div class="flex flex-col sm:flex-row justify-center items-center gap-4 mt-6">
					<button
						on:click={handleGetStarted}
						in:scale={{ duration: 400, delay: 800 }}
						class="bg-yellow-300 text-black hover:bg-white hover:text-purple-700 font-semibold px-6 py-3 rounded-full shadow-lg transition-all duration-300 flex items-center gap-2 text-lg"
					>
						<span class="material-icons">chat</span>
						Start Chatting
					</button>

					<button
						on:click={() => smoothScrollTo('features')}
						in:scale={{ duration: 400, delay: 1000 }}
						class="bg-transparent border border-white/40 hover:border-yellow-300 hover:text-yellow-300 font-semibold px-6 py-3 rounded-full shadow-lg transition-all duration-300 flex items-center gap-2 text-lg"
					>
						<span class="material-icons">arrow_downward</span>
						Learn More
					</button>
				</div>
			</div>
		{/if}

		{#if showIcons}
			<div
				class="mt-20 grid grid-cols-3 sm:grid-cols-5 gap-8 text-5xl text-yellow-300/80"
				in:fade={{ duration: 800, delay: 1200 }}
			>
				<span class="material-icons transform hover:scale-110 transition-transform duration-300"
					>description</span
				>
				<span class="material-icons transform hover:scale-110 transition-transform duration-300"
					>smart_toy</span
				>
				<span class="material-icons transform hover:scale-110 transition-transform duration-300"
					>auto_awesome</span
				>
				<span class="material-icons transform hover:scale-110 transition-transform duration-300"
					>question_answer</span
				>
				<span class="material-icons transform hover:scale-110 transition-transform duration-300"
					>upload_file</span
				>
			</div>
		{/if}
	</div>

	<!-- Enhanced Features Section -->
	<section
		id="features"
		class="py-24 bg-gradient-to-b from-gray-900 to-gray-800 relative overflow-hidden"
		bind:this={featuresSection}
	>
		<div class="absolute inset-0 -z-10">
			<div
				class="absolute top-1/2 left-1/2 w-full h-full bg-purple-600 rounded-full opacity-10 blur-3xl transform -translate-x-1/2 -translate-y-1/2"
			/>
		</div>

		<div class="container mx-auto px-6">
			<h2 class="text-4xl font-bold text-center text-white mb-2">Features</h2>
			<p class="text-center text-gray-300 max-w-xl mx-auto mb-16">
				Experience the future of document interaction with our powerful AI-driven tools.
			</p>

			<div class="flex flex-wrap -mx-4">
				{#if showFeatures}
					<!-- Feature 1 -->
					<div class="w-full md:w-1/3 px-4 mb-8" in:fly={{ y: 40, duration: 600, delay: 0 }}>
						<div
							class="bg-gray-800/50 backdrop-blur-sm border border-purple-500/20 p-6 rounded-xl shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1 transition-all duration-300 h-full"
						>
							<span class="material-icons text-5xl text-yellow-300 mb-4">chat</span>
							<h3 class="text-2xl font-semibold text-white mb-3">Intelligent Conversations</h3>
							<p class="text-gray-300">
								Engage in natural, context-aware discussions with your PDFs. Ask questions, request
								summaries, and extract insights with remarkable accuracy.
							</p>
						</div>
					</div>

					<!-- Feature 2 -->
					<div class="w-full md:w-1/3 px-4 mb-8" in:fly={{ y: 40, duration: 600, delay: 200 }}>
						<div
							class="bg-gray-800/50 backdrop-blur-sm border border-purple-500/20 p-6 rounded-xl shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1 transition-all duration-300 h-full"
						>
							<span class="material-icons text-5xl text-yellow-300 mb-4">search</span>
							<h3 class="text-2xl font-semibold text-white mb-3">Semantic Search</h3>
							<p class="text-gray-300">
								Move beyond keyword matching. Our AI understands the meaning behind your queries,
								finding relevant information even when exact terms aren't present.
							</p>
						</div>
					</div>

					<!-- Feature 3 -->
					<div class="w-full md:w-1/3 px-4 mb-8" in:fly={{ y: 40, duration: 600, delay: 400 }}>
						<div
							class="bg-gray-800/50 backdrop-blur-sm border border-purple-500/20 p-6 rounded-xl shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1 transition-all duration-300 h-full"
						>
							<span class="material-icons text-5xl text-yellow-300 mb-4">lock</span>
							<h3 class="text-2xl font-semibold text-white mb-3">Zero-Knowledge Security</h3>
							<p class="text-gray-300">
								Your documents remain yours alone. Our end-to-end encryption and secure processing
								ensure complete privacy and confidentiality.
							</p>
						</div>
					</div>

					<!-- Feature 4 -->
					<div class="w-full md:w-1/2 px-4 mb-8" in:fly={{ y: 40, duration: 600, delay: 600 }}>
						<div
							class="bg-gray-800/50 backdrop-blur-sm border border-purple-500/20 p-6 rounded-xl shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1 transition-all duration-300 h-full"
						>
							<span class="material-icons text-5xl text-yellow-300 mb-4">bolt</span>
							<h3 class="text-2xl font-semibold text-white mb-3">Lightning Fast Processing</h3>
							<p class="text-gray-300">
								Upload PDFs of any size and receive instant insights. Our optimized processing
								engine handles even the most complex documents with ease.
							</p>
						</div>
					</div>

					<!-- Feature 5 -->
					<div class="w-full md:w-1/2 px-4 mb-8" in:fly={{ y: 40, duration: 600, delay: 800 }}>
						<div
							class="bg-gray-800/50 backdrop-blur-sm border border-purple-500/20 p-6 rounded-xl shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1 transition-all duration-300 h-full"
						>
							<span class="material-icons text-5xl text-yellow-300 mb-4">analytics</span>
							<h3 class="text-2xl font-semibold text-white mb-3">Advanced Analytics</h3>
							<p class="text-gray-300">
								Extract trends, patterns, and key metrics from your documents. Transform dense text
								into actionable insights and visualized data.
							</p>
						</div>
					</div>
				{/if}
			</div>
		</div>
	</section>

	<!-- Modern Contact Section -->
	<section id="contact" class="bg-gray-800 py-24 px-6 relative" bind:this={contactSection}>
		<div class="max-w-4xl mx-auto">
			<div class="text-center mb-12">
				<h2 class="text-4xl font-bold text-white mb-4">Contact Us</h2>
				<p class="text-gray-300 max-w-xl mx-auto">
					Have questions about how NeuraPDF can transform your document workflow? We'd love to hear
					from you.
				</p>
			</div>

			<div
				class="bg-gray-900/80 backdrop-blur-sm border border-purple-500/20 rounded-xl p-8 shadow-xl"
			>
				<form class="space-y-6">
					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div>
							<label for="name" class="block text-sm font-medium text-gray-300 mb-1">Name</label>
							<input
								id="name"
								type="text"
								class="w-full p-3 rounded-lg border border-gray-700 bg-gray-800/50 text-white focus:ring-2 focus:ring-yellow-300 focus:border-transparent transition-all"
								placeholder="Your name"
							/>
						</div>
						<div>
							<label for="email" class="block text-sm font-medium text-gray-300 mb-1">Email</label>
							<input
								id="email"
								type="email"
								class="w-full p-3 rounded-lg border border-gray-700 bg-gray-800/50 text-white focus:ring-2 focus:ring-yellow-300 focus:border-transparent transition-all"
								placeholder="your@email.com"
							/>
						</div>
					</div>

					<div>
						<label for="subject" class="block text-sm font-medium text-gray-300 mb-1">Subject</label
						>
						<input
							id="subject"
							type="text"
							class="w-full p-3 rounded-lg border border-gray-700 bg-gray-800/50 text-white focus:ring-2 focus:ring-yellow-300 focus:border-transparent transition-all"
							placeholder="How can we help?"
						/>
					</div>

					<div>
						<label for="message" class="block text-sm font-medium text-gray-300 mb-1">Message</label
						>
						<textarea
							id="message"
							rows="5"
							class="w-full p-3 rounded-lg border border-gray-700 bg-gray-800/50 text-white focus:ring-2 focus:ring-yellow-300 focus:border-transparent transition-all"
							placeholder="Your message here..."
						/>
					</div>

					<div class="flex justify-end">
						<button
							type="submit"
							class="bg-yellow-300 hover:bg-white text-gray-900 px-8 py-3 rounded-lg font-semibold shadow-lg transition-all duration-300 flex items-center gap-2"
						>
							<span class="material-icons text-sm">send</span>
							Send Message
						</button>
					</div>
				</form>
			</div>
		</div>
	</section>

	<!-- Modern Footer -->
	<footer id="footer" class="bg-gray-900 text-white py-12 border-t border-white/10">
		<div class="container mx-auto px-6">
			<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
				<div>
					<div class="text-2xl font-bold mb-4 flex items-center gap-2">
						<span class="material-icons text-yellow-300">auto_awesome</span>
						Neura<span class="text-yellow-300">PDF</span>
					</div>
					<p class="text-gray-400 mb-4">Revolutionizing how you interact with your documents.</p>
					<div class="flex space-x-4">
						<a href="#" class="text-gray-400 hover:text-yellow-300 transition-colors">
							<span class="material-icons">facebook</span>
						</a>
						<a href="#" class="text-gray-400 hover:text-yellow-300 transition-colors">
							<span class="material-icons">twitter</span>
						</a>
						<a href="#" class="text-gray-400 hover:text-yellow-300 transition-colors">
							<span class="material-icons">linkedin</span>
						</a>
					</div>
				</div>

				<div>
					<h3 class="text-lg font-semibold mb-4">Quick Links</h3>
					<ul class="space-y-2">
						<li>
							<a href="#hero" class="text-gray-400 hover:text-yellow-300 transition-colors">Home</a>
						</li>
						<li>
							<a href="#features" class="text-gray-400 hover:text-yellow-300 transition-colors"
								>Features</a
							>
						</li>
						<li>
							<a href="#contact" class="text-gray-400 hover:text-yellow-300 transition-colors"
								>Contact</a
							>
						</li>
						<li>
							<a href="#p" class="text-gray-400 hover:text-yellow-300 transition-colors"
								>Privacy Policy</a
							>
						</li>
					</ul>
				</div>

				<div>
					<h3 class="text-lg font-semibold mb-4">Newsletter</h3>
					<p class="text-gray-400 mb-4">Stay updated with our latest features and news.</p>
					<div class="flex">
						<input
							type="email"
							placeholder="Your email"
							class="flex-1 p-2 rounded-l-lg border border-gray-700 bg-gray-800 text-white focus:ring-2 focus:ring-yellow-300 focus:border-transparent"
						/>
						<button
							class="bg-yellow-300 hover:bg-white text-gray-900 px-4 py-2 rounded-r-lg font-medium transition-colors"
						>
							<span class="material-icons text-sm">send</span>
						</button>
					</div>
				</div>
			</div>

			<div class="border-t border-white/10 mt-8 pt-8 text-center text-gray-400 text-sm">
				© {new Date().getFullYear()} NeuraPDF — Built for intelligent document conversations.
			</div>
		</div>
	</footer>
</div>

<style>
	.page-wrapper {
		scroll-behavior: smooth;
	}
	.bg-landing {
		background: linear-gradient(135deg, #1a1c42 0%, #2c1b5b 50%, #3b185f 100%);
	}

	:global(html) {
		scroll-behavior: smooth;
	}

	/* Custom scrollbar styles */
	::-webkit-scrollbar {
		width: 8px;
	}

	::-webkit-scrollbar-track {
		background: rgba(0, 0, 0, 0.1);
	}

	::-webkit-scrollbar-thumb {
		background: rgba(147, 51, 234, 0.5);
		border-radius: 4px;
	}

	::-webkit-scrollbar-thumb:hover {
		background: rgba(147, 51, 234, 0.7);
	}
</style>
