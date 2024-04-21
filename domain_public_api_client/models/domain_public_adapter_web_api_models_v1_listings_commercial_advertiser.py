from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_advertiser_images import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages,
    )
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_contact import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialContact,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiser:
    """Agency details

    Attributes:
        address (Union[Unset, str]): agency address
        id (Union[Unset, int]): Agency ID
        name (Union[Unset, str]): Agency Name
        preferred_color_hex (Union[Unset, str]): Agency color
        images (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages]): Agency images
            (logos, banners)
        contacts (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialContact']]): Agency contacts
        is_conjunctional (Union[Unset, bool]): Checks whether advertiser is conjunctional or not
    """

    address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    preferred_color_hex: Union[Unset, str] = UNSET
    images: Union[Unset, "DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages"] = UNSET
    contacts: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialContact"]] = UNSET
    is_conjunctional: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        id = self.id

        name = self.name

        preferred_color_hex = self.preferred_color_hex

        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        is_conjunctional = self.is_conjunctional

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if preferred_color_hex is not UNSET:
            field_dict["preferredColorHex"] = preferred_color_hex
        if images is not UNSET:
            field_dict["images"] = images
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if is_conjunctional is not UNSET:
            field_dict["isConjunctional"] = is_conjunctional

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_advertiser_images import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages,
        )
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_contact import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialContact,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        preferred_color_hex = d.pop("preferredColorHex", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = DomainPublicAdapterWebApiModelsV1ListingsCommercialAdvertiserImages.from_dict(_images)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        is_conjunctional = d.pop("isConjunctional", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_advertiser = cls(
            address=address,
            id=id,
            name=name,
            preferred_color_hex=preferred_color_hex,
            images=images,
            contacts=contacts,
            is_conjunctional=is_conjunctional,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_advertiser.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_advertiser

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
