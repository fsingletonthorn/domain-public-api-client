from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1EnquiriesSender")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1EnquiriesSender:
    """Contains enquiry sender details

    Attributes:
        first_name (Union[Unset, str]): Sender first name
        last_name (Union[Unset, str]): Sender lastname/surname
        email (Union[Unset, str]): Sender email address
        phone_number (Union[Unset, str]): Sender phone number
        postcode (Union[Unset, str]): Postcode of sender's location
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone_number = self.phone_number

        postcode = self.postcode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if postcode is not UNSET:
            field_dict["postcode"] = postcode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        postcode = d.pop("postcode", UNSET)

        domain_public_adapter_web_api_models_v1_enquiries_sender = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            postcode=postcode,
        )

        domain_public_adapter_web_api_models_v1_enquiries_sender.additional_properties = d
        return domain_public_adapter_web_api_models_v1_enquiries_sender

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
