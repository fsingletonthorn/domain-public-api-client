from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_exclusion_types_item import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestExclusionTypesItem,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_property_title import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_property_types_item import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTypesItem,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_sale_type import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_search_mode import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request_sort import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_window import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_location_search import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_parking_search import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_price_search import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest:
    """Listing search criteria

    Attributes:
        page_number (Union[Unset, int]):
        advertiser_id (Union[Unset, int]): Agency ID
        page_size (Union[Unset, int]): Search results page size
        property_types (Union[Unset,
            List[DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTypesItem]]): Listing property
            types
        price (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch]): Search criteria. Price
        locations (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch']]): Location
            search criteria
        keywords (Union[Unset, List[str]]): Search listings by keyword
        geo_window (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow]): Polygon which specifies
            geographical area for listing search
        land_area_min (Union[Unset, int]): Minimum land area
        land_area_max (Union[Unset, int]): Maximum land area
        building_size_min (Union[Unset, int]): Minimum building area
        building_size_max (Union[Unset, int]): Maximum building area
        search_mode (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode]): Search
            mode
        occupancy (Union[Unset, str]): Occupancy
        sort (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort]): Sorting order
        sale_type (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType]): Sale type
        property_title (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle]):
            Property title
        parking (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch]): Listing search.
            Parking search criteria
        exclusion_types (Union[Unset,
            List[DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestExclusionTypesItem]]): Exclusion Types
        annual_return (Union[Unset, int]): Minimum annual return (in percents)
    """

    page_number: Union[Unset, int] = UNSET
    advertiser_id: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    property_types: Union[
        Unset, List[DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTypesItem]
    ] = UNSET
    price: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch"] = UNSET
    locations: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch"]] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    geo_window: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow"] = UNSET
    land_area_min: Union[Unset, int] = UNSET
    land_area_max: Union[Unset, int] = UNSET
    building_size_min: Union[Unset, int] = UNSET
    building_size_max: Union[Unset, int] = UNSET
    search_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode] = UNSET
    occupancy: Union[Unset, str] = UNSET
    sort: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort] = UNSET
    sale_type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType] = UNSET
    property_title: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle] = UNSET
    parking: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch"] = UNSET
    exclusion_types: Union[
        Unset, List[DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestExclusionTypesItem]
    ] = UNSET
    annual_return: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_number = self.page_number

        advertiser_id = self.advertiser_id

        page_size = self.page_size

        property_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_types, Unset):
            property_types = []
            for property_types_item_data in self.property_types:
                property_types_item = property_types_item_data.value
                property_types.append(property_types_item)

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        geo_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_window, Unset):
            geo_window = self.geo_window.to_dict()

        land_area_min = self.land_area_min

        land_area_max = self.land_area_max

        building_size_min = self.building_size_min

        building_size_max = self.building_size_max

        search_mode: Union[Unset, str] = UNSET
        if not isinstance(self.search_mode, Unset):
            search_mode = self.search_mode.value

        occupancy = self.occupancy

        sort: Union[Unset, str] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        sale_type: Union[Unset, str] = UNSET
        if not isinstance(self.sale_type, Unset):
            sale_type = self.sale_type.value

        property_title: Union[Unset, str] = UNSET
        if not isinstance(self.property_title, Unset):
            property_title = self.property_title.value

        parking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parking, Unset):
            parking = self.parking.to_dict()

        exclusion_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclusion_types, Unset):
            exclusion_types = []
            for exclusion_types_item_data in self.exclusion_types:
                exclusion_types_item = exclusion_types_item_data.value
                exclusion_types.append(exclusion_types_item)

        annual_return = self.annual_return

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if advertiser_id is not UNSET:
            field_dict["advertiserId"] = advertiser_id
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if price is not UNSET:
            field_dict["price"] = price
        if locations is not UNSET:
            field_dict["locations"] = locations
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if geo_window is not UNSET:
            field_dict["geoWindow"] = geo_window
        if land_area_min is not UNSET:
            field_dict["landAreaMin"] = land_area_min
        if land_area_max is not UNSET:
            field_dict["landAreaMax"] = land_area_max
        if building_size_min is not UNSET:
            field_dict["buildingSizeMin"] = building_size_min
        if building_size_max is not UNSET:
            field_dict["buildingSizeMax"] = building_size_max
        if search_mode is not UNSET:
            field_dict["searchMode"] = search_mode
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if sort is not UNSET:
            field_dict["sort"] = sort
        if sale_type is not UNSET:
            field_dict["saleType"] = sale_type
        if property_title is not UNSET:
            field_dict["propertyTitle"] = property_title
        if parking is not UNSET:
            field_dict["parking"] = parking
        if exclusion_types is not UNSET:
            field_dict["exclusionTypes"] = exclusion_types
        if annual_return is not UNSET:
            field_dict["annualReturn"] = annual_return

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_window import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_location_search import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_parking_search import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_price_search import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch,
        )

        d = src_dict.copy()
        page_number = d.pop("pageNumber", UNSET)

        advertiser_id = d.pop("advertiserId", UNSET)

        page_size = d.pop("pageSize", UNSET)

        property_types = []
        _property_types = d.pop("propertyTypes", UNSET)
        for property_types_item_data in _property_types or []:
            property_types_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTypesItem(
                property_types_item_data
            )

            property_types.append(property_types_item)

        _price = d.pop("price", UNSET)
        price: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch.from_dict(_price)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        _geo_window = d.pop("geoWindow", UNSET)
        geo_window: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow]
        if isinstance(_geo_window, Unset):
            geo_window = UNSET
        else:
            geo_window = DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow.from_dict(_geo_window)

        land_area_min = d.pop("landAreaMin", UNSET)

        land_area_max = d.pop("landAreaMax", UNSET)

        building_size_min = d.pop("buildingSizeMin", UNSET)

        building_size_max = d.pop("buildingSizeMax", UNSET)

        _search_mode = d.pop("searchMode", UNSET)
        search_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode]
        if isinstance(_search_mode, Unset):
            search_mode = UNSET
        else:
            search_mode = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode(_search_mode)

        occupancy = d.pop("occupancy", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort(_sort)

        _sale_type = d.pop("saleType", UNSET)
        sale_type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType]
        if isinstance(_sale_type, Unset):
            sale_type = UNSET
        else:
            sale_type = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType(_sale_type)

        _property_title = d.pop("propertyTitle", UNSET)
        property_title: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle]
        if isinstance(_property_title, Unset):
            property_title = UNSET
        else:
            property_title = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle(
                _property_title
            )

        _parking = d.pop("parking", UNSET)
        parking: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch]
        if isinstance(_parking, Unset):
            parking = UNSET
        else:
            parking = DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch.from_dict(_parking)

        exclusion_types = []
        _exclusion_types = d.pop("exclusionTypes", UNSET)
        for exclusion_types_item_data in _exclusion_types or []:
            exclusion_types_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestExclusionTypesItem(
                exclusion_types_item_data
            )

            exclusion_types.append(exclusion_types_item)

        annual_return = d.pop("annualReturn", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_search_request = cls(
            page_number=page_number,
            advertiser_id=advertiser_id,
            page_size=page_size,
            property_types=property_types,
            price=price,
            locations=locations,
            keywords=keywords,
            geo_window=geo_window,
            land_area_min=land_area_min,
            land_area_max=land_area_max,
            building_size_min=building_size_min,
            building_size_max=building_size_max,
            search_mode=search_mode,
            occupancy=occupancy,
            sort=sort,
            sale_type=sale_type,
            property_title=property_title,
            parking=parking,
            exclusion_types=exclusion_types,
            annual_return=annual_return,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_search_request.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_search_request

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
