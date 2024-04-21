from enum import Enum


class ListingsV2ProjectMediaType(str, Enum):
    PHOTO = "photo"
    POSTER = "poster"
    VIDEO = "video"
    VIRTUALTOUR = "virtualTour"
    WEBLINK = "webLink"

    def __str__(self) -> str:
        return str(self.value)
