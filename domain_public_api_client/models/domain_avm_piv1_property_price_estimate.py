from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.domain_avm_piv1_confidence_enum import DomainAvmPIV1ConfidenceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_avm_piv1_property_price_estimate_history import DomainAvmPIV1PropertyPriceEstimateHistory


T = TypeVar("T", bound="DomainAvmPIV1PropertyPriceEstimate")


@_attrs_define
class DomainAvmPIV1PropertyPriceEstimate:
    """
    Attributes:
        date (Union[None, Unset, str]):
        lower_price (Union[None, Unset, float]):
        mid_price (Union[None, Unset, float]):
        price_confidence (Union[Unset, DomainAvmPIV1ConfidenceEnum]):
        source (Union[None, Unset, str]):
        upper_price (Union[None, Unset, float]):
        history (Union[List['DomainAvmPIV1PropertyPriceEstimateHistory'], None, Unset]):
    """

    date: Union[None, Unset, str] = UNSET
    lower_price: Union[None, Unset, float] = UNSET
    mid_price: Union[None, Unset, float] = UNSET
    price_confidence: Union[Unset, DomainAvmPIV1ConfidenceEnum] = UNSET
    source: Union[None, Unset, str] = UNSET
    upper_price: Union[None, Unset, float] = UNSET
    history: Union[List["DomainAvmPIV1PropertyPriceEstimateHistory"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        price_confidence: Union[Unset, str] = UNSET
        if not isinstance(self.price_confidence, Unset):
            price_confidence = self.price_confidence.value

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

        history: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, list):
            history = []
            for history_type_0_item_data in self.history:
                history_type_0_item = history_type_0_item_data.to_dict()
                history.append(history_type_0_item)

        else:
            history = self.history

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if lower_price is not UNSET:
            field_dict["lowerPrice"] = lower_price
        if mid_price is not UNSET:
            field_dict["midPrice"] = mid_price
        if price_confidence is not UNSET:
            field_dict["priceConfidence"] = price_confidence
        if source is not UNSET:
            field_dict["source"] = source
        if upper_price is not UNSET:
            field_dict["upperPrice"] = upper_price
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_avm_piv1_property_price_estimate_history import DomainAvmPIV1PropertyPriceEstimateHistory

        d = src_dict.copy()

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

        _price_confidence = d.pop("priceConfidence", UNSET)
        price_confidence: Union[Unset, DomainAvmPIV1ConfidenceEnum]
        if isinstance(_price_confidence, Unset):
            price_confidence = UNSET
        else:
            price_confidence = DomainAvmPIV1ConfidenceEnum(_price_confidence)

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

        def _parse_history(data: object) -> Union[List["DomainAvmPIV1PropertyPriceEstimateHistory"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_0 = []
                _history_type_0 = data
                for history_type_0_item_data in _history_type_0:
                    history_type_0_item = DomainAvmPIV1PropertyPriceEstimateHistory.from_dict(history_type_0_item_data)

                    history_type_0.append(history_type_0_item)

                return history_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DomainAvmPIV1PropertyPriceEstimateHistory"], None, Unset], data)

        history = _parse_history(d.pop("history", UNSET))

        domain_avm_piv1_property_price_estimate = cls(
            date=date,
            lower_price=lower_price,
            mid_price=mid_price,
            price_confidence=price_confidence,
            source=source,
            upper_price=upper_price,
            history=history,
        )

        return domain_avm_piv1_property_price_estimate
