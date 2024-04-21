from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_phone_number import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialPhoneNumber,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialContact")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialContact:
    """Contact

    Attributes:
        id (Union[Unset, int]): Agent identifier
        first_name (Union[Unset, str]): First name. Not available in CRE
        last_name (Union[Unset, str]): Last name. Not available in CRE
        image_url (Union[Unset, str]): Image URL
        display_full_name (Union[Unset, str]): Full name
        phone_numbers (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialPhoneNumber']]): Phone
            numbers
        email_address (Union[Unset, str]): E-mail address
        address (Union[Unset, str]): Full address
    """

    id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    display_full_name: Union[Unset, str] = UNSET
    phone_numbers: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialPhoneNumber"]] = UNSET
    email_address: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        image_url = self.image_url

        display_full_name = self.display_full_name

        phone_numbers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        email_address = self.email_address

        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if display_full_name is not UNSET:
            field_dict["displayFullName"] = display_full_name
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_phone_number import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialPhoneNumber,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        display_full_name = d.pop("displayFullName", UNSET)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialPhoneNumber.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        email_address = d.pop("emailAddress", UNSET)

        address = d.pop("address", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_contact = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            image_url=image_url,
            display_full_name=display_full_name,
            phone_numbers=phone_numbers,
            email_address=email_address,
            address=address,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_contact.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_contact

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
