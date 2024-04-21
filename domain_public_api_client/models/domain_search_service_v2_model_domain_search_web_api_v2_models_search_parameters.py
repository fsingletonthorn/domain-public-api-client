import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters_listing_attributes_item import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingAttributesItem,
)
from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters_listing_type import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType,
)
from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters_property_established_type import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType,
)
from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters_property_features_item import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyFeaturesItem,
)
from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters_property_types_item import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_window import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_school_catchment import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSchoolCatchment,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_location import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery,
    )
    from ..models.domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by import (
        DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters:
    """
    Attributes:
        listing_type (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType]):
        property_types (Union[Unset,
            List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyTypesItem]]):
        property_features (Union[Unset,
            List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyFeaturesItem]]):
        listing_attributes (Union[Unset,
            List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingAttributesItem]]):
        property_established_type (Union[Unset,
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType]):
        min_bedrooms (Union[Unset, float]):
        max_bedrooms (Union[Unset, float]):
        min_bathrooms (Union[Unset, float]):
        max_bathrooms (Union[Unset, float]):
        min_carspaces (Union[Unset, int]):
        max_carspaces (Union[Unset, int]):
        min_price (Union[Unset, int]):
        max_price (Union[Unset, int]):
        min_land_area (Union[Unset, int]):
        max_land_area (Union[Unset, int]):
        advertiser_ids (Union[Unset, List[int]]):
        ad_ids (Union[Unset, List[int]]):
        exclude_ad_ids (Union[Unset, List[int]]):
        locations (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation']]):
        school_catchments (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSchoolCatchment']]):
        location_terms (Union[Unset, str]):
        keywords (Union[Unset, List[str]]):
        new_dev_only (Union[Unset, bool]):
        inspection_from (Union[Unset, datetime.datetime]):
        inspection_to (Union[Unset, datetime.datetime]):
        auction_from (Union[Unset, datetime.datetime]):
        auction_to (Union[Unset, datetime.datetime]):
        date_available_from (Union[Unset, datetime.datetime]):
        date_available_to (Union[Unset, datetime.datetime]):
        rural_only (Union[Unset, bool]):
        exclude_price_withheld (Union[Unset, bool]):
        exclude_deposit_taken (Union[Unset, bool]):
        topspot_keywords (Union[Unset, List[str]]):
        custom_sort (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort]):
        sort (Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy]):
        page_size (Union[Unset, int]):
        geo_window (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow]):
        updated_since (Union[Unset, datetime.datetime]):
        listed_since (Union[Unset, datetime.datetime]):
        include_inspection_aggregations (Union[Unset, bool]):
        tags (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery']]):
        page_number (Union[Unset, int]):
    """

    listing_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType] = UNSET
    property_types: Union[
        Unset, List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyTypesItem]
    ] = UNSET
    property_features: Union[
        Unset, List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyFeaturesItem]
    ] = UNSET
    listing_attributes: Union[
        Unset, List[DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingAttributesItem]
    ] = UNSET
    property_established_type: Union[
        Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType
    ] = UNSET
    min_bedrooms: Union[Unset, float] = UNSET
    max_bedrooms: Union[Unset, float] = UNSET
    min_bathrooms: Union[Unset, float] = UNSET
    max_bathrooms: Union[Unset, float] = UNSET
    min_carspaces: Union[Unset, int] = UNSET
    max_carspaces: Union[Unset, int] = UNSET
    min_price: Union[Unset, int] = UNSET
    max_price: Union[Unset, int] = UNSET
    min_land_area: Union[Unset, int] = UNSET
    max_land_area: Union[Unset, int] = UNSET
    advertiser_ids: Union[Unset, List[int]] = UNSET
    ad_ids: Union[Unset, List[int]] = UNSET
    exclude_ad_ids: Union[Unset, List[int]] = UNSET
    locations: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation"]] = UNSET
    school_catchments: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSchoolCatchment"]] = UNSET
    location_terms: Union[Unset, str] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    new_dev_only: Union[Unset, bool] = UNSET
    inspection_from: Union[Unset, datetime.datetime] = UNSET
    inspection_to: Union[Unset, datetime.datetime] = UNSET
    auction_from: Union[Unset, datetime.datetime] = UNSET
    auction_to: Union[Unset, datetime.datetime] = UNSET
    date_available_from: Union[Unset, datetime.datetime] = UNSET
    date_available_to: Union[Unset, datetime.datetime] = UNSET
    rural_only: Union[Unset, bool] = UNSET
    exclude_price_withheld: Union[Unset, bool] = UNSET
    exclude_deposit_taken: Union[Unset, bool] = UNSET
    topspot_keywords: Union[Unset, List[str]] = UNSET
    custom_sort: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort"] = UNSET
    sort: Union[Unset, "DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy"] = UNSET
    page_size: Union[Unset, int] = UNSET
    geo_window: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow"] = UNSET
    updated_since: Union[Unset, datetime.datetime] = UNSET
    listed_since: Union[Unset, datetime.datetime] = UNSET
    include_inspection_aggregations: Union[Unset, bool] = UNSET
    tags: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery"]] = UNSET
    page_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing_type: Union[Unset, str] = UNSET
        if not isinstance(self.listing_type, Unset):
            listing_type = self.listing_type.value

        property_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_types, Unset):
            property_types = []
            for property_types_item_data in self.property_types:
                property_types_item = property_types_item_data.value
                property_types.append(property_types_item)

        property_features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_features, Unset):
            property_features = []
            for property_features_item_data in self.property_features:
                property_features_item = property_features_item_data.value
                property_features.append(property_features_item)

        listing_attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.listing_attributes, Unset):
            listing_attributes = []
            for listing_attributes_item_data in self.listing_attributes:
                listing_attributes_item = listing_attributes_item_data.value
                listing_attributes.append(listing_attributes_item)

        property_established_type: Union[Unset, str] = UNSET
        if not isinstance(self.property_established_type, Unset):
            property_established_type = self.property_established_type.value

        min_bedrooms = self.min_bedrooms

        max_bedrooms = self.max_bedrooms

        min_bathrooms = self.min_bathrooms

        max_bathrooms = self.max_bathrooms

        min_carspaces = self.min_carspaces

        max_carspaces = self.max_carspaces

        min_price = self.min_price

        max_price = self.max_price

        min_land_area = self.min_land_area

        max_land_area = self.max_land_area

        advertiser_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.advertiser_ids, Unset):
            advertiser_ids = self.advertiser_ids

        ad_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ad_ids, Unset):
            ad_ids = self.ad_ids

        exclude_ad_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.exclude_ad_ids, Unset):
            exclude_ad_ids = self.exclude_ad_ids

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        school_catchments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.school_catchments, Unset):
            school_catchments = []
            for school_catchments_item_data in self.school_catchments:
                school_catchments_item = school_catchments_item_data.to_dict()
                school_catchments.append(school_catchments_item)

        location_terms = self.location_terms

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        new_dev_only = self.new_dev_only

        inspection_from: Union[Unset, str] = UNSET
        if not isinstance(self.inspection_from, Unset):
            inspection_from = self.inspection_from.isoformat()

        inspection_to: Union[Unset, str] = UNSET
        if not isinstance(self.inspection_to, Unset):
            inspection_to = self.inspection_to.isoformat()

        auction_from: Union[Unset, str] = UNSET
        if not isinstance(self.auction_from, Unset):
            auction_from = self.auction_from.isoformat()

        auction_to: Union[Unset, str] = UNSET
        if not isinstance(self.auction_to, Unset):
            auction_to = self.auction_to.isoformat()

        date_available_from: Union[Unset, str] = UNSET
        if not isinstance(self.date_available_from, Unset):
            date_available_from = self.date_available_from.isoformat()

        date_available_to: Union[Unset, str] = UNSET
        if not isinstance(self.date_available_to, Unset):
            date_available_to = self.date_available_to.isoformat()

        rural_only = self.rural_only

        exclude_price_withheld = self.exclude_price_withheld

        exclude_deposit_taken = self.exclude_deposit_taken

        topspot_keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.topspot_keywords, Unset):
            topspot_keywords = self.topspot_keywords

        custom_sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_sort, Unset):
            custom_sort = self.custom_sort.to_dict()

        sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        page_size = self.page_size

        geo_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_window, Unset):
            geo_window = self.geo_window.to_dict()

        updated_since: Union[Unset, str] = UNSET
        if not isinstance(self.updated_since, Unset):
            updated_since = self.updated_since.isoformat()

        listed_since: Union[Unset, str] = UNSET
        if not isinstance(self.listed_since, Unset):
            listed_since = self.listed_since.isoformat()

        include_inspection_aggregations = self.include_inspection_aggregations

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        page_number = self.page_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listing_type is not UNSET:
            field_dict["listingType"] = listing_type
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if property_features is not UNSET:
            field_dict["propertyFeatures"] = property_features
        if listing_attributes is not UNSET:
            field_dict["listingAttributes"] = listing_attributes
        if property_established_type is not UNSET:
            field_dict["propertyEstablishedType"] = property_established_type
        if min_bedrooms is not UNSET:
            field_dict["minBedrooms"] = min_bedrooms
        if max_bedrooms is not UNSET:
            field_dict["maxBedrooms"] = max_bedrooms
        if min_bathrooms is not UNSET:
            field_dict["minBathrooms"] = min_bathrooms
        if max_bathrooms is not UNSET:
            field_dict["maxBathrooms"] = max_bathrooms
        if min_carspaces is not UNSET:
            field_dict["minCarspaces"] = min_carspaces
        if max_carspaces is not UNSET:
            field_dict["maxCarspaces"] = max_carspaces
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if min_land_area is not UNSET:
            field_dict["minLandArea"] = min_land_area
        if max_land_area is not UNSET:
            field_dict["maxLandArea"] = max_land_area
        if advertiser_ids is not UNSET:
            field_dict["advertiserIds"] = advertiser_ids
        if ad_ids is not UNSET:
            field_dict["adIds"] = ad_ids
        if exclude_ad_ids is not UNSET:
            field_dict["excludeAdIds"] = exclude_ad_ids
        if locations is not UNSET:
            field_dict["locations"] = locations
        if school_catchments is not UNSET:
            field_dict["schoolCatchments"] = school_catchments
        if location_terms is not UNSET:
            field_dict["locationTerms"] = location_terms
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if new_dev_only is not UNSET:
            field_dict["newDevOnly"] = new_dev_only
        if inspection_from is not UNSET:
            field_dict["inspectionFrom"] = inspection_from
        if inspection_to is not UNSET:
            field_dict["inspectionTo"] = inspection_to
        if auction_from is not UNSET:
            field_dict["auctionFrom"] = auction_from
        if auction_to is not UNSET:
            field_dict["auctionTo"] = auction_to
        if date_available_from is not UNSET:
            field_dict["dateAvailableFrom"] = date_available_from
        if date_available_to is not UNSET:
            field_dict["dateAvailableTo"] = date_available_to
        if rural_only is not UNSET:
            field_dict["ruralOnly"] = rural_only
        if exclude_price_withheld is not UNSET:
            field_dict["excludePriceWithheld"] = exclude_price_withheld
        if exclude_deposit_taken is not UNSET:
            field_dict["excludeDepositTaken"] = exclude_deposit_taken
        if topspot_keywords is not UNSET:
            field_dict["topspotKeywords"] = topspot_keywords
        if custom_sort is not UNSET:
            field_dict["customSort"] = custom_sort
        if sort is not UNSET:
            field_dict["sort"] = sort
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if geo_window is not UNSET:
            field_dict["geoWindow"] = geo_window
        if updated_since is not UNSET:
            field_dict["updatedSince"] = updated_since
        if listed_since is not UNSET:
            field_dict["listedSince"] = listed_since
        if include_inspection_aggregations is not UNSET:
            field_dict["includeInspectionAggregations"] = include_inspection_aggregations
        if tags is not UNSET:
            field_dict["tags"] = tags
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_window import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_school_catchment import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSchoolCatchment,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_location import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery,
        )
        from ..models.domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by import (
            DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy,
        )

        d = src_dict.copy()
        _listing_type = d.pop("listingType", UNSET)
        listing_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType]
        if isinstance(_listing_type, Unset):
            listing_type = UNSET
        else:
            listing_type = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType(
                _listing_type
            )

        property_types = []
        _property_types = d.pop("propertyTypes", UNSET)
        for property_types_item_data in _property_types or []:
            property_types_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyTypesItem(
                property_types_item_data
            )

            property_types.append(property_types_item)

        property_features = []
        _property_features = d.pop("propertyFeatures", UNSET)
        for property_features_item_data in _property_features or []:
            property_features_item = (
                DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyFeaturesItem(
                    property_features_item_data
                )
            )

            property_features.append(property_features_item)

        listing_attributes = []
        _listing_attributes = d.pop("listingAttributes", UNSET)
        for listing_attributes_item_data in _listing_attributes or []:
            listing_attributes_item = (
                DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingAttributesItem(
                    listing_attributes_item_data
                )
            )

            listing_attributes.append(listing_attributes_item)

        _property_established_type = d.pop("propertyEstablishedType", UNSET)
        property_established_type: Union[
            Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType
        ]
        if isinstance(_property_established_type, Unset):
            property_established_type = UNSET
        else:
            property_established_type = (
                DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType(
                    _property_established_type
                )
            )

        min_bedrooms = d.pop("minBedrooms", UNSET)

        max_bedrooms = d.pop("maxBedrooms", UNSET)

        min_bathrooms = d.pop("minBathrooms", UNSET)

        max_bathrooms = d.pop("maxBathrooms", UNSET)

        min_carspaces = d.pop("minCarspaces", UNSET)

        max_carspaces = d.pop("maxCarspaces", UNSET)

        min_price = d.pop("minPrice", UNSET)

        max_price = d.pop("maxPrice", UNSET)

        min_land_area = d.pop("minLandArea", UNSET)

        max_land_area = d.pop("maxLandArea", UNSET)

        advertiser_ids = cast(List[int], d.pop("advertiserIds", UNSET))

        ad_ids = cast(List[int], d.pop("adIds", UNSET))

        exclude_ad_ids = cast(List[int], d.pop("excludeAdIds", UNSET))

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        school_catchments = []
        _school_catchments = d.pop("schoolCatchments", UNSET)
        for school_catchments_item_data in _school_catchments or []:
            school_catchments_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSchoolCatchment.from_dict(
                school_catchments_item_data
            )

            school_catchments.append(school_catchments_item)

        location_terms = d.pop("locationTerms", UNSET)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        new_dev_only = d.pop("newDevOnly", UNSET)

        _inspection_from = d.pop("inspectionFrom", UNSET)
        inspection_from: Union[Unset, datetime.datetime]
        if isinstance(_inspection_from, Unset):
            inspection_from = UNSET
        else:
            inspection_from = isoparse(_inspection_from)

        _inspection_to = d.pop("inspectionTo", UNSET)
        inspection_to: Union[Unset, datetime.datetime]
        if isinstance(_inspection_to, Unset):
            inspection_to = UNSET
        else:
            inspection_to = isoparse(_inspection_to)

        _auction_from = d.pop("auctionFrom", UNSET)
        auction_from: Union[Unset, datetime.datetime]
        if isinstance(_auction_from, Unset):
            auction_from = UNSET
        else:
            auction_from = isoparse(_auction_from)

        _auction_to = d.pop("auctionTo", UNSET)
        auction_to: Union[Unset, datetime.datetime]
        if isinstance(_auction_to, Unset):
            auction_to = UNSET
        else:
            auction_to = isoparse(_auction_to)

        _date_available_from = d.pop("dateAvailableFrom", UNSET)
        date_available_from: Union[Unset, datetime.datetime]
        if isinstance(_date_available_from, Unset):
            date_available_from = UNSET
        else:
            date_available_from = isoparse(_date_available_from)

        _date_available_to = d.pop("dateAvailableTo", UNSET)
        date_available_to: Union[Unset, datetime.datetime]
        if isinstance(_date_available_to, Unset):
            date_available_to = UNSET
        else:
            date_available_to = isoparse(_date_available_to)

        rural_only = d.pop("ruralOnly", UNSET)

        exclude_price_withheld = d.pop("excludePriceWithheld", UNSET)

        exclude_deposit_taken = d.pop("excludeDepositTaken", UNSET)

        topspot_keywords = cast(List[str], d.pop("topspotKeywords", UNSET))

        _custom_sort = d.pop("customSort", UNSET)
        custom_sort: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort]
        if isinstance(_custom_sort, Unset):
            custom_sort = UNSET
        else:
            custom_sort = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort.from_dict(_custom_sort)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy.from_dict(_sort)

        page_size = d.pop("pageSize", UNSET)

        _geo_window = d.pop("geoWindow", UNSET)
        geo_window: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow]
        if isinstance(_geo_window, Unset):
            geo_window = UNSET
        else:
            geo_window = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow.from_dict(_geo_window)

        _updated_since = d.pop("updatedSince", UNSET)
        updated_since: Union[Unset, datetime.datetime]
        if isinstance(_updated_since, Unset):
            updated_since = UNSET
        else:
            updated_since = isoparse(_updated_since)

        _listed_since = d.pop("listedSince", UNSET)
        listed_since: Union[Unset, datetime.datetime]
        if isinstance(_listed_since, Unset):
            listed_since = UNSET
        else:
            listed_since = isoparse(_listed_since)

        include_inspection_aggregations = d.pop("includeInspectionAggregations", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery.from_dict(tags_item_data)

            tags.append(tags_item)

        page_number = d.pop("pageNumber", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters = cls(
            listing_type=listing_type,
            property_types=property_types,
            property_features=property_features,
            listing_attributes=listing_attributes,
            property_established_type=property_established_type,
            min_bedrooms=min_bedrooms,
            max_bedrooms=max_bedrooms,
            min_bathrooms=min_bathrooms,
            max_bathrooms=max_bathrooms,
            min_carspaces=min_carspaces,
            max_carspaces=max_carspaces,
            min_price=min_price,
            max_price=max_price,
            min_land_area=min_land_area,
            max_land_area=max_land_area,
            advertiser_ids=advertiser_ids,
            ad_ids=ad_ids,
            exclude_ad_ids=exclude_ad_ids,
            locations=locations,
            school_catchments=school_catchments,
            location_terms=location_terms,
            keywords=keywords,
            new_dev_only=new_dev_only,
            inspection_from=inspection_from,
            inspection_to=inspection_to,
            auction_from=auction_from,
            auction_to=auction_to,
            date_available_from=date_available_from,
            date_available_to=date_available_to,
            rural_only=rural_only,
            exclude_price_withheld=exclude_price_withheld,
            exclude_deposit_taken=exclude_deposit_taken,
            topspot_keywords=topspot_keywords,
            custom_sort=custom_sort,
            sort=sort,
            page_size=page_size,
            geo_window=geo_window,
            updated_since=updated_since,
            listed_since=listed_since,
            include_inspection_aggregations=include_inspection_aggregations,
            tags=tags,
            page_number=page_number,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters

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
