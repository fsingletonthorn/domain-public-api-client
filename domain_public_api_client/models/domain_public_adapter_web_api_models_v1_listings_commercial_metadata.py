from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_address_components import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialMetadata:
    """Listing metadata

    Attributes:
        address_components (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents]): Address
            components
    """

    address_components: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_address_components import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents,
        )

        d = src_dict.copy()
        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = DomainPublicAdapterWebApiModelsV1ListingsCommercialAddressComponents.from_dict(
                _address_components
            )

        domain_public_adapter_web_api_models_v1_listings_commercial_metadata = cls(
            address_components=address_components,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_metadata.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_metadata

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
