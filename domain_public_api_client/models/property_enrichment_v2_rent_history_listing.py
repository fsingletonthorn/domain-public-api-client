import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2RentHistoryListing")


@_attrs_define
class PropertyEnrichmentV2RentHistoryListing:
    """
    Attributes:
        id (Union[Unset, str]):
        agency_name (Union[None, Unset, str]):
        agency_id (Union[None, Unset, str]):
        first_listed_date (Union[None, Unset, datetime.date]): First activity date in YYYY-MM-DD format
        last_listed_date (Union[None, Unset, datetime.date]): Last activity date in YYYY-MM-DD format
        last_listed_price (Union[None, Unset, float]):
        days_on_market (Union[None, Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    agency_name: Union[None, Unset, str] = UNSET
    agency_id: Union[None, Unset, str] = UNSET
    first_listed_date: Union[None, Unset, datetime.date] = UNSET
    last_listed_date: Union[None, Unset, datetime.date] = UNSET
    last_listed_price: Union[None, Unset, float] = UNSET
    days_on_market: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        agency_name: Union[None, Unset, str]
        if isinstance(self.agency_name, Unset):
            agency_name = UNSET
        else:
            agency_name = self.agency_name

        agency_id: Union[None, Unset, str]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        first_listed_date: Union[None, Unset, str]
        if isinstance(self.first_listed_date, Unset):
            first_listed_date = UNSET
        elif isinstance(self.first_listed_date, datetime.date):
            first_listed_date = self.first_listed_date.isoformat()
        else:
            first_listed_date = self.first_listed_date

        last_listed_date: Union[None, Unset, str]
        if isinstance(self.last_listed_date, Unset):
            last_listed_date = UNSET
        elif isinstance(self.last_listed_date, datetime.date):
            last_listed_date = self.last_listed_date.isoformat()
        else:
            last_listed_date = self.last_listed_date

        last_listed_price: Union[None, Unset, float]
        if isinstance(self.last_listed_price, Unset):
            last_listed_price = UNSET
        else:
            last_listed_price = self.last_listed_price

        days_on_market: Union[None, Unset, int]
        if isinstance(self.days_on_market, Unset):
            days_on_market = UNSET
        else:
            days_on_market = self.days_on_market

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if first_listed_date is not UNSET:
            field_dict["firstListedDate"] = first_listed_date
        if last_listed_date is not UNSET:
            field_dict["lastListedDate"] = last_listed_date
        if last_listed_price is not UNSET:
            field_dict["lastListedPrice"] = last_listed_price
        if days_on_market is not UNSET:
            field_dict["daysOnMarket"] = days_on_market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_agency_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_name = _parse_agency_name(d.pop("agencyName", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_first_listed_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_listed_date_type_0 = isoparse(data).date()

                return first_listed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        first_listed_date = _parse_first_listed_date(d.pop("firstListedDate", UNSET))

        def _parse_last_listed_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_listed_date_type_0 = isoparse(data).date()

                return last_listed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        last_listed_date = _parse_last_listed_date(d.pop("lastListedDate", UNSET))

        def _parse_last_listed_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_listed_price = _parse_last_listed_price(d.pop("lastListedPrice", UNSET))

        def _parse_days_on_market(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        days_on_market = _parse_days_on_market(d.pop("daysOnMarket", UNSET))

        property_enrichment_v2_rent_history_listing = cls(
            id=id,
            agency_name=agency_name,
            agency_id=agency_id,
            first_listed_date=first_listed_date,
            last_listed_date=last_listed_date,
            last_listed_price=last_listed_price,
            days_on_market=days_on_market,
        )

        property_enrichment_v2_rent_history_listing.additional_properties = d
        return property_enrichment_v2_rent_history_listing

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
