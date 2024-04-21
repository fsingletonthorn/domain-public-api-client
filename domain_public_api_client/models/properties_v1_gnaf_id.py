from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1GnafId")


@_attrs_define
class PropertiesV1GnafId:
    """DomainPropertyIdModelModelsGnafId

    Attributes:
        month_no (Union[None, Unset, int]): Gets or Sets MonthNo
        year_no (Union[None, Unset, int]): Gets or Sets YearNo
        gnaf_pid (Union[None, Unset, str]): Gets or Sets GnafPID
    """

    month_no: Union[None, Unset, int] = UNSET
    year_no: Union[None, Unset, int] = UNSET
    gnaf_pid: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        month_no: Union[None, Unset, int]
        if isinstance(self.month_no, Unset):
            month_no = UNSET
        else:
            month_no = self.month_no

        year_no: Union[None, Unset, int]
        if isinstance(self.year_no, Unset):
            year_no = UNSET
        else:
            year_no = self.year_no

        gnaf_pid: Union[None, Unset, str]
        if isinstance(self.gnaf_pid, Unset):
            gnaf_pid = UNSET
        else:
            gnaf_pid = self.gnaf_pid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if month_no is not UNSET:
            field_dict["monthNo"] = month_no
        if year_no is not UNSET:
            field_dict["yearNo"] = year_no
        if gnaf_pid is not UNSET:
            field_dict["gnafPID"] = gnaf_pid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_month_no(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        month_no = _parse_month_no(d.pop("monthNo", UNSET))

        def _parse_year_no(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        year_no = _parse_year_no(d.pop("yearNo", UNSET))

        def _parse_gnaf_pid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gnaf_pid = _parse_gnaf_pid(d.pop("gnafPID", UNSET))

        properties_v1_gnaf_id = cls(
            month_no=month_no,
            year_no=year_no,
            gnaf_pid=gnaf_pid,
        )

        return properties_v1_gnaf_id
