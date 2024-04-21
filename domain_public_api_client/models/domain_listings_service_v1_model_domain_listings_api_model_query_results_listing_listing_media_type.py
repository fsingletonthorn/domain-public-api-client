from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType(str, Enum):
    FLOORPLAN = "floorplan"
    MP4 = "mp4"
    NOTSPECIFIED = "notSpecified"
    PHOTO = "photo"
    VIMEO = "vimeo"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
