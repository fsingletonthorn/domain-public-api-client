from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1Contact")


@_attrs_define
class PreMarketV1Contact:
    """
    Attributes:
        first_name (str): First name of the agent contact.
        last_name (str): Last name of the agent contact.
        email (str): Agent contact email. Valid email address.
        phone (Union[None, Unset, str]): Agent contact phone number. Valid phone number.
        mobile (Union[None, Unset, str]): Agent contact mobile number. Valid mobile number.
        fax (Union[None, Unset, str]):
    """

    first_name: str
    last_name: str
    email: str
    phone: Union[None, Unset, str] = UNSET
    mobile: Union[None, Unset, str] = UNSET
    fax: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        mobile: Union[None, Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if fax is not UNSET:
            field_dict["fax"] = fax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_mobile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        pre_market_v1_contact = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            mobile=mobile,
            fax=fax,
        )

        return pre_market_v1_contact
