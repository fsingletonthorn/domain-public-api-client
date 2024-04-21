from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeV1AgencySummary")


@_attrs_define
class MeV1AgencySummary:
    """
    Attributes:
        id (Union[None, Unset, int]):
        name (Union[None, Unset, str]):
        admin (Union[None, Unset, bool]): True if this user is an admin of this agency
    """

    id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    admin: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        admin: Union[None, Unset, bool]
        if isinstance(self.admin, Unset):
            admin = UNSET
        else:
            admin = self.admin

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_admin(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        admin = _parse_admin(d.pop("admin", UNSET))

        me_v1_agency_summary = cls(
            id=id,
            name=name,
            admin=admin,
        )

        return me_v1_agency_summary
