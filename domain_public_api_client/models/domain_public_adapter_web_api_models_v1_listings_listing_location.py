from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsListingLocation")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsListingLocation:
    """Listing location

    Attributes:
        name (Union[Unset, str]): Name
        state (Union[Unset, str]): State
        postcode (Union[Unset, str]): Postcode
        area (Union[Unset, str]): Area
        region (Union[Unset, str]): Region
        type (Union[Unset, str]): Type
    """

    name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        state = self.state

        postcode = self.postcode

        area = self.area

        region = self.region

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if area is not UNSET:
            field_dict["area"] = area
        if region is not UNSET:
            field_dict["region"] = region
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        postcode = d.pop("postcode", UNSET)

        area = d.pop("area", UNSET)

        region = d.pop("region", UNSET)

        type = d.pop("type", UNSET)

        domain_public_adapter_web_api_models_v1_listings_listing_location = cls(
            name=name,
            state=state,
            postcode=postcode,
            area=area,
            region=region,
            type=type,
        )

        domain_public_adapter_web_api_models_v1_listings_listing_location.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_listing_location

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
