from fern_labour_notifications_shared.enums import NotificationChannel, NotificationTemplate


def test_can_instantiate_notification_channel() -> None:
    enum = NotificationChannel.EMAIL
    assert enum == "email"


def test_can_instantiate_notification_template() -> None:
    enum = NotificationTemplate.CONTACT_US_SUBMISSION
    assert enum == "contact_us_submission"
