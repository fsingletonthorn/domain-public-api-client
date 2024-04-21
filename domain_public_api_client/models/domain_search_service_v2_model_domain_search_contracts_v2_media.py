from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_media_category import (
    DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2Media")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2Media:
    """
    Attributes:
        category (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory]):
        url (Union[Unset, str]):
    """

    category: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory(_category)

        url = d.pop("url", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_media = cls(
            category=category,
            url=url,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_media.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_media

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
