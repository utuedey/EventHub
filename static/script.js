function fetchData(url) {
    return fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Add any required headers here, e.g., authentication tokens
        },
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            // Handle the data here
            populateEventCards(data);
        })
        .catch((error) => {
            // Handle errors here
            console.error('Fetch error:', error);
        });
}

function populateEventCards(events) {
    const eventList = document.getElementById('event-list');

    // Clear existing content
    eventList.innerHTML = '';

    // Iterate through the events and create event cards
    events.forEach((event, index) => {
        // Render only the first four events
        if (index < 4) {
            const eventCard = document.createElement('div');
            const anchor = document.createElement('a');
            anchor.classList.add('event-card-link');
            anchor.href = `/core/events/${event.id}`;

            eventCard.classList.add('event-card');

            // Set event card content
            eventCard.innerHTML = `
            <img src="${event.image}" alt="${event.title}">
            <h3>${event.title}</h3>
            <p>Date: ${new Date(event.date_time).toLocaleDateString()}</p>
            <p>Location: Venue 1</p>
            <p>Price: $${event.ticket_price}</p>
            <a href="/core/events/${event.id}" class="cta-button">Learn More</a>
        `;

            anchor.appendChild(eventCard);
            // Append event card to the event list
            eventList.appendChild(anchor);
        }
    });

}

fetchData('/core/api/events/');

