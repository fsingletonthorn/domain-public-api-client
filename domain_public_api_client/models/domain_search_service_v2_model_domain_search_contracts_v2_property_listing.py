import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_listing_listing_type import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_listing_promo_level import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_advertiser import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_auction_schedule import (
        DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_inspection_schedule import (
        DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_media import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Media,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_price_details import (
        DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details import (
        DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_sold_data import (
        DomainSearchServiceV2ModelDomainSearchContractsV2SoldData,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing:
    """
    Attributes:
        promo_level (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel]):
        listing_type (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType]):
        id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        advertiser (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser]):
        price_details (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails]):
        media (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchContractsV2Media']]):
        property_details (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails]):
        headline (Union[Unset, str]):
        summary_description (Union[Unset, str]):
        has_floorplan (Union[Unset, bool]):
        has_video (Union[Unset, bool]):
        labels (Union[Unset, List[str]]):
        auction_schedule (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule]):
        date_available (Union[Unset, datetime.datetime]):
        date_listed (Union[Unset, datetime.datetime]):
        inspection_schedule (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule]):
        sold_data (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldData]):
        listing_slug (Union[Unset, str]):
    """

    promo_level: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel] = UNSET
    listing_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType] = UNSET
    id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    advertiser: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser"] = UNSET
    price_details: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails"] = UNSET
    media: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchContractsV2Media"]] = UNSET
    property_details: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails"] = UNSET
    headline: Union[Unset, str] = UNSET
    summary_description: Union[Unset, str] = UNSET
    has_floorplan: Union[Unset, bool] = UNSET
    has_video: Union[Unset, bool] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    auction_schedule: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule"] = UNSET
    date_available: Union[Unset, datetime.datetime] = UNSET
    date_listed: Union[Unset, datetime.datetime] = UNSET
    inspection_schedule: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule"] = UNSET
    sold_data: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2SoldData"] = UNSET
    listing_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promo_level: Union[Unset, str] = UNSET
        if not isinstance(self.promo_level, Unset):
            promo_level = self.promo_level.value

        listing_type: Union[Unset, str] = UNSET
        if not isinstance(self.listing_type, Unset):
            listing_type = self.listing_type.value

        id = self.id

        project_id = self.project_id

        advertiser: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advertiser, Unset):
            advertiser = self.advertiser.to_dict()

        price_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_details, Unset):
            price_details = self.price_details.to_dict()

        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        property_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_details, Unset):
            property_details = self.property_details.to_dict()

        headline = self.headline

        summary_description = self.summary_description

        has_floorplan = self.has_floorplan

        has_video = self.has_video

        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        auction_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction_schedule, Unset):
            auction_schedule = self.auction_schedule.to_dict()

        date_available: Union[Unset, str] = UNSET
        if not isinstance(self.date_available, Unset):
            date_available = self.date_available.isoformat()

        date_listed: Union[Unset, str] = UNSET
        if not isinstance(self.date_listed, Unset):
            date_listed = self.date_listed.isoformat()

        inspection_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inspection_schedule, Unset):
            inspection_schedule = self.inspection_schedule.to_dict()

        sold_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sold_data, Unset):
            sold_data = self.sold_data.to_dict()

        listing_slug = self.listing_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promo_level is not UNSET:
            field_dict["promoLevel"] = promo_level
        if listing_type is not UNSET:
            field_dict["listingType"] = listing_type
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if advertiser is not UNSET:
            field_dict["advertiser"] = advertiser
        if price_details is not UNSET:
            field_dict["priceDetails"] = price_details
        if media is not UNSET:
            field_dict["media"] = media
        if property_details is not UNSET:
            field_dict["propertyDetails"] = property_details
        if headline is not UNSET:
            field_dict["headline"] = headline
        if summary_description is not UNSET:
            field_dict["summaryDescription"] = summary_description
        if has_floorplan is not UNSET:
            field_dict["hasFloorplan"] = has_floorplan
        if has_video is not UNSET:
            field_dict["hasVideo"] = has_video
        if labels is not UNSET:
            field_dict["labels"] = labels
        if auction_schedule is not UNSET:
            field_dict["auctionSchedule"] = auction_schedule
        if date_available is not UNSET:
            field_dict["dateAvailable"] = date_available
        if date_listed is not UNSET:
            field_dict["dateListed"] = date_listed
        if inspection_schedule is not UNSET:
            field_dict["inspectionSchedule"] = inspection_schedule
        if sold_data is not UNSET:
            field_dict["soldData"] = sold_data
        if listing_slug is not UNSET:
            field_dict["listingSlug"] = listing_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_advertiser import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_auction_schedule import (
            DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_inspection_schedule import (
            DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_media import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Media,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_price_details import (
            DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details import (
            DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_sold_data import (
            DomainSearchServiceV2ModelDomainSearchContractsV2SoldData,
        )

        d = src_dict.copy()
        _promo_level = d.pop("promoLevel", UNSET)
        promo_level: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel]
        if isinstance(_promo_level, Unset):
            promo_level = UNSET
        else:
            promo_level = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel(_promo_level)

        _listing_type = d.pop("listingType", UNSET)
        listing_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType]
        if isinstance(_listing_type, Unset):
            listing_type = UNSET
        else:
            listing_type = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType(_listing_type)

        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

        _advertiser = d.pop("advertiser", UNSET)
        advertiser: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser]
        if isinstance(_advertiser, Unset):
            advertiser = UNSET
        else:
            advertiser = DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser.from_dict(_advertiser)

        _price_details = d.pop("priceDetails", UNSET)
        price_details: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails]
        if isinstance(_price_details, Unset):
            price_details = UNSET
        else:
            price_details = DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails.from_dict(_price_details)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = DomainSearchServiceV2ModelDomainSearchContractsV2Media.from_dict(media_item_data)

            media.append(media_item)

        _property_details = d.pop("propertyDetails", UNSET)
        property_details: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails]
        if isinstance(_property_details, Unset):
            property_details = UNSET
        else:
            property_details = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails.from_dict(
                _property_details
            )

        headline = d.pop("headline", UNSET)

        summary_description = d.pop("summaryDescription", UNSET)

        has_floorplan = d.pop("hasFloorplan", UNSET)

        has_video = d.pop("hasVideo", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        _auction_schedule = d.pop("auctionSchedule", UNSET)
        auction_schedule: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule]
        if isinstance(_auction_schedule, Unset):
            auction_schedule = UNSET
        else:
            auction_schedule = DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule.from_dict(
                _auction_schedule
            )

        _date_available = d.pop("dateAvailable", UNSET)
        date_available: Union[Unset, datetime.datetime]
        if isinstance(_date_available, Unset):
            date_available = UNSET
        else:
            date_available = isoparse(_date_available)

        _date_listed = d.pop("dateListed", UNSET)
        date_listed: Union[Unset, datetime.datetime]
        if isinstance(_date_listed, Unset):
            date_listed = UNSET
        else:
            date_listed = isoparse(_date_listed)

        _inspection_schedule = d.pop("inspectionSchedule", UNSET)
        inspection_schedule: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule]
        if isinstance(_inspection_schedule, Unset):
            inspection_schedule = UNSET
        else:
            inspection_schedule = DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule.from_dict(
                _inspection_schedule
            )

        _sold_data = d.pop("soldData", UNSET)
        sold_data: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldData]
        if isinstance(_sold_data, Unset):
            sold_data = UNSET
        else:
            sold_data = DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.from_dict(_sold_data)

        listing_slug = d.pop("listingSlug", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_property_listing = cls(
            promo_level=promo_level,
            listing_type=listing_type,
            id=id,
            project_id=project_id,
            advertiser=advertiser,
            price_details=price_details,
            media=media,
            property_details=property_details,
            headline=headline,
            summary_description=summary_description,
            has_floorplan=has_floorplan,
            has_video=has_video,
            labels=labels,
            auction_schedule=auction_schedule,
            date_available=date_available,
            date_listed=date_listed,
            inspection_schedule=inspection_schedule,
            sold_data=sold_data,
            listing_slug=listing_slug,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_property_listing.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_property_listing

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
