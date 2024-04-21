from enum import Enum


class DomainListingAdminServiceV1ModelListingResponseProcessStatus(str, Enum):
    ERROR = "error"
    FAILED = "failed"
    PROCESSED = "processed"
    PROCESSING = "processing"
    QUEUED = "queued"
    SEARCHABLE = "searchable"

    def __str__(self) -> str:
        return str(self.value)
