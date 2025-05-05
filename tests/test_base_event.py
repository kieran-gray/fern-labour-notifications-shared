from datetime import UTC, datetime

from fern_labour_notifications_shared.base_event import BaseEvent


def test_can_instantiate() -> None:
    event = BaseEvent(
        id="id123", type="test.event", data={"test": "data", "also": 123}, time=datetime.now(UTC)
    )
    assert isinstance(event, BaseEvent)

    cls_event = BaseEvent.create(data={"test": "data", "also": 123}, event_type="test.event")
    assert isinstance(cls_event, BaseEvent)


def test_can_serde_base_event() -> None:
    event = BaseEvent(
        id="id123", type="test.event", data={"test": "data", "also": 123}, time=datetime.now(UTC)
    )
    event_dict = event.to_dict()
    from_dict = BaseEvent.from_dict(event_dict)
    assert event == from_dict
