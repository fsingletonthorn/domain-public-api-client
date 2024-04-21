from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.domain_avm_piv1_confidence_enum import DomainAvmPIV1ConfidenceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainAvmPIV1PropertyPriceEstimateHistory")


@_attrs_define
class DomainAvmPIV1PropertyPriceEstimateHistory:
    """
    Attributes:
        confidence (Union[Unset, DomainAvmPIV1ConfidenceEnum]):
        date (Union[None, Unset, str]):
        lower_price (Union[None, Unset, float]):
        mid_price (Union[None, Unset, float]):
        source (Union[None, Unset, str]):
        upper_price (Union[None, Unset, float]):
    """

    confidence: Union[Unset, DomainAvmPIV1ConfidenceEnum] = UNSET
    date: Union[None, Unset, str] = UNSET
    lower_price: Union[None, Unset, float] = UNSET
    mid_price: Union[None, Unset, float] = UNSET
    source: Union[None, Unset, str] = UNSET
    upper_price: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        confidence: Union[Unset, str] = UNSET
        if not isinstance(self.confidence, Unset):
            confidence = self.confidence.value

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        lower_price: Union[None, Unset, float]
        if isinstance(self.lower_price, Unset):
            lower_price = UNSET
        else:
            lower_price = self.lower_price

        mid_price: Union[None, Unset, float]
        if isinstance(self.mid_price, Unset):
            mid_price = UNSET
        else:
            mid_price = self.mid_price

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        upper_price: Union[None, Unset, float]
        if isinstance(self.upper_price, Unset):
            upper_price = UNSET
        else:
            upper_price = self.upper_price

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if date is not UNSET:
            field_dict["date"] = date
        if lower_price is not UNSET:
            field_dict["lowerPrice"] = lower_price
        if mid_price is not UNSET:
            field_dict["midPrice"] = mid_price
        if source is not UNSET:
            field_dict["source"] = source
        if upper_price is not UNSET:
            field_dict["upperPrice"] = upper_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _confidence = d.pop("confidence", UNSET)
        confidence: Union[Unset, DomainAvmPIV1ConfidenceEnum]
        if isinstance(_confidence, Unset):
            confidence = UNSET
        else:
            confidence = DomainAvmPIV1ConfidenceEnum(_confidence)

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_lower_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lower_price = _parse_lower_price(d.pop("lowerPrice", UNSET))

        def _parse_mid_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        mid_price = _parse_mid_price(d.pop("midPrice", UNSET))

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_upper_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        upper_price = _parse_upper_price(d.pop("upperPrice", UNSET))

        domain_avm_piv1_property_price_estimate_history = cls(
            confidence=confidence,
            date=date,
            lower_price=lower_price,
            mid_price=mid_price,
            source=source,
            upper_price=upper_price,
        )

        return domain_avm_piv1_property_price_estimate_history
