import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorities_v1_address import AuthoritiesV1Address


T = TypeVar("T", bound="AuthoritiesV1IndividualResponse")


@_attrs_define
class AuthoritiesV1IndividualResponse:
    """
    Attributes:
        address (AuthoritiesV1Address):
        email (str):  Example: johndoe@email.com.
        first_name (str):  Example: John.
        last_name (str):  Example: Smith.
        mobile (str):  Example: 1234567890.
        phone_number (str):  Example: 1234567890.
        id (str):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        date_of_birth (Union[None, Unset, datetime.date]):  Example: 2022-07-16.
        middle_name (Union[Unset, str]):  Example: Doe.
        title (Union[Unset, str]):
        type (Union[Unset, str]): Available options are: `individual`, `company` Example: individual.
    """

    address: "AuthoritiesV1Address"
    email: str
    first_name: str
    last_name: str
    mobile: str
    phone_number: str
    id: str
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    middle_name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        mobile = self.mobile

        phone_number = self.phone_number

        id = self.id

        date_of_birth: Union[None, Unset, str]
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        middle_name = self.middle_name

        title = self.title

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "mobile": mobile,
                "phoneNumber": phone_number,
                "id": id,
            }
        )
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorities_v1_address import AuthoritiesV1Address

        d = src_dict.copy()
        address = AuthoritiesV1Address.from_dict(d.pop("address"))

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        mobile = d.pop("mobile")

        phone_number = d.pop("phoneNumber")

        id = d.pop("id")

        def _parse_date_of_birth(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = isoparse(data).date()

                return date_of_birth_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))

        middle_name = d.pop("middleName", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        authorities_v1_individual_response = cls(
            address=address,
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            phone_number=phone_number,
            id=id,
            date_of_birth=date_of_birth,
            middle_name=middle_name,
            title=title,
            type=type,
        )

        authorities_v1_individual_response.additional_properties = d
        return authorities_v1_individual_response

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
