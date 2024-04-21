from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_parking_details_parking_type import ListingAdminV2ParkingDetailsParkingType

T = TypeVar("T", bound="ListingAdminV2ParkingDetails")


@_attrs_define
class ListingAdminV2ParkingDetails:
    """Parking Details

    Attributes:
        parking_type (ListingAdminV2ParkingDetailsParkingType): Can have the value "OnSite", "OnStreet", "NoParking".
            Default: "NoParking"
        number_of_spaces (int): Number of parking spaces on site
    """

    parking_type: ListingAdminV2ParkingDetailsParkingType
    number_of_spaces: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parking_type = self.parking_type.value

        number_of_spaces = self.number_of_spaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parkingType": parking_type,
                "numberOfSpaces": number_of_spaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parking_type = ListingAdminV2ParkingDetailsParkingType(d.pop("parkingType"))

        number_of_spaces = d.pop("numberOfSpaces")

        listing_admin_v2_parking_details = cls(
            parking_type=parking_type,
            number_of_spaces=number_of_spaces,
        )

        listing_admin_v2_parking_details.additional_properties = d
        return listing_admin_v2_parking_details

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
