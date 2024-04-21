from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.schools_v2_school_catchment_type import SchoolsV2SchoolCatchmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchoolsV2SchoolCatchment")


@_attrs_define
class SchoolsV2SchoolCatchment:
    """SchoolCatchment

    Attributes:
        type (Union[Unset, SchoolsV2SchoolCatchmentType]): Gets or Sets Type
    """

    type: Union[Unset, SchoolsV2SchoolCatchmentType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, SchoolsV2SchoolCatchmentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SchoolsV2SchoolCatchmentType(_type)

        schools_v2_school_catchment = cls(
            type=type,
        )

        return schools_v2_school_catchment
