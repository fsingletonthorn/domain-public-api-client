from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnquiriesV1Sender")


@_attrs_define
class EnquiriesV1Sender:
    """
    Attributes:
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        phone_number (Union[None, Unset, str]):
        postcode (Union[None, Unset, str]):
    """

    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    phone_number: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone_number: Union[None, Unset, str]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        field_dict: Dict[str, Any] = {}
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

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        enquiries_v1_sender = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            postcode=postcode,
        )

        return enquiries_v1_sender
