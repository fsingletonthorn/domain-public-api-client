from enum import Enum


class PropertyEnrichmentV2ImageTypes(str, Enum):
    ADVERTISERIMAGE = "AdvertiserImage"
    AGENTCAROUSEL = "AgentCarousel"
    BUILDINGPHOTO = "BuildingPhoto"
    CONJUNCTIONAGENTLOGO = "ConjunctionAgentLogo"
    DEVELOPMENTPROJECTADVERTISEMENTPHOTO = "DevelopmentProjectAdvertisementPhoto"
    DEVELOPMENTPROJECTGALLERYPHOTO = "DevelopmentProjectGalleryPhoto"
    LISTINGPHOTO = "ListingPhoto"
    NEWDEVELOPMENTFEATUREDPHOTO = "NewDevelopmentFeaturedPhoto"
    NEWDEVELOPMENTLANDPHOTO = "NewDevelopmentLandPhoto"
    NEWDEVELOPMENTLUMIEREPHOTO = "NewDevelopmentLumierePhoto"
    NEWDEVELOPMENTREGIONALPHOTO = "NewDevelopmentRegionalPhoto"
    NEWFLOORPLANPHOTO = "NewFloorPlanPhoto"
    OLDFLOORPLANPHOTO = "OldFloorPlanPhoto"
    YOUWISHCLIP = "YouWishClip"

    def __str__(self) -> str:
        return str(self.value)
