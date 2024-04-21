from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.social_boost_v1_rate_for_new_social_boost_reason import SocialBoostV1RateForNewSocialBoostReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_boost_v1_contract_info import SocialBoostV1ContractInfo
    from ..models.social_boost_v1_listing_rate_info import SocialBoostV1ListingRateInfo


T = TypeVar("T", bound="SocialBoostV1RateForNewSocialBoost")


@_attrs_define
class SocialBoostV1RateForNewSocialBoost:
    """GetRatesForNewSocialBoostResponse

    Attributes:
        reason (Union[Unset, SocialBoostV1RateForNewSocialBoostReason]): Gets or Sets Reason
        contract (Union[Unset, SocialBoostV1ContractInfo]): ContractInfo
        rate (Union[Unset, SocialBoostV1ListingRateInfo]): ListingRateInfo
    """

    reason: Union[Unset, SocialBoostV1RateForNewSocialBoostReason] = UNSET
    contract: Union[Unset, "SocialBoostV1ContractInfo"] = UNSET
    rate: Union[Unset, "SocialBoostV1ListingRateInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contract, Unset):
            contract = self.contract.to_dict()

        rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if contract is not UNSET:
            field_dict["contract"] = contract
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.social_boost_v1_contract_info import SocialBoostV1ContractInfo
        from ..models.social_boost_v1_listing_rate_info import SocialBoostV1ListingRateInfo

        d = src_dict.copy()
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SocialBoostV1RateForNewSocialBoostReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = SocialBoostV1RateForNewSocialBoostReason(_reason)

        _contract = d.pop("contract", UNSET)
        contract: Union[Unset, SocialBoostV1ContractInfo]
        if isinstance(_contract, Unset):
            contract = UNSET
        else:
            contract = SocialBoostV1ContractInfo.from_dict(_contract)

        _rate = d.pop("rate", UNSET)
        rate: Union[Unset, SocialBoostV1ListingRateInfo]
        if isinstance(_rate, Unset):
            rate = UNSET
        else:
            rate = SocialBoostV1ListingRateInfo.from_dict(_rate)

        social_boost_v1_rate_for_new_social_boost = cls(
            reason=reason,
            contract=contract,
            rate=rate,
        )

        return social_boost_v1_rate_for_new_social_boost
