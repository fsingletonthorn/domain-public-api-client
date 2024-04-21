from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_listings_business_search_request_property_types_item import (
    DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestPropertyTypesItem,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_business_search_request_search_mode import (
    DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_business_search_request_sort import (
    DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_business_location_search import (
        DomainPublicAdapterWebApiModelsV1ListingsBusinessLocationSearch,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_business_price_search import (
        DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest:
    """Represents a CRE Business Search Request

    Attributes:
        page_number (Union[Unset, int]):
        advertiser_id (Union[Unset, int]): AdvertiserId e.g. An Agency ID
        property_types (Union[Unset,
            List[DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestPropertyTypesItem]]): Listing property types
        keywords (Union[Unset, List[str]]): Search listings by keyword
        brand_id (Union[Unset, int]): The franchise brand ID
        franchise_group_id (Union[Unset, int]): The franchise group ID. A franchise group owns multiple franchise
            brands.
        locations (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsBusinessLocationSearch']]): Location
            search criteria
        page_size (Union[Unset, int]): Search results page size
        price (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch]): Search criteria. Price
        sort (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort]): Sorting order
        search_mode (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode]): Search
            mode
    """

    page_number: Union[Unset, int] = UNSET
    advertiser_id: Union[Unset, int] = UNSET
    property_types: Union[
        Unset, List[DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestPropertyTypesItem]
    ] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    brand_id: Union[Unset, int] = UNSET
    franchise_group_id: Union[Unset, int] = UNSET
    locations: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsBusinessLocationSearch"]] = UNSET
    page_size: Union[Unset, int] = UNSET
    price: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch"] = UNSET
    sort: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort] = UNSET
    search_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_number = self.page_number

        advertiser_id = self.advertiser_id

        property_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_types, Unset):
            property_types = []
            for property_types_item_data in self.property_types:
                property_types_item = property_types_item_data.value
                property_types.append(property_types_item)

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        brand_id = self.brand_id

        franchise_group_id = self.franchise_group_id

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        page_size = self.page_size

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        sort: Union[Unset, str] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        search_mode: Union[Unset, str] = UNSET
        if not isinstance(self.search_mode, Unset):
            search_mode = self.search_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if advertiser_id is not UNSET:
            field_dict["advertiserId"] = advertiser_id
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if brand_id is not UNSET:
            field_dict["brandId"] = brand_id
        if franchise_group_id is not UNSET:
            field_dict["franchiseGroupId"] = franchise_group_id
        if locations is not UNSET:
            field_dict["locations"] = locations
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if price is not UNSET:
            field_dict["price"] = price
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search_mode is not UNSET:
            field_dict["searchMode"] = search_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_business_location_search import (
            DomainPublicAdapterWebApiModelsV1ListingsBusinessLocationSearch,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_business_price_search import (
            DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch,
        )

        d = src_dict.copy()
        page_number = d.pop("pageNumber", UNSET)

        advertiser_id = d.pop("advertiserId", UNSET)

        property_types = []
        _property_types = d.pop("propertyTypes", UNSET)
        for property_types_item_data in _property_types or []:
            property_types_item = DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestPropertyTypesItem(
                property_types_item_data
            )

            property_types.append(property_types_item)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        brand_id = d.pop("brandId", UNSET)

        franchise_group_id = d.pop("franchiseGroupId", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = DomainPublicAdapterWebApiModelsV1ListingsBusinessLocationSearch.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        page_size = d.pop("pageSize", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = DomainPublicAdapterWebApiModelsV1ListingsBusinessPriceSearch.from_dict(_price)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort(_sort)

        _search_mode = d.pop("searchMode", UNSET)
        search_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode]
        if isinstance(_search_mode, Unset):
            search_mode = UNSET
        else:
            search_mode = DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode(_search_mode)

        domain_public_adapter_web_api_models_v1_listings_business_search_request = cls(
            page_number=page_number,
            advertiser_id=advertiser_id,
            property_types=property_types,
            keywords=keywords,
            brand_id=brand_id,
            franchise_group_id=franchise_group_id,
            locations=locations,
            page_size=page_size,
            price=price,
            sort=sort,
            search_mode=search_mode,
        )

        domain_public_adapter_web_api_models_v1_listings_business_search_request.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_business_search_request

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
