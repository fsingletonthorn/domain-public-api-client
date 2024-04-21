import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2Inspection")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2Inspection:
    """
    Attributes:
        opening_time (Union[Unset, datetime.datetime]):
        closing_time (Union[Unset, datetime.datetime]):
    """

    opening_time: Union[Unset, datetime.datetime] = UNSET
    closing_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opening_time: Union[Unset, str] = UNSET
        if not isinstance(self.opening_time, Unset):
            opening_time = self.opening_time.isoformat()

        closing_time: Union[Unset, str] = UNSET
        if not isinstance(self.closing_time, Unset):
            closing_time = self.closing_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opening_time is not UNSET:
            field_dict["openingTime"] = opening_time
        if closing_time is not UNSET:
            field_dict["closingTime"] = closing_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _opening_time = d.pop("openingTime", UNSET)
        opening_time: Union[Unset, datetime.datetime]
        if isinstance(_opening_time, Unset):
            opening_time = UNSET
        else:
            opening_time = isoparse(_opening_time)

        _closing_time = d.pop("closingTime", UNSET)
        closing_time: Union[Unset, datetime.datetime]
        if isinstance(_closing_time, Unset):
            closing_time = UNSET
        else:
            closing_time = isoparse(_closing_time)

        domain_search_service_v2_model_domain_search_contracts_v2_inspection = cls(
            opening_time=opening_time,
            closing_time=closing_time,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_inspection.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_inspection

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
