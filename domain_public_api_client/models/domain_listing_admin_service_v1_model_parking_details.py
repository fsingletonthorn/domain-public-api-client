from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_parking_details_parking_type import (
    DomainListingAdminServiceV1ModelParkingDetailsParkingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelParkingDetails")


@_attrs_define
class DomainListingAdminServiceV1ModelParkingDetails:
    r"""Parking Details

    Attributes:
        parking_type (Union[Unset, DomainListingAdminServiceV1ModelParkingDetailsParkingType]): Can have the value
            \"OnSite\", \"OnStreet\", \"NoParking\". Default: \"NoParking\"
        number_of_spaces (Union[Unset, int]): Number of parking spaces on site
    """

    parking_type: Union[Unset, DomainListingAdminServiceV1ModelParkingDetailsParkingType] = UNSET
    number_of_spaces: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parking_type: Union[Unset, str] = UNSET
        if not isinstance(self.parking_type, Unset):
            parking_type = self.parking_type.value

        number_of_spaces = self.number_of_spaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parking_type is not UNSET:
            field_dict["parkingType"] = parking_type
        if number_of_spaces is not UNSET:
            field_dict["numberOfSpaces"] = number_of_spaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _parking_type = d.pop("parkingType", UNSET)
        parking_type: Union[Unset, DomainListingAdminServiceV1ModelParkingDetailsParkingType]
        if isinstance(_parking_type, Unset):
            parking_type = UNSET
        else:
            parking_type = DomainListingAdminServiceV1ModelParkingDetailsParkingType(_parking_type)

        number_of_spaces = d.pop("numberOfSpaces", UNSET)

        domain_listing_admin_service_v1_model_parking_details = cls(
            parking_type=parking_type,
            number_of_spaces=number_of_spaces,
        )

        domain_listing_admin_service_v1_model_parking_details.additional_properties = d
        return domain_listing_admin_service_v1_model_parking_details

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
