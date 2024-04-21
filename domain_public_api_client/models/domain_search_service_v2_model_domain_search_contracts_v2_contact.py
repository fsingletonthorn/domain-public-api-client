from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2Contact")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2Contact:
    """
    Attributes:
        name (Union[Unset, str]):
        photo_url (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    photo_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        photo_url = self.photo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        photo_url = d.pop("photoUrl", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_contact = cls(
            name=name,
            photo_url=photo_url,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_contact.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_contact

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
