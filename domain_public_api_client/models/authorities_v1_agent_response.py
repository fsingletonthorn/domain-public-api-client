from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthoritiesV1AgentResponse")


@_attrs_define
class AuthoritiesV1AgentResponse:
    """
    Attributes:
        name (str):  Example: John Doe.
        email (str):  Example: johndoe@email.com.
        id (str):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        user (Union[Unset, str]):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        mobile (Union[Unset, str]):  Example: 0123456789.
        office_number (Union[Unset, str]):  Example: 0123456789.
        license_number (Union[Unset, str]):  Example: 0123456789.
    """

    name: str
    email: str
    id: str
    user: Union[Unset, str] = UNSET
    mobile: Union[Unset, str] = UNSET
    office_number: Union[Unset, str] = UNSET
    license_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        email = self.email

        id = self.id

        user = self.user

        mobile = self.mobile

        office_number = self.office_number

        license_number = self.license_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "id": id,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if office_number is not UNSET:
            field_dict["officeNumber"] = office_number
        if license_number is not UNSET:
            field_dict["licenseNumber"] = license_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email")

        id = d.pop("id")

        user = d.pop("user", UNSET)

        mobile = d.pop("mobile", UNSET)

        office_number = d.pop("officeNumber", UNSET)

        license_number = d.pop("licenseNumber", UNSET)

        authorities_v1_agent_response = cls(
            name=name,
            email=email,
            id=id,
            user=user,
            mobile=mobile,
            office_number=office_number,
            license_number=license_number,
        )

        authorities_v1_agent_response.additional_properties = d
        return authorities_v1_agent_response

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
