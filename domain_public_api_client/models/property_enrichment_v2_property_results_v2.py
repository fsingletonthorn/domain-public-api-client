from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
    from ..models.property_enrichment_v2_property_activity_summary_v2 import (
        PropertyEnrichmentV2PropertyActivitySummaryV2,
    )
    from ..models.property_enrichment_v2_property_summary import PropertyEnrichmentV2PropertySummary


T = TypeVar("T", bound="PropertyEnrichmentV2PropertyResultsV2")


@_attrs_define
class PropertyEnrichmentV2PropertyResultsV2:
    """
    Attributes:
        property_id (Union[Unset, str]): Unique ID for the property
        address_components (Union[Unset, PropertyEnrichmentV2AddressBasic]): Address of property
        property_summary (Union[Unset, PropertyEnrichmentV2PropertySummary]): Property summary
        activity_summary (Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2]): Property activity summary
            derived from property activity events (not currently in EVENT-SCHEMAS project)
    """

    property_id: Union[Unset, str] = UNSET
    address_components: Union[Unset, "PropertyEnrichmentV2AddressBasic"] = UNSET
    property_summary: Union[Unset, "PropertyEnrichmentV2PropertySummary"] = UNSET
    activity_summary: Union[Unset, "PropertyEnrichmentV2PropertyActivitySummaryV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_id = self.property_id

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        property_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_summary, Unset):
            property_summary = self.property_summary.to_dict()

        activity_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity_summary, Unset):
            activity_summary = self.activity_summary.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if property_summary is not UNSET:
            field_dict["propertySummary"] = property_summary
        if activity_summary is not UNSET:
            field_dict["activitySummary"] = activity_summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
        from ..models.property_enrichment_v2_property_activity_summary_v2 import (
            PropertyEnrichmentV2PropertyActivitySummaryV2,
        )
        from ..models.property_enrichment_v2_property_summary import PropertyEnrichmentV2PropertySummary

        d = src_dict.copy()
        property_id = d.pop("propertyId", UNSET)

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, PropertyEnrichmentV2AddressBasic]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = PropertyEnrichmentV2AddressBasic.from_dict(_address_components)

        _property_summary = d.pop("propertySummary", UNSET)
        property_summary: Union[Unset, PropertyEnrichmentV2PropertySummary]
        if isinstance(_property_summary, Unset):
            property_summary = UNSET
        else:
            property_summary = PropertyEnrichmentV2PropertySummary.from_dict(_property_summary)

        _activity_summary = d.pop("activitySummary", UNSET)
        activity_summary: Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2]
        if isinstance(_activity_summary, Unset):
            activity_summary = UNSET
        else:
            activity_summary = PropertyEnrichmentV2PropertyActivitySummaryV2.from_dict(_activity_summary)

        property_enrichment_v2_property_results_v2 = cls(
            property_id=property_id,
            address_components=address_components,
            property_summary=property_summary,
            activity_summary=activity_summary,
        )

        property_enrichment_v2_property_results_v2.additional_properties = d
        return property_enrichment_v2_property_results_v2

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
