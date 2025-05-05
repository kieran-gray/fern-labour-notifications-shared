from fern_labour_notifications_shared.events import NotificationRequested
from fern_labour_notifications_shared.notification_data import LabourUpdateData


def can_instantiate_notification_data_type() -> None:
    dataclass = LabourUpdateData(
        birthing_person_name="test",
        subscriber_first_name="test",
        update="test",
        link="test",
        notes="test",
    )
    if not dataclass:
        raise RuntimeError("Notification Dataclass instantiation failed.")
    print("Instantiated Notification Dataclass successfully.")


def can_instantiate_event() -> None:
    event = NotificationRequested.create(data={})
    if not event:
        raise RuntimeError("Event instantiation failed.")
    print("Instantiated Event successfully.")


if __name__ == "__main__":
    can_instantiate_notification_data_type()
    can_instantiate_event()
