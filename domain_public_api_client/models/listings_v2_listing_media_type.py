from enum import Enum


class ListingsV2ListingMediaType(str, Enum):
    FLOORPLAN = "floorplan"
    MP4 = "mp4"
    NOTSPECIFIED = "notSpecified"
    PHOTO = "photo"
    VIMEO = "vimeo"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
