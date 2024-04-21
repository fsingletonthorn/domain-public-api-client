from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_ad import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialAd,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_advertiser import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_location import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_media import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialMedia,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_metadata import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialListing")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialListing:
    """Listing details for univesal app

    Attributes:
        ad (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAd]): Listing details
        price (Union[Unset, str]): Formatted listing price
        advertiser (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser]): Agency details
        geo_location (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation]): Geographic
            coordinate
        property_area (Union[Unset, str]): Building size
        property_type (Union[Unset, str]): Property type
        address (Union[Unset, str]): Full address
        headline (Union[Unset, str]): Headline
        has_video (Union[Unset, bool]): Has video?
        media (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialMedia']]): Media resources for
            listing (images, video, floor plans)
        auction_date (Union[Unset, str]): Auction date
        id (Union[Unset, int]): AdID
        metadata (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata]): Listing metadata
        carspace_count (Union[Unset, int]): Car parking spaces count
    """

    ad: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialAd"] = UNSET
    price: Union[Unset, str] = UNSET
    advertiser: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser"] = UNSET
    geo_location: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation"] = UNSET
    property_area: Union[Unset, str] = UNSET
    property_type: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    has_video: Union[Unset, bool] = UNSET
    media: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialMedia"]] = UNSET
    auction_date: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    metadata: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata"] = UNSET
    carspace_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ad: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ad, Unset):
            ad = self.ad.to_dict()

        price = self.price

        advertiser: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advertiser, Unset):
            advertiser = self.advertiser.to_dict()

        geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        property_area = self.property_area

        property_type = self.property_type

        address = self.address

        headline = self.headline

        has_video = self.has_video

        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        auction_date = self.auction_date

        id = self.id

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        carspace_count = self.carspace_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad is not UNSET:
            field_dict["ad"] = ad
        if price is not UNSET:
            field_dict["price"] = price
        if advertiser is not UNSET:
            field_dict["advertiser"] = advertiser
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if property_area is not UNSET:
            field_dict["propertyArea"] = property_area
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if address is not UNSET:
            field_dict["address"] = address
        if headline is not UNSET:
            field_dict["headline"] = headline
        if has_video is not UNSET:
            field_dict["hasVideo"] = has_video
        if media is not UNSET:
            field_dict["media"] = media
        if auction_date is not UNSET:
            field_dict["auctionDate"] = auction_date
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if carspace_count is not UNSET:
            field_dict["carspaceCount"] = carspace_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_ad import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialAd,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_advertiser import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_location import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_media import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialMedia,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_metadata import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata,
        )

        d = src_dict.copy()
        _ad = d.pop("ad", UNSET)
        ad: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAd]
        if isinstance(_ad, Unset):
            ad = UNSET
        else:
            ad = DomainPublicAdapterWebApiModelsV1ListingsCommercialAd.from_dict(_ad)

        price = d.pop("price", UNSET)

        _advertiser = d.pop("advertiser", UNSET)
        advertiser: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser]
        if isinstance(_advertiser, Unset):
            advertiser = UNSET
        else:
            advertiser = DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser.from_dict(_advertiser)

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation]
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoLocation.from_dict(_geo_location)

        property_area = d.pop("propertyArea", UNSET)

        property_type = d.pop("propertyType", UNSET)

        address = d.pop("address", UNSET)

        headline = d.pop("headline", UNSET)

        has_video = d.pop("hasVideo", UNSET)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialMedia.from_dict(media_item_data)

            media.append(media_item)

        auction_date = d.pop("auctionDate", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata.from_dict(_metadata)

        carspace_count = d.pop("carspaceCount", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_listing = cls(
            ad=ad,
            price=price,
            advertiser=advertiser,
            geo_location=geo_location,
            property_area=property_area,
            property_type=property_type,
            address=address,
            headline=headline,
            has_video=has_video,
            media=media,
            auction_date=auction_date,
            id=id,
            metadata=metadata,
            carspace_count=carspace_count,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_listing.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_listing

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
