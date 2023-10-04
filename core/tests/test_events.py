import pytest
from django.urls import reverse
from core.models import Event, User, Category, Location, Tag
from core.views import EventListView

@pytest.fixture
def user_factory():
    def create_user(username, password):
        return User.objects.create_user(username=username, password=password)
    return create_user

@pytest.fixture
def category_factory():
    def create_category(name):
        return Category.objects.create(name=name)
    return create_category

@pytest.fixture
def location_factory():
    def create_location(name):
        return Location.objects.create(name=name)
    return create_location

@pytest.fixture
def tag_factory():
    def create_tag(name):
        return Tag.objects.create(name=name)
    return create_tag

@pytest.fixture
def event_factory(user_factory, category_factory, location_factory, tag_factory):
    def create_event(title, description, user, category, location, date_time, ticket_price, capacity, registration_deadline):
        return Event.objects.create(
            title=title,
            description=description,
            organizer=user,
            category=category,
            location=location,
            date_time=date_time,
            ticket_price=ticket_price,
            capacity=capacity,
            registration_deadline=registration_deadline,
        )
    return create_event

@pytest.mark.django_db
def test_event_list_view(client, user_factory, category_factory, location_factory, tag_factory, event_factory):
    # Create a user, category, location, and tags for the event
    user = user_factory("testuser", "password")
    category = category_factory("Test Category")
    location = location_factory("Test Location")
    tag1 = tag_factory("Tag 1")
    tag2 = tag_factory("Tag 2")

    # Create some sample events
    event_factory("Event 1", "Description 1", user, category, location, "2023-10-01 12:00:00", 10.0, 100, "2023-09-30 23:59:59").tags.set([tag1])
    event_factory("Event 2", "Description 2", user, category, location, "2023-10-02 12:00:00", 20.0, 200, "2023-10-01 23:59:59").tags.set([tag2])

    # Get the URL for the EventListView
    url = reverse('event-list')  # Replace 'event-list' with the actual URL name

    # Use the client to make a GET request to the view
    response = client.get(url)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the correct template is used
    assert 'event_list.html' in [template.name for template in response.templates]

    # Check that the 'events' context variable is present in the response
    assert 'events' in response.context

    # Check that the number of events in the context matches the number of created events
    assert len(response.context['events']) == 2

    # Check that the rendered HTML contains the titles of the created events
    content = response.content.decode('utf-8')
    assert 'Event 1' in content
    assert 'Event 2' in content