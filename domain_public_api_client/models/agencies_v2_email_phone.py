from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2EmailPhone")


@_attrs_define
class AgenciesV2EmailPhone:
    """EmailPhone

    Attributes:
        email (Union[None, Unset, str]): Gets or Sets Email
        phone (Union[None, Unset, str]): Gets or Sets Phone
    """

    email: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        agencies_v2_email_phone = cls(
            email=email,
            phone=phone,
        )

        return agencies_v2_email_phone
