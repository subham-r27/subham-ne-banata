document.addEventListener('DOMContentLoaded', () => {
    const distanceInput = document.getElementById('distance-input');
    const emissionsOutput = document.getElementById('emissions-output');
    const rewardOutput = document.getElementById('reward-output');
    const adjustedRewardOutput = document.getElementById('adjusted-reward-output');

    distanceInput.addEventListener('input', () => {
        const distance = parseFloat(distanceInput.value) || 0;
        
        const emissionsAvoided = calculateEmissionsAvoided(distance);
        const rewardPoints = calculateRewardPoints(emissionsAvoided);
        const adjustedRewardPoints = adjustRewardPoints(rewardPoints);

        emissionsOutput.value = emissionsAvoided.toFixed(2);
        rewardOutput.value = rewardPoints.toFixed(2);
        adjustedRewardOutput.value = adjustedRewardPoints.toFixed(2);
    });

    // Navbar navigation
    const navbarLinks = document.querySelectorAll('.nav-link');
    navbarLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default anchor behavior
            const page = event.target.textContent.trim().toLowerCase().replace(' ', '-');
            navigateToPage(page);
        });
    });
});

function calculateEmissionsAvoided(distance) {
    const emissionFactor = 0.21; // Example emission factor in kg CO2 per km
    return distance * emissionFactor;
}

function calculateRewardPoints(emissionsAvoided) {
    const rewardFactor = 10; // Example reward factor
    return emissionsAvoided * rewardFactor;
}

function adjustRewardPoints(rewardPoints) {
    const adjustmentFactor = 1.1; // Example adjustment factor
    return rewardPoints * adjustmentFactor;
}

function navigateToPage(page) {
    // You can implement logic here to navigate to different pages based on 'page' parameter
    console.log(`Navigating to ${page}`);
    // Example: window.location.href = `/${page}.html`;
}
