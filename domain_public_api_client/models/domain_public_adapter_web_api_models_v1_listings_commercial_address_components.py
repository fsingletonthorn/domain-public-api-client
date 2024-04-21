from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents:
    """Address components

    Attributes:
        area (Union[Unset, str]): Listing Area
        district (Union[Unset, str]): Not used
        postcode (Union[Unset, str]): Postcode
        region (Union[Unset, str]): Listing Region
        state_short (Union[Unset, str]): AUS State. 2 or 3 characters
        street (Union[Unset, str]): Street address
        street_number (Union[Unset, str]): Street number
        suburb (Union[Unset, str]): Suburb
        unit_number (Union[Unset, str]): Unit number
    """

    area: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    state_short: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    unit_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        area = self.area

        district = self.district

        postcode = self.postcode

        region = self.region

        state_short = self.state_short

        street = self.street

        street_number = self.street_number

        suburb = self.suburb

        unit_number = self.unit_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if district is not UNSET:
            field_dict["district"] = district
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if region is not UNSET:
            field_dict["region"] = region
        if state_short is not UNSET:
            field_dict["stateShort"] = state_short
        if street is not UNSET:
            field_dict["street"] = street
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        area = d.pop("area", UNSET)

        district = d.pop("district", UNSET)

        postcode = d.pop("postcode", UNSET)

        region = d.pop("region", UNSET)

        state_short = d.pop("stateShort", UNSET)

        street = d.pop("street", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        suburb = d.pop("suburb", UNSET)

        unit_number = d.pop("unitNumber", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_address_components = cls(
            area=area,
            district=district,
            postcode=postcode,
            region=region,
            state_short=state_short,
            street=street,
            street_number=street_number,
            suburb=suburb,
            unit_number=unit_number,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_address_components.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_address_components

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
