from enum import Enum


class ListingsV2PdfUploadType(str, Enum):
    COMMERCIALPDF = "commercialPdf"
    DEVPROJECTMASTERPLANPDF = "devProjectMasterplanPdf"
    DEVPROJECTPDF = "devProjectPdf"
    FLOORPLANPDF = "floorplanPdf"
    NEWDEVBROCHUREPDF = "newDevBrochurePdf"

    def __str__(self) -> str:
        return str(self.value)
