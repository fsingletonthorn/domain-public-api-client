import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1SoldDetails")


@_attrs_define
class PreMarketV1SoldDetails:
    """
    Attributes:
        sold_price (Union[None, Unset, int]): Price the property was sold for.
        sold_date (Union[None, Unset, datetime.datetime]): The date when the property was sold.
            The date must comply with the ISO 8601 and be in the UTC format, e.g. 2021-10-15T13:45:30.0000000Z.
    """

    sold_price: Union[None, Unset, int] = UNSET
    sold_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sold_price: Union[None, Unset, int]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        sold_date: Union[None, Unset, str]
        if isinstance(self.sold_date, Unset):
            sold_date = UNSET
        elif isinstance(self.sold_date, datetime.datetime):
            sold_date = self.sold_date.isoformat()
        else:
            sold_date = self.sold_date

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_sold_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))

        def _parse_sold_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sold_date_type_0 = isoparse(data)

                return sold_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sold_date = _parse_sold_date(d.pop("soldDate", UNSET))

        pre_market_v1_sold_details = cls(
            sold_price=sold_price,
            sold_date=sold_date,
        )

        return pre_market_v1_sold_details
