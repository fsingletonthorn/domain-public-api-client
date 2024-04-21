from enum import Enum


class EnquiriesV1RecipientRecipientType(str, Enum):
    HIDDEN = "hidden"
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
