from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_location_state import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocationState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocation:
    """
    Attributes:
        state (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocationState]):
        region (Union[Unset, str]):
        area (Union[Unset, str]):
        suburb (Union[Unset, str]):
        post_code (Union[Unset, str]):
        include_surrounding_suburbs (Union[Unset, bool]):
        surrounding_radius_in_meters (Union[Unset, int]):
    """

    state: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocationState] = UNSET
    region: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    include_surrounding_suburbs: Union[Unset, bool] = UNSET
    surrounding_radius_in_meters: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        region = self.region

        area = self.area

        suburb = self.suburb

        post_code = self.post_code

        include_surrounding_suburbs = self.include_surrounding_suburbs

        surrounding_radius_in_meters = self.surrounding_radius_in_meters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if region is not UNSET:
            field_dict["region"] = region
        if area is not UNSET:
            field_dict["area"] = area
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if include_surrounding_suburbs is not UNSET:
            field_dict["includeSurroundingSuburbs"] = include_surrounding_suburbs
        if surrounding_radius_in_meters is not UNSET:
            field_dict["surroundingRadiusInMeters"] = surrounding_radius_in_meters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocationState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchLocationState(_state)

        region = d.pop("region", UNSET)

        area = d.pop("area", UNSET)

        suburb = d.pop("suburb", UNSET)

        post_code = d.pop("postCode", UNSET)

        include_surrounding_suburbs = d.pop("includeSurroundingSuburbs", UNSET)

        surrounding_radius_in_meters = d.pop("surroundingRadiusInMeters", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_search_location = cls(
            state=state,
            region=region,
            area=area,
            suburb=suburb,
            post_code=post_code,
            include_surrounding_suburbs=include_surrounding_suburbs,
            surrounding_radius_in_meters=surrounding_radius_in_meters,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_search_location.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_search_location

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
