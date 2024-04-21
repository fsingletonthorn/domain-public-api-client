from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v2_median_price_data_price_type import ListingsV2MedianPriceDataPriceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2MedianPriceData")


@_attrs_define
class ListingsV2MedianPriceData:
    """Information regarding median house/unit price   for the suburb

    Attributes:
        price_type (Union[Unset, ListingsV2MedianPriceDataPriceType]): Gets or Sets PriceType
        suburb (Union[None, Unset, str]): Name of the suburb median price is based on.
        postcode (Union[None, Unset, str]): Postcode of the suburb
        median_price (Union[None, Unset, int]): Median price for the suburb.
        source (Union[None, Unset, str]): Where median price data comes from
        source_date_from (Union[None, Unset, str]): Start date of the median price source time period
        source_date_to (Union[None, Unset, str]): End date of the median price source time period
        source_collection_date (Union[None, Unset, str]): The collection date of the median price source
    """

    price_type: Union[Unset, ListingsV2MedianPriceDataPriceType] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    median_price: Union[None, Unset, int] = UNSET
    source: Union[None, Unset, str] = UNSET
    source_date_from: Union[None, Unset, str] = UNSET
    source_date_to: Union[None, Unset, str] = UNSET
    source_collection_date: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        median_price: Union[None, Unset, int]
        if isinstance(self.median_price, Unset):
            median_price = UNSET
        else:
            median_price = self.median_price

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_date_from: Union[None, Unset, str]
        if isinstance(self.source_date_from, Unset):
            source_date_from = UNSET
        else:
            source_date_from = self.source_date_from

        source_date_to: Union[None, Unset, str]
        if isinstance(self.source_date_to, Unset):
            source_date_to = UNSET
        else:
            source_date_to = self.source_date_to

        source_collection_date: Union[None, Unset, str]
        if isinstance(self.source_collection_date, Unset):
            source_collection_date = UNSET
        else:
            source_collection_date = self.source_collection_date

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if median_price is not UNSET:
            field_dict["medianPrice"] = median_price
        if source is not UNSET:
            field_dict["source"] = source
        if source_date_from is not UNSET:
            field_dict["sourceDateFrom"] = source_date_from
        if source_date_to is not UNSET:
            field_dict["sourceDateTo"] = source_date_to
        if source_collection_date is not UNSET:
            field_dict["sourceCollectionDate"] = source_collection_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _price_type = d.pop("priceType", UNSET)
        price_type: Union[Unset, ListingsV2MedianPriceDataPriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = ListingsV2MedianPriceDataPriceType(_price_type)

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_median_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        median_price = _parse_median_price(d.pop("medianPrice", UNSET))

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_source_date_from(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_date_from = _parse_source_date_from(d.pop("sourceDateFrom", UNSET))

        def _parse_source_date_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_date_to = _parse_source_date_to(d.pop("sourceDateTo", UNSET))

        def _parse_source_collection_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_collection_date = _parse_source_collection_date(d.pop("sourceCollectionDate", UNSET))

        listings_v2_median_price_data = cls(
            price_type=price_type,
            suburb=suburb,
            postcode=postcode,
            median_price=median_price,
            source=source,
            source_date_from=source_date_from,
            source_date_to=source_date_to,
            source_collection_date=source_collection_date,
        )

        return listings_v2_median_price_data
