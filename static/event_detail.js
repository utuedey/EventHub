function getEventIdFromUrl() {
    const urlParams = document.location.href;
    const urlParts = urlParams.split('/');
    const eventId = urlParts[urlParts.length - 2];
    return eventId;
}

const eventId = getEventIdFromUrl();
if (eventId) {
    fetchEventDetails(eventId);
}

function fetchEventDetails(eventId) {
    fetch(`/core/api/events/${eventId}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            // Update event details with fetched data
            document.getElementById('event-image-img').src = data.image;
            document.getElementById('event-title').textContent = `${data.title}`;
            document.getElementById('event-description').textContent = `${data.description}`;
            document.getElementById('event-date').textContent = `Date: ${new Date(data.date_time).toLocaleDateString()}`;
            document.getElementById('event-location').textContent = `${data.location.address}, ${data.location.city}`;
            document.getElementById('event-price').textContent = `$${data.ticket_price}`;
        })
        .catch((error) => {
            // Handle errors here
            console.error('Fetch error:', error);
        });
}