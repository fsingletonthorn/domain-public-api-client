from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_inspection import ListingAdminV2Inspection


T = TypeVar("T", bound="ListingAdminV2InspectionDetails")


@_attrs_define
class ListingAdminV2InspectionDetails:
    """Inspection details

    Attributes:
        inspection_description (Union[Unset, str]): Free text field for inspections
        inspections (Union[Unset, List['ListingAdminV2Inspection']]): Inspection times of the listing
    """

    inspection_description: Union[Unset, str] = UNSET
    inspections: Union[Unset, List["ListingAdminV2Inspection"]] = UNSET
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
        from ..models.listing_admin_v2_inspection import ListingAdminV2Inspection

        d = src_dict.copy()
        inspection_description = d.pop("inspectionDescription", UNSET)

        inspections = []
        _inspections = d.pop("inspections", UNSET)
        for inspections_item_data in _inspections or []:
            inspections_item = ListingAdminV2Inspection.from_dict(inspections_item_data)

            inspections.append(inspections_item)

        listing_admin_v2_inspection_details = cls(
            inspection_description=inspection_description,
            inspections=inspections,
        )

        listing_admin_v2_inspection_details.additional_properties = d
        return listing_admin_v2_inspection_details

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
