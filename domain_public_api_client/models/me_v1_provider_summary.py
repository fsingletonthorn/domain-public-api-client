from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeV1ProviderSummary")


@_attrs_define
class MeV1ProviderSummary:
    """Create provider response

    Attributes:
        id (Union[None, Unset, str]): Provider identifier - this will map to the username
        company_name (Union[None, Unset, str]): Company name
        contact_name_technical (Union[None, Unset, str]): Contact person's name for technical related enquiries
        email_technical (Union[None, Unset, str]): Email address to receive technical related emails
        phone_technical (Union[None, Unset, str]): Phone to be contact for technical related enquiries
        contact_name_business (Union[None, Unset, str]): Contact person's name for business related enquiries
        email_business (Union[None, Unset, str]): Email address to receive business related emails
        phone_business (Union[None, Unset, str]): Phone to be contact for business related enquiries
    """

    id: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    contact_name_technical: Union[None, Unset, str] = UNSET
    email_technical: Union[None, Unset, str] = UNSET
    phone_technical: Union[None, Unset, str] = UNSET
    contact_name_business: Union[None, Unset, str] = UNSET
    email_business: Union[None, Unset, str] = UNSET
    phone_business: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        contact_name_technical: Union[None, Unset, str]
        if isinstance(self.contact_name_technical, Unset):
            contact_name_technical = UNSET
        else:
            contact_name_technical = self.contact_name_technical

        email_technical: Union[None, Unset, str]
        if isinstance(self.email_technical, Unset):
            email_technical = UNSET
        else:
            email_technical = self.email_technical

        phone_technical: Union[None, Unset, str]
        if isinstance(self.phone_technical, Unset):
            phone_technical = UNSET
        else:
            phone_technical = self.phone_technical

        contact_name_business: Union[None, Unset, str]
        if isinstance(self.contact_name_business, Unset):
            contact_name_business = UNSET
        else:
            contact_name_business = self.contact_name_business

        email_business: Union[None, Unset, str]
        if isinstance(self.email_business, Unset):
            email_business = UNSET
        else:
            email_business = self.email_business

        phone_business: Union[None, Unset, str]
        if isinstance(self.phone_business, Unset):
            phone_business = UNSET
        else:
            phone_business = self.phone_business

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if contact_name_technical is not UNSET:
            field_dict["contactNameTechnical"] = contact_name_technical
        if email_technical is not UNSET:
            field_dict["emailTechnical"] = email_technical
        if phone_technical is not UNSET:
            field_dict["phoneTechnical"] = phone_technical
        if contact_name_business is not UNSET:
            field_dict["contactNameBusiness"] = contact_name_business
        if email_business is not UNSET:
            field_dict["emailBusiness"] = email_business
        if phone_business is not UNSET:
            field_dict["phoneBusiness"] = phone_business

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_contact_name_technical(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contact_name_technical = _parse_contact_name_technical(d.pop("contactNameTechnical", UNSET))

        def _parse_email_technical(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_technical = _parse_email_technical(d.pop("emailTechnical", UNSET))

        def _parse_phone_technical(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_technical = _parse_phone_technical(d.pop("phoneTechnical", UNSET))

        def _parse_contact_name_business(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contact_name_business = _parse_contact_name_business(d.pop("contactNameBusiness", UNSET))

        def _parse_email_business(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_business = _parse_email_business(d.pop("emailBusiness", UNSET))

        def _parse_phone_business(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_business = _parse_phone_business(d.pop("phoneBusiness", UNSET))

        me_v1_provider_summary = cls(
            id=id,
            company_name=company_name,
            contact_name_technical=contact_name_technical,
            email_technical=email_technical,
            phone_technical=phone_technical,
            contact_name_business=contact_name_business,
            email_business=email_business,
            phone_business=phone_business,
        )

        return me_v1_provider_summary
