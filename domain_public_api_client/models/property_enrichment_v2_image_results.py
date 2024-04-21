from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
    from ..models.property_enrichment_v2_image_url import PropertyEnrichmentV2ImageUrl


T = TypeVar("T", bound="PropertyEnrichmentV2ImageResults")


@_attrs_define
class PropertyEnrichmentV2ImageResults:
    """
    Attributes:
        property_id (Union[Unset, str]): Unique ID for the property
        address_components (Union[Unset, PropertyEnrichmentV2AddressBasic]): Address of property
        images (Union[Unset, List['PropertyEnrichmentV2ImageUrl']]):
    """

    property_id: Union[Unset, str] = UNSET
    address_components: Union[Unset, "PropertyEnrichmentV2AddressBasic"] = UNSET
    images: Union[Unset, List["PropertyEnrichmentV2ImageUrl"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_id = self.property_id

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
        from ..models.property_enrichment_v2_image_url import PropertyEnrichmentV2ImageUrl

        d = src_dict.copy()
        property_id = d.pop("propertyId", UNSET)

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, PropertyEnrichmentV2AddressBasic]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = PropertyEnrichmentV2AddressBasic.from_dict(_address_components)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = PropertyEnrichmentV2ImageUrl.from_dict(images_item_data)

            images.append(images_item)

        property_enrichment_v2_image_results = cls(
            property_id=property_id,
            address_components=address_components,
            images=images,
        )

        property_enrichment_v2_image_results.additional_properties = d
        return property_enrichment_v2_image_results

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
