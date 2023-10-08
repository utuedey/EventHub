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


// Function to make the API call for event registration
function registerForEvent(eventId) {
    fetch(`/events/${eventId}/registration/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            // Handle successful registration here (e.g., show a success message)
            alert('Registration successful!');
            console.log('Registration data:', data);
        })
        .catch((error) => {
            // Handle errors here (e.g., show an error message)
            alert('Registration error. Please try again later.');
            console.error('Registration error:', error);
        });
}

// Event registration button click handler
document.addEventListener('DOMContentLoaded', function () {
    const registerButton = document.querySelector('.register-button');
    registerButton.addEventListener('click', function () {
        // Get the event ID from the URL
        const eventUrl = document.location.href;
        const eventId = eventUrl.split('/').slice(-2, -1)[0];

        // Call the registration function with the event ID
        registerForEvent(eventId);
    });
});


function getCookie(name) {
    // Function to get a cookie by name
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
