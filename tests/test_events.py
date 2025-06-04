from fern_labour_notifications_shared.events import NotificationRequested


def test_can_instantiate_notification_requested_event() -> None:
    event = NotificationRequested.create(
        aggregate_id="test", aggregate_type="test", data={"test": "data", "also": 123}
    )
    assert isinstance(event, NotificationRequested)
    assert event.type == "notification.requested"
