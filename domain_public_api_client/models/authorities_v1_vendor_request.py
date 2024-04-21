from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorities_v1_company_request import AuthoritiesV1CompanyRequest
    from ..models.authorities_v1_individual_request import AuthoritiesV1IndividualRequest


T = TypeVar("T", bound="AuthoritiesV1VendorRequest")


@_attrs_define
class AuthoritiesV1VendorRequest:
    """
    Attributes:
        contact (AuthoritiesV1IndividualRequest):
        nature (str):  Example: Legal Representative.
        order (int):  Example: 1.
        id (Union[Unset, str]):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        contact_represented (Union[Unset, AuthoritiesV1CompanyRequest]):
        concierge_opted_in (Union[None, Unset, bool]):
        trust (Union[None, Unset, str]):
        authority_attachments (Union[Unset, List[str]]): An array of attachment IDs.
    """

    contact: "AuthoritiesV1IndividualRequest"
    nature: str
    order: int
    id: Union[Unset, str] = UNSET
    contact_represented: Union[Unset, "AuthoritiesV1CompanyRequest"] = UNSET
    concierge_opted_in: Union[None, Unset, bool] = UNSET
    trust: Union[None, Unset, str] = UNSET
    authority_attachments: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        nature = self.nature

        order = self.order

        id = self.id

        contact_represented: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_represented, Unset):
            contact_represented = self.contact_represented.to_dict()

        concierge_opted_in: Union[None, Unset, bool]
        if isinstance(self.concierge_opted_in, Unset):
            concierge_opted_in = UNSET
        else:
            concierge_opted_in = self.concierge_opted_in

        trust: Union[None, Unset, str]
        if isinstance(self.trust, Unset):
            trust = UNSET
        else:
            trust = self.trust

        authority_attachments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authority_attachments, Unset):
            authority_attachments = self.authority_attachments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "nature": nature,
                "order": order,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if contact_represented is not UNSET:
            field_dict["contactRepresented"] = contact_represented
        if concierge_opted_in is not UNSET:
            field_dict["conciergeOptedIn"] = concierge_opted_in
        if trust is not UNSET:
            field_dict["trust"] = trust
        if authority_attachments is not UNSET:
            field_dict["authorityAttachments"] = authority_attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorities_v1_company_request import AuthoritiesV1CompanyRequest
        from ..models.authorities_v1_individual_request import AuthoritiesV1IndividualRequest

        d = src_dict.copy()
        contact = AuthoritiesV1IndividualRequest.from_dict(d.pop("contact"))

        nature = d.pop("nature")

        order = d.pop("order")

        id = d.pop("id", UNSET)

        _contact_represented = d.pop("contactRepresented", UNSET)
        contact_represented: Union[Unset, AuthoritiesV1CompanyRequest]
        if isinstance(_contact_represented, Unset):
            contact_represented = UNSET
        else:
            contact_represented = AuthoritiesV1CompanyRequest.from_dict(_contact_represented)

        def _parse_concierge_opted_in(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        concierge_opted_in = _parse_concierge_opted_in(d.pop("conciergeOptedIn", UNSET))

        def _parse_trust(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        trust = _parse_trust(d.pop("trust", UNSET))

        authority_attachments = cast(List[str], d.pop("authorityAttachments", UNSET))

        authorities_v1_vendor_request = cls(
            contact=contact,
            nature=nature,
            order=order,
            id=id,
            contact_represented=contact_represented,
            concierge_opted_in=concierge_opted_in,
            trust=trust,
            authority_attachments=authority_attachments,
        )

        authorities_v1_vendor_request.additional_properties = d
        return authorities_v1_vendor_request

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
