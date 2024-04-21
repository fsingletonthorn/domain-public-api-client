from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic


T = TypeVar("T", bound="PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem")


@_attrs_define
class PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem:
    """
    Attributes:
        property_id (Union[Unset, str]):
        address_components (Union[Unset, PropertyEnrichmentV2AddressBasic]): Address of property
    """

    property_id: Union[Unset, str] = UNSET
    address_components: Union[Unset, "PropertyEnrichmentV2AddressBasic"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_id = self.property_id

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic

        d = src_dict.copy()
        property_id = d.pop("propertyId", UNSET)

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, PropertyEnrichmentV2AddressBasic]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = PropertyEnrichmentV2AddressBasic.from_dict(_address_components)

        property_enrichment_v2_multiple_property_results_properties_item = cls(
            property_id=property_id,
            address_components=address_components,
        )

        property_enrichment_v2_multiple_property_results_properties_item.additional_properties = d
        return property_enrichment_v2_multiple_property_results_properties_item

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
