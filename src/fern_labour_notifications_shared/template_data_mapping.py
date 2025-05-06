from fern_labour_notifications_shared.enums import NotificationTemplate
from fern_labour_notifications_shared.notification_data import (
    BaseNotificationData,
    ContactUsData,
    LabourAnnouncementData,
    LabourBegunData,
    LabourCompletedData,
    LabourCompletedWithNoteData,
    LabourInviteData,
    LabourUpdateData,
    SubscriberApprovedData,
    SubscriberInviteData,
    SubscriberRequestedData,
)

TEMPLATE_TO_PAYLOAD: dict[NotificationTemplate, type[BaseNotificationData]] = {
    NotificationTemplate.LABOUR_ANNOUNCEMENT: LabourAnnouncementData,
    NotificationTemplate.LABOUR_BEGUN: LabourBegunData,
    NotificationTemplate.LABOUR_COMPLETED: LabourCompletedData,
    NotificationTemplate.LABOUR_COMPLETED_WITH_NOTE: LabourCompletedWithNoteData,
    NotificationTemplate.LABOUR_UPDATE: LabourUpdateData,
    NotificationTemplate.LABOUR_INVITE: LabourInviteData,
    NotificationTemplate.CONTACT_US_SUBMISSION: ContactUsData,
    NotificationTemplate.SUBSCRIBER_APPROVED: SubscriberApprovedData,
    NotificationTemplate.SUBSCRIBER_INVITE: SubscriberInviteData,
    NotificationTemplate.SUBSCRIBER_REQUESTED: SubscriberRequestedData,
}
