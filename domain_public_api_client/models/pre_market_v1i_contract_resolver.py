from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreMarketV1IContractResolver")


@_attrs_define
class PreMarketV1IContractResolver:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pre_market_v1i_contract_resolver = cls()

        return pre_market_v1i_contract_resolver
