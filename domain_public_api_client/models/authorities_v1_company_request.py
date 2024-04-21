from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorities_v1_address import AuthoritiesV1Address


T = TypeVar("T", bound="AuthoritiesV1CompanyRequest")


@_attrs_define
class AuthoritiesV1CompanyRequest:
    """
    Attributes:
        address (AuthoritiesV1Address):
        email (str):  Example: johndoe@email.com.
        id (Union[Unset, str]):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        name (Union[Unset, str]):  Example: Company Name.
        phone_number (Union[Unset, str]):  Example: 1234567890.
        fax (Union[Unset, str]):  Example: 1234567890.
        abn (Union[Unset, str]):  Example: 1234567890.
        acn (Union[Unset, str]):  Example: 1234567890.
        gst_registered (Union[None, Unset, bool]):
        type (Union[Unset, str]): Available options are: `individual`, `company` Example: company.
    """

    address: "AuthoritiesV1Address"
    email: str
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    abn: Union[Unset, str] = UNSET
    acn: Union[Unset, str] = UNSET
    gst_registered: Union[None, Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        email = self.email

        id = self.id

        name = self.name

        phone_number = self.phone_number

        fax = self.fax

        abn = self.abn

        acn = self.acn

        gst_registered: Union[None, Unset, bool]
        if isinstance(self.gst_registered, Unset):
            gst_registered = UNSET
        else:
            gst_registered = self.gst_registered

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "email": email,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if fax is not UNSET:
            field_dict["fax"] = fax
        if abn is not UNSET:
            field_dict["abn"] = abn
        if acn is not UNSET:
            field_dict["acn"] = acn
        if gst_registered is not UNSET:
            field_dict["gstRegistered"] = gst_registered
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorities_v1_address import AuthoritiesV1Address

        d = src_dict.copy()
        address = AuthoritiesV1Address.from_dict(d.pop("address"))

        email = d.pop("email")

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        fax = d.pop("fax", UNSET)

        abn = d.pop("abn", UNSET)

        acn = d.pop("acn", UNSET)

        def _parse_gst_registered(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        gst_registered = _parse_gst_registered(d.pop("gstRegistered", UNSET))

        type = d.pop("type", UNSET)

        authorities_v1_company_request = cls(
            address=address,
            email=email,
            id=id,
            name=name,
            phone_number=phone_number,
            fax=fax,
            abn=abn,
            acn=acn,
            gst_registered=gst_registered,
            type=type,
        )

        authorities_v1_company_request.additional_properties = d
        return authorities_v1_company_request

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
