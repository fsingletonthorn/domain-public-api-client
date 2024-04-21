from enum import Enum


class StatisticsPostEvent(str, Enum):
    LISTINGADDEDTOSHORTLIST = "listingAddedToShortlist"
    LISTINGAGENTCALLED = "listingAgentCalled"
    LISTINGAGENTPHONEREVEALED = "listingAgentPhoneRevealed"
    LISTINGEMAILEDTOAFRIEND = "listingEmailedToAFriend"
    LISTINGENQUIRYSENT = "listingEnquirySent"
    LISTINGFLOORPLANVIEWED = "listingFloorPlanViewed"
    LISTINGIMAGEGALLERYVIEWED = "listingImageGalleryViewed"
    LISTINGIMAGEVIEWED = "listingImageViewed"
    LISTINGMAPVIEWED = "listingMapViewed"
    LISTINGNOTESADDED = "listingNotesAdded"
    LISTINGVIDEOVIEWED = "listingVideoViewed"
    LISTINGVIEWED = "listingViewed"
    LOANEVENTRAISED = "loanEventRaised"

    def __str__(self) -> str:
        return str(self.value)
