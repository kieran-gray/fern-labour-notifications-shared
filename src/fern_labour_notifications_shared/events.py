from dataclasses import dataclass
from typing import Any, Self

from fern_labour_notifications_shared.base_event import BaseEvent


@dataclass
class NotificationRequested(BaseEvent):
    @classmethod
    def create(cls, data: dict[str, Any], event_type: str = "notification.requested") -> Self:
        return super().create(event_type=event_type, data=data)
