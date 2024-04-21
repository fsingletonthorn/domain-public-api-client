from enum import Enum


class EnquiriesV1RecipientDeliveryStatusDeliveryStatus(str, Enum):
    DEFERRED = "deferred"
    DELIVERED = "delivered"
    FAILED = "failed"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
