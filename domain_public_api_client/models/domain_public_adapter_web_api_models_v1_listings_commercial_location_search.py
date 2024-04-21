from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_location_search_state import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearchState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch:
    """Search request location details

    Attributes:
        area (Union[Unset, str]): Location area
        postcode (Union[Unset, str]): Location postcode
        region (Union[Unset, str]): Location region
        state (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearchState]): State
        street (Union[Unset, str]): Street address
        suburb (Union[Unset, str]): Suburb
    """

    area: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    state: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearchState] = UNSET
    street: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        area = self.area

        postcode = self.postcode

        region = self.region

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        street = self.street

        suburb = self.suburb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if region is not UNSET:
            field_dict["region"] = region
        if state is not UNSET:
            field_dict["state"] = state
        if street is not UNSET:
            field_dict["street"] = street
        if suburb is not UNSET:
            field_dict["suburb"] = suburb

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        area = d.pop("area", UNSET)

        postcode = d.pop("postcode", UNSET)

        region = d.pop("region", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearchState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearchState(_state)

        street = d.pop("street", UNSET)

        suburb = d.pop("suburb", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_location_search = cls(
            area=area,
            postcode=postcode,
            region=region,
            state=state,
            street=street,
            suburb=suburb,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_location_search.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_location_search

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
