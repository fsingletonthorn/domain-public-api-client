from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details_all_property_types_item import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsAllPropertyTypesItem,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details_features_item import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsFeaturesItem,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details_property_type import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsPropertyType,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_details_state import (
    DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetails:
    """
    Attributes:
        state (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState]):
        features (Union[Unset, List[DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsFeaturesItem]]):
        property_type (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsPropertyType]):
        all_property_types (Union[Unset,
            List[DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsAllPropertyTypesItem]]):
        bathrooms (Union[Unset, float]):
        bedrooms (Union[Unset, float]):
        carspaces (Union[Unset, int]):
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street (Union[Unset, str]):
        area (Union[Unset, str]):
        region (Union[Unset, str]):
        suburb (Union[Unset, str]):
        suburb_id (Union[Unset, int]):
        postcode (Union[Unset, str]):
        displayable_address (Union[Unset, str]):
        latitude (Union[Unset, float]):
        longitude (Union[Unset, float]):
        map_certainty (Union[Unset, int]):
        land_area (Union[Unset, float]):
        building_area (Union[Unset, float]):
        only_show_properties (Union[Unset, List[str]]):
        display_address_type (Union[Unset, str]):
        is_rural (Union[Unset, bool]):
        top_spot_keywords (Union[Unset, List[str]]):
        is_new (Union[Unset, bool]):
        tags (Union[Unset, List[str]]):
    """

    state: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState] = UNSET
    features: Union[Unset, List[DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsFeaturesItem]] = UNSET
    property_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsPropertyType] = UNSET
    all_property_types: Union[
        Unset, List[DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsAllPropertyTypesItem]
    ] = UNSET
    bathrooms: Union[Unset, float] = UNSET
    bedrooms: Union[Unset, float] = UNSET
    carspaces: Union[Unset, int] = UNSET
    unit_number: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    suburb_id: Union[Unset, int] = UNSET
    postcode: Union[Unset, str] = UNSET
    displayable_address: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    map_certainty: Union[Unset, int] = UNSET
    land_area: Union[Unset, float] = UNSET
    building_area: Union[Unset, float] = UNSET
    only_show_properties: Union[Unset, List[str]] = UNSET
    display_address_type: Union[Unset, str] = UNSET
    is_rural: Union[Unset, bool] = UNSET
    top_spot_keywords: Union[Unset, List[str]] = UNSET
    is_new: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value
                features.append(features_item)

        property_type: Union[Unset, str] = UNSET
        if not isinstance(self.property_type, Unset):
            property_type = self.property_type.value

        all_property_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.all_property_types, Unset):
            all_property_types = []
            for all_property_types_item_data in self.all_property_types:
                all_property_types_item = all_property_types_item_data.value
                all_property_types.append(all_property_types_item)

        bathrooms = self.bathrooms

        bedrooms = self.bedrooms

        carspaces = self.carspaces

        unit_number = self.unit_number

        street_number = self.street_number

        street = self.street

        area = self.area

        region = self.region

        suburb = self.suburb

        suburb_id = self.suburb_id

        postcode = self.postcode

        displayable_address = self.displayable_address

        latitude = self.latitude

        longitude = self.longitude

        map_certainty = self.map_certainty

        land_area = self.land_area

        building_area = self.building_area

        only_show_properties: Union[Unset, List[str]] = UNSET
        if not isinstance(self.only_show_properties, Unset):
            only_show_properties = self.only_show_properties

        display_address_type = self.display_address_type

        is_rural = self.is_rural

        top_spot_keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.top_spot_keywords, Unset):
            top_spot_keywords = self.top_spot_keywords

        is_new = self.is_new

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if features is not UNSET:
            field_dict["features"] = features
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if all_property_types is not UNSET:
            field_dict["allPropertyTypes"] = all_property_types
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if carspaces is not UNSET:
            field_dict["carspaces"] = carspaces
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street is not UNSET:
            field_dict["street"] = street
        if area is not UNSET:
            field_dict["area"] = area
        if region is not UNSET:
            field_dict["region"] = region
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if displayable_address is not UNSET:
            field_dict["displayableAddress"] = displayable_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if map_certainty is not UNSET:
            field_dict["mapCertainty"] = map_certainty
        if land_area is not UNSET:
            field_dict["landArea"] = land_area
        if building_area is not UNSET:
            field_dict["buildingArea"] = building_area
        if only_show_properties is not UNSET:
            field_dict["onlyShowProperties"] = only_show_properties
        if display_address_type is not UNSET:
            field_dict["displayAddressType"] = display_address_type
        if is_rural is not UNSET:
            field_dict["isRural"] = is_rural
        if top_spot_keywords is not UNSET:
            field_dict["topSpotKeywords"] = top_spot_keywords
        if is_new is not UNSET:
            field_dict["isNew"] = is_new
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState(_state)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in _features or []:
            features_item = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsFeaturesItem(
                features_item_data
            )

            features.append(features_item)

        _property_type = d.pop("propertyType", UNSET)
        property_type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsPropertyType]
        if isinstance(_property_type, Unset):
            property_type = UNSET
        else:
            property_type = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsPropertyType(_property_type)

        all_property_types = []
        _all_property_types = d.pop("allPropertyTypes", UNSET)
        for all_property_types_item_data in _all_property_types or []:
            all_property_types_item = (
                DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsAllPropertyTypesItem(
                    all_property_types_item_data
                )
            )

            all_property_types.append(all_property_types_item)

        bathrooms = d.pop("bathrooms", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        carspaces = d.pop("carspaces", UNSET)

        unit_number = d.pop("unitNumber", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        street = d.pop("street", UNSET)

        area = d.pop("area", UNSET)

        region = d.pop("region", UNSET)

        suburb = d.pop("suburb", UNSET)

        suburb_id = d.pop("suburbId", UNSET)

        postcode = d.pop("postcode", UNSET)

        displayable_address = d.pop("displayableAddress", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        map_certainty = d.pop("mapCertainty", UNSET)

        land_area = d.pop("landArea", UNSET)

        building_area = d.pop("buildingArea", UNSET)

        only_show_properties = cast(List[str], d.pop("onlyShowProperties", UNSET))

        display_address_type = d.pop("displayAddressType", UNSET)

        is_rural = d.pop("isRural", UNSET)

        top_spot_keywords = cast(List[str], d.pop("topSpotKeywords", UNSET))

        is_new = d.pop("isNew", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        domain_search_service_v2_model_domain_search_contracts_v2_property_details = cls(
            state=state,
            features=features,
            property_type=property_type,
            all_property_types=all_property_types,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            carspaces=carspaces,
            unit_number=unit_number,
            street_number=street_number,
            street=street,
            area=area,
            region=region,
            suburb=suburb,
            suburb_id=suburb_id,
            postcode=postcode,
            displayable_address=displayable_address,
            latitude=latitude,
            longitude=longitude,
            map_certainty=map_certainty,
            land_area=land_area,
            building_area=building_area,
            only_show_properties=only_show_properties,
            display_address_type=display_address_type,
            is_rural=is_rural,
            top_spot_keywords=top_spot_keywords,
            is_new=is_new,
            tags=tags,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_property_details.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_property_details

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
