from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_parking_parking_type import ListingAdminV2ParkingParkingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Parking")


@_attrs_define
class ListingAdminV2Parking:
    """Parking Details

    Attributes:
        parking_type (Union[Unset, ListingAdminV2ParkingParkingType]): Can have the value "OnSite", "OnStreet",
            "NoParking". Default "NoParking"
        number_on_site (Union[Unset, int]): Number On Site
        information (Union[Unset, str]): Additional information regarding the parking condition
    """

    parking_type: Union[Unset, ListingAdminV2ParkingParkingType] = UNSET
    number_on_site: Union[Unset, int] = UNSET
    information: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parking_type: Union[Unset, str] = UNSET
        if not isinstance(self.parking_type, Unset):
            parking_type = self.parking_type.value

        number_on_site = self.number_on_site

        information = self.information

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parking_type is not UNSET:
            field_dict["parkingType"] = parking_type
        if number_on_site is not UNSET:
            field_dict["numberOnSite"] = number_on_site
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _parking_type = d.pop("parkingType", UNSET)
        parking_type: Union[Unset, ListingAdminV2ParkingParkingType]
        if isinstance(_parking_type, Unset):
            parking_type = UNSET
        else:
            parking_type = ListingAdminV2ParkingParkingType(_parking_type)

        number_on_site = d.pop("numberOnSite", UNSET)

        information = d.pop("information", UNSET)

        listing_admin_v2_parking = cls(
            parking_type=parking_type,
            number_on_site=number_on_site,
            information=information,
        )

        listing_admin_v2_parking.additional_properties = d
        return listing_admin_v2_parking

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
