from enum import Enum


class ListingAdminV2PropertyMediaResourceType(str, Enum):
    FLOORPLAN = "floorPlan"
    PHOTOGRAPH = "photograph"
    VIDEO = "video"
    VIRTUALTOUR = "virtualTour"
    WEBLINK = "webLink"

    def __str__(self) -> str:
        return str(self.value)
