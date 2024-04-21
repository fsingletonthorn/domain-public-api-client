from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_parking_details import (
        DomainListingAdminServiceV1ModelParkingDetails,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelParkingInfo")


@_attrs_define
class DomainListingAdminServiceV1ModelParkingInfo:
    """Parking Details

    Attributes:
        details (Union[Unset, List['DomainListingAdminServiceV1ModelParkingDetails']]): Details for available parking
            spaces
        information (Union[Unset, str]): Additional information regarding the parking condition
    """

    details: Union[Unset, List["DomainListingAdminServiceV1ModelParkingDetails"]] = UNSET
    information: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        information = self.information

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_parking_details import (
            DomainListingAdminServiceV1ModelParkingDetails,
        )

        d = src_dict.copy()
        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = DomainListingAdminServiceV1ModelParkingDetails.from_dict(details_item_data)

            details.append(details_item)

        information = d.pop("information", UNSET)

        domain_listing_admin_service_v1_model_parking_info = cls(
            details=details,
            information=information,
        )

        domain_listing_admin_service_v1_model_parking_info.additional_properties = d
        return domain_listing_admin_service_v1_model_parking_info

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
