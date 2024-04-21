from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1ProviderDetails")


@_attrs_define
class PreMarketV1ProviderDetails:
    """Information for the listing provider

    Attributes:
        provider_system (Union[None, Unset, str]): Identify the source of the listing
        provider_ad_id (Union[None, Unset, str]): Unique ID within provider system
    """

    provider_system: Union[None, Unset, str] = UNSET
    provider_ad_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        provider_system: Union[None, Unset, str]
        if isinstance(self.provider_system, Unset):
            provider_system = UNSET
        else:
            provider_system = self.provider_system

        provider_ad_id: Union[None, Unset, str]
        if isinstance(self.provider_ad_id, Unset):
            provider_ad_id = UNSET
        else:
            provider_ad_id = self.provider_ad_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if provider_system is not UNSET:
            field_dict["providerSystem"] = provider_system
        if provider_ad_id is not UNSET:
            field_dict["providerAdID"] = provider_ad_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_provider_system(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_system = _parse_provider_system(d.pop("providerSystem", UNSET))

        def _parse_provider_ad_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_ad_id = _parse_provider_ad_id(d.pop("providerAdID", UNSET))

        pre_market_v1_provider_details = cls(
            provider_system=provider_system,
            provider_ad_id=provider_ad_id,
        )

        return pre_market_v1_provider_details
