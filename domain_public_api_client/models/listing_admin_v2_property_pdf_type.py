from enum import Enum


class ListingAdminV2PropertyPdfType(str, Enum):
    COMMERCIALPDF = "commercialPdf"
    DEVPROJECTMASTERPLANPDF = "devProjectMasterplanPdf"
    DEVPROJECTPDF = "devProjectPdf"
    FLOORPLANPDF = "floorplanPdf"
    NEWDEVBROCHUREPDF = "newDevBrochurePdf"

    def __str__(self) -> str:
        return str(self.value)
