from fern_labour_notifications_shared.enums import NotificationTemplate
from fern_labour_notifications_shared.notification_data import BaseNotificationData
from fern_labour_notifications_shared.template_data_mapping import TEMPLATE_TO_PAYLOAD


def test_all_templates_have_payload() -> None:
    for template in NotificationTemplate:
        payload = TEMPLATE_TO_PAYLOAD[template]
        assert isinstance(payload, BaseNotificationData)
