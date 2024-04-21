import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Inspection")


@_attrs_define
class ListingAdminV2Inspection:
    """Inspection times

    Attributes:
        from_ (datetime.datetime): Format: yyyy-mm-dd HH:mm:ss eg: 2015-10-20 13:30:00
        to (datetime.datetime): Format: yyyy-mm-dd HH:mm:ss, eg: 2015-10-20 14:30:00
        repeat (Union[Unset, bool]): Specifies if the inspection is recurring weekly
    """

    from_: datetime.datetime
    to: datetime.datetime
    repeat: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        repeat = self.repeat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        repeat = d.pop("repeat", UNSET)

        listing_admin_v2_inspection = cls(
            from_=from_,
            to=to,
            repeat=repeat,
        )

        listing_admin_v2_inspection.additional_properties = d
        return listing_admin_v2_inspection

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
