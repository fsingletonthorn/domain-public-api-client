import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2SaleListingHistory")


@_attrs_define
class PropertyEnrichmentV2SaleListingHistory:
    """property listing history object

    Attributes:
        id (Union[Unset, str]):
        agency_id (Union[None, Unset, str]):
        agency_name (Union[None, Unset, str]):
        first_listed_date (Union[None, Unset, str]):
        last_listed_date (Union[None, Unset, str]):
        listed_price (Union[None, Unset, str]):
        days_on_market (Union[None, Unset, int]):
        sold_date (Union[None, Unset, datetime.date]): Sold date in YYYY-MM-DD format
        sold_price (Union[None, Unset, float]): sold price
        sale_type (Union[None, Unset, str]):
        withdrawn (Union[None, Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    agency_id: Union[None, Unset, str] = UNSET
    agency_name: Union[None, Unset, str] = UNSET
    first_listed_date: Union[None, Unset, str] = UNSET
    last_listed_date: Union[None, Unset, str] = UNSET
    listed_price: Union[None, Unset, str] = UNSET
    days_on_market: Union[None, Unset, int] = UNSET
    sold_date: Union[None, Unset, datetime.date] = UNSET
    sold_price: Union[None, Unset, float] = UNSET
    sale_type: Union[None, Unset, str] = UNSET
    withdrawn: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        agency_id: Union[None, Unset, str]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        agency_name: Union[None, Unset, str]
        if isinstance(self.agency_name, Unset):
            agency_name = UNSET
        else:
            agency_name = self.agency_name

        first_listed_date: Union[None, Unset, str]
        if isinstance(self.first_listed_date, Unset):
            first_listed_date = UNSET
        else:
            first_listed_date = self.first_listed_date

        last_listed_date: Union[None, Unset, str]
        if isinstance(self.last_listed_date, Unset):
            last_listed_date = UNSET
        else:
            last_listed_date = self.last_listed_date

        listed_price: Union[None, Unset, str]
        if isinstance(self.listed_price, Unset):
            listed_price = UNSET
        else:
            listed_price = self.listed_price

        days_on_market: Union[None, Unset, int]
        if isinstance(self.days_on_market, Unset):
            days_on_market = UNSET
        else:
            days_on_market = self.days_on_market

        sold_date: Union[None, Unset, str]
        if isinstance(self.sold_date, Unset):
            sold_date = UNSET
        elif isinstance(self.sold_date, datetime.date):
            sold_date = self.sold_date.isoformat()
        else:
            sold_date = self.sold_date

        sold_price: Union[None, Unset, float]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        sale_type: Union[None, Unset, str]
        if isinstance(self.sale_type, Unset):
            sale_type = UNSET
        else:
            sale_type = self.sale_type

        withdrawn: Union[None, Unset, bool]
        if isinstance(self.withdrawn, Unset):
            withdrawn = UNSET
        else:
            withdrawn = self.withdrawn

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if first_listed_date is not UNSET:
            field_dict["firstListedDate"] = first_listed_date
        if last_listed_date is not UNSET:
            field_dict["lastListedDate"] = last_listed_date
        if listed_price is not UNSET:
            field_dict["listedPrice"] = listed_price
        if days_on_market is not UNSET:
            field_dict["daysOnMarket"] = days_on_market
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if sale_type is not UNSET:
            field_dict["saleType"] = sale_type
        if withdrawn is not UNSET:
            field_dict["withdrawn"] = withdrawn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_agency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_agency_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_name = _parse_agency_name(d.pop("agencyName", UNSET))

        def _parse_first_listed_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_listed_date = _parse_first_listed_date(d.pop("firstListedDate", UNSET))

        def _parse_last_listed_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_listed_date = _parse_last_listed_date(d.pop("lastListedDate", UNSET))

        def _parse_listed_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        listed_price = _parse_listed_price(d.pop("listedPrice", UNSET))

        def _parse_days_on_market(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        days_on_market = _parse_days_on_market(d.pop("daysOnMarket", UNSET))

        def _parse_sold_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sold_date_type_0 = isoparse(data).date()

                return sold_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        sold_date = _parse_sold_date(d.pop("soldDate", UNSET))

        def _parse_sold_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))

        def _parse_sale_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sale_type = _parse_sale_type(d.pop("saleType", UNSET))

        def _parse_withdrawn(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        withdrawn = _parse_withdrawn(d.pop("withdrawn", UNSET))

        property_enrichment_v2_sale_listing_history = cls(
            id=id,
            agency_id=agency_id,
            agency_name=agency_name,
            first_listed_date=first_listed_date,
            last_listed_date=last_listed_date,
            listed_price=listed_price,
            days_on_market=days_on_market,
            sold_date=sold_date,
            sold_price=sold_price,
            sale_type=sale_type,
            withdrawn=withdrawn,
        )

        return property_enrichment_v2_sale_listing_history
