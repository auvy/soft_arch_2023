import pytest

from bus import EventBus

EVENT_USER_CREATED = "user_created"
EVENT_USER_UPDATED = "user_updated"


def handle_user_created(data):
    print("User created:", data)


def handle_user_updated(data):
    print("User updated:", data)


def test_event_bus_subscribe():
    event_bus = EventBus()
    event_bus.subscribe(EVENT_USER_CREATED, handle_user_created)
    event_bus.subscribe(EVENT_USER_UPDATED, handle_user_updated)

    assert len(event_bus.listeners) == 2
    assert len(event_bus.listeners[EVENT_USER_CREATED]) == 1
    assert len(event_bus.listeners[EVENT_USER_UPDATED]) == 1


def test_event_bus_unsubscribe():
    event_bus = EventBus()
    event_bus.subscribe(EVENT_USER_CREATED, handle_user_created)
    event_bus.subscribe(EVENT_USER_UPDATED, handle_user_updated)

    event_bus.unsubscribe(EVENT_USER_CREATED, handle_user_created)
    event_bus.unsubscribe(EVENT_USER_UPDATED, handle_user_updated)

    assert len(event_bus.listeners) == 0


def test_event_bus_publish():
    event_bus = EventBus()

    # mock listener functions
    def listener1(data):
        assert data == {"user_id": 1, "username": "Donny"}

    def listener2(data):
        assert data == {"user_id": 1, "username": "Donny", "email": "donnydee@gmail.com"}

    event_bus.subscribe(EVENT_USER_CREATED, listener1)
    event_bus.subscribe(EVENT_USER_UPDATED, listener2)

    event_bus.publish(EVENT_USER_CREATED, {"user_id": 1, "username": "Donny"})
    event_bus.publish(EVENT_USER_UPDATED, {"user_id": 1, "username": "Donny", "email": "donnydee@gmail.com"})
