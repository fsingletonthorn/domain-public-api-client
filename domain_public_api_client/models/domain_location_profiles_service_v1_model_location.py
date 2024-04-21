from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_location_profiles_service_v1_model_location_data import (
        DomainLocationProfilesServiceV1ModelLocationData,
    )
    from ..models.domain_location_profiles_service_v1_model_location_surrounding_suburbs import (
        DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs,
    )


T = TypeVar("T", bound="DomainLocationProfilesServiceV1ModelLocation")


@_attrs_define
class DomainLocationProfilesServiceV1ModelLocation:
    """
    Attributes:
        domain_location_id (Union[Unset, int]):
        postcode (Union[Unset, str]):
        pf_location_id (Union[Unset, str]):
        surrounding_suburbs (Union[Unset, List['DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs']]):
        url_slug (Union[Unset, str]):
        suburb_name (Union[Unset, str]):
        data (Union[Unset, DomainLocationProfilesServiceV1ModelLocationData]):
        apm_location_id (Union[Unset, int]):
        location_id (Union[Unset, int]):
        area_name (Union[Unset, str]):
        region_name (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    domain_location_id: Union[Unset, int] = UNSET
    postcode: Union[Unset, str] = UNSET
    pf_location_id: Union[Unset, str] = UNSET
    surrounding_suburbs: Union[Unset, List["DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs"]] = UNSET
    url_slug: Union[Unset, str] = UNSET
    suburb_name: Union[Unset, str] = UNSET
    data: Union[Unset, "DomainLocationProfilesServiceV1ModelLocationData"] = UNSET
    apm_location_id: Union[Unset, int] = UNSET
    location_id: Union[Unset, int] = UNSET
    area_name: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_location_id = self.domain_location_id

        postcode = self.postcode

        pf_location_id = self.pf_location_id

        surrounding_suburbs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.surrounding_suburbs, Unset):
            surrounding_suburbs = []
            for surrounding_suburbs_item_data in self.surrounding_suburbs:
                surrounding_suburbs_item = surrounding_suburbs_item_data.to_dict()
                surrounding_suburbs.append(surrounding_suburbs_item)

        url_slug = self.url_slug

        suburb_name = self.suburb_name

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        apm_location_id = self.apm_location_id

        location_id = self.location_id

        area_name = self.area_name

        region_name = self.region_name

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_location_id is not UNSET:
            field_dict["domainLocationId"] = domain_location_id
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if pf_location_id is not UNSET:
            field_dict["pfLocationId"] = pf_location_id
        if surrounding_suburbs is not UNSET:
            field_dict["surroundingSuburbs"] = surrounding_suburbs
        if url_slug is not UNSET:
            field_dict["urlSlug"] = url_slug
        if suburb_name is not UNSET:
            field_dict["suburbName"] = suburb_name
        if data is not UNSET:
            field_dict["data"] = data
        if apm_location_id is not UNSET:
            field_dict["apmLocationId"] = apm_location_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if area_name is not UNSET:
            field_dict["areaName"] = area_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_location_profiles_service_v1_model_location_data import (
            DomainLocationProfilesServiceV1ModelLocationData,
        )
        from ..models.domain_location_profiles_service_v1_model_location_surrounding_suburbs import (
            DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs,
        )

        d = src_dict.copy()
        domain_location_id = d.pop("domainLocationId", UNSET)

        postcode = d.pop("postcode", UNSET)

        pf_location_id = d.pop("pfLocationId", UNSET)

        surrounding_suburbs = []
        _surrounding_suburbs = d.pop("surroundingSuburbs", UNSET)
        for surrounding_suburbs_item_data in _surrounding_suburbs or []:
            surrounding_suburbs_item = DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs.from_dict(
                surrounding_suburbs_item_data
            )

            surrounding_suburbs.append(surrounding_suburbs_item)

        url_slug = d.pop("urlSlug", UNSET)

        suburb_name = d.pop("suburbName", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, DomainLocationProfilesServiceV1ModelLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DomainLocationProfilesServiceV1ModelLocationData.from_dict(_data)

        apm_location_id = d.pop("apmLocationId", UNSET)

        location_id = d.pop("locationId", UNSET)

        area_name = d.pop("areaName", UNSET)

        region_name = d.pop("regionName", UNSET)

        state = d.pop("state", UNSET)

        domain_location_profiles_service_v1_model_location = cls(
            domain_location_id=domain_location_id,
            postcode=postcode,
            pf_location_id=pf_location_id,
            surrounding_suburbs=surrounding_suburbs,
            url_slug=url_slug,
            suburb_name=suburb_name,
            data=data,
            apm_location_id=apm_location_id,
            location_id=location_id,
            area_name=area_name,
            region_name=region_name,
            state=state,
        )

        domain_location_profiles_service_v1_model_location.additional_properties = d
        return domain_location_profiles_service_v1_model_location

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
