function toggleTheme() {
	document.body.classList.toggle('dark-theme');
	const themeIcon = document.getElementById("theme-icon");

	// Toggle icon between moon and sun
	if (document.body.classList.contains('dark-theme')) {
		themeIcon.classList.remove('fa-moon');
		themeIcon.classList.add('fa-sun');
	} else {
		themeIcon.classList.remove('fa-sun');
		themeIcon.classList.add('fa-moon');
	}
}