import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelInspection")


@_attrs_define
class DomainListingAdminServiceV1ModelInspection:
    """Inspection times

    Attributes:
        from_ (Union[Unset, datetime.datetime]): Format: yyyy-mm-dd HH:mm:ss eg: 2015-10-20 13:30:00
        to (Union[Unset, datetime.datetime]): Format: yyyy-mm-dd HH:mm:ss, eg: 2015-10-20 14:30:00
        repeat (Union[Unset, bool]): Specifies if the inspection is recurring weekly
    """

    from_: Union[Unset, datetime.datetime] = UNSET
    to: Union[Unset, datetime.datetime] = UNSET
    repeat: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        repeat = self.repeat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.datetime]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        repeat = d.pop("repeat", UNSET)

        domain_listing_admin_service_v1_model_inspection = cls(
            from_=from_,
            to=to,
            repeat=repeat,
        )

        domain_listing_admin_service_v1_model_inspection.additional_properties = d
        return domain_listing_admin_service_v1_model_inspection

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
