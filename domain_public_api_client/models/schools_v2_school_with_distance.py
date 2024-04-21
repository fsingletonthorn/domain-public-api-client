from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schools_v2_school import SchoolsV2School


T = TypeVar("T", bound="SchoolsV2SchoolWithDistance")


@_attrs_define
class SchoolsV2SchoolWithDistance:
    """SchoolWithDistance

    Attributes:
        distance (Union[None, Unset, float]): Gets or Sets Distance
        school (Union[Unset, SchoolsV2School]): School
    """

    distance: Union[None, Unset, float] = UNSET
    school: Union[Unset, "SchoolsV2School"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        distance: Union[None, Unset, float]
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        school: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.school, Unset):
            school = self.school.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if distance is not UNSET:
            field_dict["distance"] = distance
        if school is not UNSET:
            field_dict["school"] = school

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schools_v2_school import SchoolsV2School

        d = src_dict.copy()

        def _parse_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        distance = _parse_distance(d.pop("distance", UNSET))

        _school = d.pop("school", UNSET)
        school: Union[Unset, SchoolsV2School]
        if isinstance(_school, Unset):
            school = UNSET
        else:
            school = SchoolsV2School.from_dict(_school)

        schools_v2_school_with_distance = cls(
            distance=distance,
            school=school,
        )

        return schools_v2_school_with_distance
