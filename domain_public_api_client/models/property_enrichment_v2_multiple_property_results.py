from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_multiple_property_results_properties_item import (
        PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem,
    )


T = TypeVar("T", bound="PropertyEnrichmentV2MultiplePropertyResults")


@_attrs_define
class PropertyEnrichmentV2MultiplePropertyResults:
    """
    Attributes:
        properties (Union[Unset, List['PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem']]):
    """

    properties: Union[Unset, List["PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_multiple_property_results_properties_item import (
            PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem,
        )

        d = src_dict.copy()
        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = PropertyEnrichmentV2MultiplePropertyResultsPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        property_enrichment_v2_multiple_property_results = cls(
            properties=properties,
        )

        property_enrichment_v2_multiple_property_results.additional_properties = d
        return property_enrichment_v2_multiple_property_results

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
