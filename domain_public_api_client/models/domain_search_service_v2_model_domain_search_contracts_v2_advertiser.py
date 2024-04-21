from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_advertiser_type import (
    DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_contact import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Contact,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2Advertiser:
    """
    Attributes:
        type (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        preferred_colour_hex (Union[Unset, str]):
        banner_url (Union[Unset, str]):
        contacts (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchContractsV2Contact']]):
    """

    type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    preferred_colour_hex: Union[Unset, str] = UNSET
    banner_url: Union[Unset, str] = UNSET
    contacts: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchContractsV2Contact"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        name = self.name

        logo_url = self.logo_url

        preferred_colour_hex = self.preferred_colour_hex

        banner_url = self.banner_url

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if preferred_colour_hex is not UNSET:
            field_dict["preferredColourHex"] = preferred_colour_hex
        if banner_url is not UNSET:
            field_dict["bannerUrl"] = banner_url
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_contact import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Contact,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType(_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        preferred_colour_hex = d.pop("preferredColourHex", UNSET)

        banner_url = d.pop("bannerUrl", UNSET)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = DomainSearchServiceV2ModelDomainSearchContractsV2Contact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        domain_search_service_v2_model_domain_search_contracts_v2_advertiser = cls(
            type=type,
            id=id,
            name=name,
            logo_url=logo_url,
            preferred_colour_hex=preferred_colour_hex,
            banner_url=banner_url,
            contacts=contacts,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_advertiser.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_advertiser

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
