// Get elements
const searchBox = document.getElementById('searchBox');
const brandFilter = document.getElementById('brandFilter');
const sortFilter = document.getElementById('sortFilter');
const vehicleList = document.getElementById('vehicleList');
const cards = Array.from(vehicleList.getElementsByClassName('card'));

// Filter and display vehicles
function filterVehicles() {
    const searchText = searchBox.value.toLowerCase();
    const selectedBrand = brandFilter.value;

    // Filter cards by search text and brand
    cards.forEach(card => {
        const name = card.querySelector('h2').textContent.toLowerCase();
        const brand = card.dataset.brand;

        const matchesSearch = name.includes(searchText);
        const matchesBrand = selectedBrand === 'all' || selectedBrand === brand;

        card.style.display = (matchesSearch && matchesBrand) ? 'block' : 'none';
    });

    sortVehicles(); // apply sorting after filtering
}

// Sort vehicles
function sortVehicles() {
    const sortValue = sortFilter.value;
    const visibleCards = cards.filter(card => card.style.display !== 'none');

    visibleCards.sort((a, b) => {
        const aDetails = a.querySelector('.details').textContent;
        const bDetails = b.querySelector('.details').textContent;

        const aPrice = parseInt(aDetails.match(/💲\s?([\d,]+)/)[1].replace(/,/g, ''));
        const bPrice = parseInt(bDetails.match(/💲\s?([\d,]+)/)[1].replace(/,/g, ''));

        const aSpeed = parseInt(aDetails.match(/⚡\s?([\d]+)/)[1]);
        const bSpeed = parseInt(bDetails.match(/⚡\s?([\d]+)/)[1]);

        if(sortValue === 'price-low') return aPrice - bPrice;
        if(sortValue === 'price-high') return bPrice - aPrice;
        if(sortValue === 'speed-low') return aSpeed - bSpeed;
        if(sortValue === 'speed-high') return bSpeed - aSpeed;
        return 0;
    });

    // Re-append sorted cards to the container
    visibleCards.forEach(card => vehicleList.appendChild(card));
}

// Event listeners
searchBox.addEventListener('input', filterVehicles);
brandFilter.addEventListener('change', filterVehicles);
sortFilter.addEventListener('change', filterVehicles);
