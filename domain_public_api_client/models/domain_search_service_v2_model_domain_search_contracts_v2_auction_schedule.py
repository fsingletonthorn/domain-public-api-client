import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2AuctionSchedule:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]):
        auction_location (Union[Unset, str]):
    """

    time: Union[Unset, datetime.datetime] = UNSET
    auction_location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        auction_location = self.auction_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if auction_location is not UNSET:
            field_dict["auctionLocation"] = auction_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        auction_location = d.pop("auctionLocation", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_auction_schedule = cls(
            time=time,
            auction_location=auction_location,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_auction_schedule.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_auction_schedule

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
