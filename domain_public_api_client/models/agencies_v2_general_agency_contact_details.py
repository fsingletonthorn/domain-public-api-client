from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2GeneralAgencyContactDetails")


@_attrs_define
class AgenciesV2GeneralAgencyContactDetails:
    """GeneralAgencyContactDetails

    Attributes:
        email (Union[None, Unset, str]): Gets or Sets Email
        fax (Union[None, Unset, str]): Gets or Sets Fax
        phone (Union[None, Unset, str]): Gets or Sets Phone
        mobile (Union[None, Unset, str]): Gets or Sets Mobile
    """

    email: Union[None, Unset, str] = UNSET
    fax: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    mobile: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if phone is not UNSET:
            field_dict["phone"] = phone
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

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

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

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

        agencies_v2_general_agency_contact_details = cls(
            email=email,
            fax=fax,
            phone=phone,
            mobile=mobile,
        )

        return agencies_v2_general_agency_contact_details
