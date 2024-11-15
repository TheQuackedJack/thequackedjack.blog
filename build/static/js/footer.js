document.addEventListener("DOMContentLoaded", function() {
	const currentYear = new Date().getFullYear();
	let yearString = currentYear === 2024 ? "2024" : `2024-${currentYear}`;
	document.getElementById("footer-copyright").textContent = `© ${yearString} TheQuackedJack. No rights reserved 🦆`;
});