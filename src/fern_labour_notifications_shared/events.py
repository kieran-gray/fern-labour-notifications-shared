from dataclasses import dataclass
from typing import Any, Self

from fern_labour_core.events.event import DomainEvent


@dataclass(frozen=True)
class NotificationRequested(DomainEvent):
    @classmethod
    def create(
        cls,
        aggregate_id: str,
        aggregate_type: str,
        data: dict[str, Any],
        event_type: str = "notification.requested",
    ) -> Self:
        return super().create(
            aggregate_id=aggregate_id,
            aggregate_type=aggregate_type,
            event_type=event_type,
            data=data,
        )
