from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2AgentContact")


@_attrs_define
class ListingAdminV2AgentContact:
    """Represents a agent or conjunction agent domain model
    The only difference to normal contacts is agent contacts needs to have their agency specified

        Attributes:
            agency_id (int): Conjunction agent's agency
            domain_agent_id (Union[Unset, int]): Domain ID of the contact person at the agency
            first_name (Union[Unset, str]): First name. Maximum 50 characters.
            last_name (Union[Unset, str]): Last name. Maximum 50 characters.
            phone (Union[Unset, str]): Phone. Maximum 20 characters.
            fax (Union[Unset, str]): Fax. Maximum 20 characters.
            mobile (Union[Unset, str]): Mobile. Maximum 20 characters.
            email (Union[Unset, str]): Email. Maximum 100 characters.
            receive_emails (Union[Unset, bool]): Indicates whether the contact person should receive emails for the listing
    """

    agency_id: int
    domain_agent_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    mobile: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    receive_emails: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agency_id = self.agency_id

        domain_agent_id = self.domain_agent_id

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        fax = self.fax

        mobile = self.mobile

        email = self.email

        receive_emails = self.receive_emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agencyId": agency_id,
            }
        )
        if domain_agent_id is not UNSET:
            field_dict["domainAgentId"] = domain_agent_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if email is not UNSET:
            field_dict["email"] = email
        if receive_emails is not UNSET:
            field_dict["receiveEmails"] = receive_emails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agency_id = d.pop("agencyId")

        domain_agent_id = d.pop("domainAgentId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        mobile = d.pop("mobile", UNSET)

        email = d.pop("email", UNSET)

        receive_emails = d.pop("receiveEmails", UNSET)

        listing_admin_v2_agent_contact = cls(
            agency_id=agency_id,
            domain_agent_id=domain_agent_id,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            fax=fax,
            mobile=mobile,
            email=email,
            receive_emails=receive_emails,
        )

        listing_admin_v2_agent_contact.additional_properties = d
        return listing_admin_v2_agent_contact

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
