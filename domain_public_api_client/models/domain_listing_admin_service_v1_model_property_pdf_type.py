from enum import Enum


class DomainListingAdminServiceV1ModelPropertyPdfType(str, Enum):
    COMMERCIALPDF = "commercialPdf"
    DEVPROJECTPDF = "devProjectPdf"
    FLOORPLANPDF = "floorplanPdf"
    NEWDEVBROCHUREPDF = "newDevBrochurePdf"

    def __str__(self) -> str:
        return str(self.value)
