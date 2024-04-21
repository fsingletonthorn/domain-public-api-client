from enum import Enum


class EnquiriesV1EnquiryReportEnquiryType(str, Enum):
    AGENCYPROFILE = "agencyProfile"
    AGENTPROFILE = "agentProfile"
    CONTRACTREQUEST = "contractRequest"
    DEVPROJECT = "devProject"
    LISTING = "listing"
    NEWDEVLANDING = "newDevLanding"
    PREPORTALLISTING = "prePortalListing"
    VENDORENQUIRY = "vendorEnquiry"

    def __str__(self) -> str:
        return str(self.value)
