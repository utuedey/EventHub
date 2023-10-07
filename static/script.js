// function fetchData(url) {
//   return fetch(url, {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json',
//       // Add any required headers here, e.g., authentication tokens
//     },
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then((data) => {
//       // Handle the data here
//       console.log(data);
//     })
//     .catch((error) => {
//       // Handle errors here
//       console.error('Fetch error:', error);
//     });
// }

// // Example usage:
// // Replace 'your-api-endpoint' with the actual API endpoint
// // fetchData('/your-api-endpoint');

// function postData(url, data) {
//   return fetch(url, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       // Add any required headers here, e.g., authentication tokens
//     },
//     body: JSON.stringify(data),
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then((responseData) => {
//       // Handle the response data here
//       console.log(responseData);
//     })
//     .catch((error) => {
//       // Handle errors here
//       console.error('Fetch error:', error);
//     });
// }

// // Example usage:
// // Replace 'your-api-endpoint' with the actual API endpoint
// const postDataObject = {
//   // Replace with your POST data
//   key1: 'value1',
//   key2: 'value2',
// };
// console.log('============= HOME PAGE =============')

// // Define the API endpoint for events
// const eventApiEndpoint = '/core/api/events/';

// // Function to fetch events and populate the HTML
// function fetchAndPopulateEvents() {
//   // Use the fetchData function to make the GET request
//   fetchData(eventApiEndpoint)
//     .then((data) => {
//       // Handle the data (list of events) here
//       const carouselContainer = document.getElementById("dynamic-carousel");

//       // Loop through the event data and create dynamic items
//       data.forEach((event) => {
//         const item = document.createElement("div");
//         item.classList.add("item");

//         const link = document.createElement("a");
//         link.href = event.url; // Replace with the actual event detail URL

//         const img = document.createElement("img");
//         img.src = event.image; // Replace with the actual image URL
//         img.alt = event.title;

//         link.appendChild(img);
//         item.appendChild(link);

//         carouselContainer.appendChild(item);
//       });
//     })
//     .catch((error) => {
//       // Handle errors here
//       console.error('Error fetching events:', error);
//     });
// }

// // Example usage
// fetchAndPopulateEvents();

// postData('/your-api-endpoint', postDataObject);

// urls = ['^locations/$' [name='location-list'], 
//   '^locations\.(?P<format>[a-z0-9]+)/?$' [name='location-list'], '^locations/(?P<pk>[^/.]+)/$' [name='location-detail'],
//   '^locations/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='location-detail'],
//   '^categories/$' [name='category-list'],
//   '^categories\.(?P<format>[a-z0-9]+)/?$' [name='category-list'],
//   '^categories/(?P<pk>[^/.]+)/$' [name='category-detail'],
//   '^categories/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='category-detail'],
//   '^tags/$' [name='tag-list'],
//   '^tags\.(?P<format>[a-z0-9]+)/?$' [name='tag-list'],
//   '^tags/(?P<pk>[^/.]+)/$' [name='tag-detail'],
//   '^tags/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='tag-detail'],
//   '^events/$' [name='event-list'],
//   '^events\.(?P<format>[a-z0-9]+)/?$' [name='event-list'],
//   '^events/(?P<pk>[^/.]+)/$' [name='event-detail'],
//   '^events/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='event-detail'],
//   '^profiles/$' [name='userprofile-list'],
//   '^profiles\.(?P<format>[a-z0-9]+)/?$' [name='userprofile-list'], 
//   '^profiles/(?P<pk>[^/.]+)/$' [name='userprofile-detail'], 
//   '^profiles/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='userprofile-detail'],
//   '^payments/$' [name='payment-list'],
//   '^payments\.(?P<format>[a-z0-9]+)/?$' [name='payment-list'],
//   '^payments/(?P<pk>[^/.]+)/$' [name='payment-detail'],
//   '^payments/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='payment-detail'],
//   '^$' [name='api-root'],
//   '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']
// ]

// urls_2 = [
//   '^events/(?P<event_pk>[^/.]+)/tickets/$' [name='event-tickets-list'],
//   '^events/(?P<event_pk>[^/.]+)/tickets\.(?P<format>[a-z0-9]+)/?$' [name='event-tickets-list'], 
//   '^events/(?P<event_pk>[^/.]+)/tickets/(?P<pk>[^/.]+)/$' [name='event-tickets-detail'],
//   '^events/(?P<event_pk>[^/.]+)/tickets/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='event-tickets-detail'],
//   '^$' [name='api-root'],
//   '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']
// ]

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
            anchor.href = `/core/api/events/${event.id}`;

            eventCard.classList.add('event-card');

            // Set event card content
            eventCard.innerHTML = `
            <img src="${event.image}" alt="${event.title}">
            <h3>${event.title}</h3>
            <p>Date: ${new Date(event.date_time).toLocaleDateString()}</p>
            <p>Location: Venue 1</p>
            <p>Price: $${event.ticket_price}</p>
            <a href="/core/api/events/${event.id}" class="cta-button">Learn More</a>
        `;

            anchor.appendChild(eventCard);
            // Append event card to the event list
            eventList.appendChild(anchor);
        }
    });

}

fetchData('/core/api/events/');
