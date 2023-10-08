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
    // const eventList = document.getElementById('event-list');
    const ticketList = document.getElementById('ticket-list');

    // Clear existing content
    ticketList.innerHTML = '';

    // Iterate through the events and create event cards
    events.forEach((event, index) => {
        // Render only the first four events
        if (index < 4) {
            const ticketCard = document.createElement('ul');
            ticketCard.innerHTML = `
            <li>
                <div class="row">
                    <div class="col-lg-3">
                        <div class="title">
                            <h4>${event.title}</h4>
                            <span>${event.ticket_available} Tickets Available</span>
                        </div>
                    </div>
                    <div class="col-lg-3">
                        <div class="time"><span><i class="fa fa-clock-o"></i>${formatDateTime(event.date_time)}</span></div>
                    </div>
                    <div class="col-lg-3">
                        <div class="place"><span><i class="fa fa-map-marker"></i>${event.location.address.slice(0, 30)}, <br>${event.location.city}</span></div>
                    </div>
                    <div class="col-lg-3">
                        <div class="main-dark-button">
                            <a href="{url 'ticket-detail' }">Purchase Tickets</a>
                        </div>
                    </div>
                </div>
            </li >`;

            // Append event card to the event list
            ticketList.appendChild(ticketCard);
        }
    });
}

// events.forEach((event, index) => {
//     // Render only the first four events
//     if (index < 4) {
//         const eventCard = document.createElement('div');
//         const anchor = document.createElement('a');
//         anchor.classList.add('event-card-link');
//         anchor.href = `/core/events/${event.id}`;

//         eventCard.classList.add('event-card');

//         // Set event card content
//         eventCard.innerHTML = `
//         <img src="${event.image}" alt="${event.title}">
//         <h3>${event.title}</h3>
//         <p>Date: ${new Date(event.date_time).toLocaleDateString()}</p>
//         <p>Location: Venue 1</p>
//         <p>Price: $${event.ticket_price}</p>
//         <a href="/core/events/${event.id}" class="cta-button">Learn More</a>
//     `;

//         anchor.appendChild(eventCard);
//         // Append event card to the event list
//         eventList.appendChild(anchor);
//     }
// });

// }

fetchData('/core/api/events/');



function formatDateTime(datetimeString) {
    const options = {
        weekday: 'short', // Short day of the week (e.g., "Fri")
        month: 'short',   // Short month name (e.g., "Sep")
        day: 'numeric',   // Day of the month (e.g., "24")
        hour: 'numeric',  // Hour (e.g., "6")
        minute: 'numeric', // Minute (e.g., "22")
        hour12: true      // Use 12-hour clock (e.g., "6PM")
    };

    const formattedDate = new Date(datetimeString).toLocaleDateString('en-US', options);

    return formattedDate;
}
