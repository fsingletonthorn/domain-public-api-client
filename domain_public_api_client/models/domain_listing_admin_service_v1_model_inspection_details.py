from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_inspection import DomainListingAdminServiceV1ModelInspection


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelInspectionDetails")


@_attrs_define
class DomainListingAdminServiceV1ModelInspectionDetails:
    """Inspection details

    Attributes:
        inspection_description (Union[Unset, str]): Free text field for inspections
        inspections (Union[Unset, List['DomainListingAdminServiceV1ModelInspection']]): Inspection times of the listing
    """

    inspection_description: Union[Unset, str] = UNSET
    inspections: Union[Unset, List["DomainListingAdminServiceV1ModelInspection"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inspection_description = self.inspection_description

        inspections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inspections, Unset):
            inspections = []
            for inspections_item_data in self.inspections:
                inspections_item = inspections_item_data.to_dict()
                inspections.append(inspections_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inspection_description is not UNSET:
            field_dict["inspectionDescription"] = inspection_description
        if inspections is not UNSET:
            field_dict["inspections"] = inspections

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_inspection import DomainListingAdminServiceV1ModelInspection

        d = src_dict.copy()
        inspection_description = d.pop("inspectionDescription", UNSET)

        inspections = []
        _inspections = d.pop("inspections", UNSET)
        for inspections_item_data in _inspections or []:
            inspections_item = DomainListingAdminServiceV1ModelInspection.from_dict(inspections_item_data)

            inspections.append(inspections_item)

        domain_listing_admin_service_v1_model_inspection_details = cls(
            inspection_description=inspection_description,
            inspections=inspections,
        )

        domain_listing_admin_service_v1_model_inspection_details.additional_properties = d
        return domain_listing_admin_service_v1_model_inspection_details

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
