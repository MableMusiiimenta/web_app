document.addEventListener('DOMContentLoaded', function () {
    // Add click event listeners to sidebar links
    document.getElementById('dashboard-link').addEventListener('click', loadDashboardContent);
    document.getElementById('sitters-link').addEventListener('click', loadSittersContent);
    // Add click event listeners for other sidebar links as needed
});

function loadDashboardContent(event) {
    event.preventDefault(); // Prevent default link behavior

    // Show dashboard content and hide other content
    document.getElementById('dashboard-content').style.display = 'block';
    document.getElementById('sitters-content').style.display = 'none';
    // Hide other content areas as needed

    // Use AJAX to load dashboard content
    // Example: Make an AJAX request to a Django view that returns dashboard data
}

function loadSittersContent(event) {
    event.preventDefault(); // Prevent default link behavior

    // Show sitters content and hide other content
    document.getElementById('dashboard-content').style.display = 'none';
    document.getElementById('sitters-content').style.display = 'block';
    // Hide other content areas as needed

    // Use AJAX to load sitters content
    // Example: Make an AJAX request to a Django view that returns sitters data
}
// Define similar functions for other sidebar items
