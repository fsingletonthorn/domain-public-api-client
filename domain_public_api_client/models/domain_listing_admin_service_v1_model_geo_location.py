from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelGeoLocation")


@_attrs_define
class DomainListingAdminServiceV1ModelGeoLocation:
    """Contains geocoding of an address

    Attributes:
        latitude (Union[Unset, float]): Latitude
        longitude (Union[Unset, float]): Longitude
    """

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        domain_listing_admin_service_v1_model_geo_location = cls(
            latitude=latitude,
            longitude=longitude,
        )

        domain_listing_admin_service_v1_model_geo_location.additional_properties = d
        return domain_listing_admin_service_v1_model_geo_location

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
