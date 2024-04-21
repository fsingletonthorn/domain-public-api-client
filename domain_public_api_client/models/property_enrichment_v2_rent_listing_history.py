from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2RentListingHistory")


@_attrs_define
class PropertyEnrichmentV2RentListingHistory:
    """property listing history object

    Attributes:
        id (Union[Unset, str]):
        agency_id (Union[None, Unset, str]):
        agency_name (Union[None, Unset, str]):
        first_listed_date (Union[None, Unset, str]):
        last_listed_date (Union[None, Unset, str]):
        listed_price (Union[None, Unset, str]):
        days_on_market (Union[None, Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    agency_id: Union[None, Unset, str] = UNSET
    agency_name: Union[None, Unset, str] = UNSET
    first_listed_date: Union[None, Unset, str] = UNSET
    last_listed_date: Union[None, Unset, str] = UNSET
    listed_price: Union[None, Unset, str] = UNSET
    days_on_market: Union[None, Unset, int] = UNSET

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

        property_enrichment_v2_rent_listing_history = cls(
            id=id,
            agency_id=agency_id,
            agency_name=agency_name,
            first_listed_date=first_listed_date,
            last_listed_date=last_listed_date,
            listed_price=listed_price,
            days_on_market=days_on_market,
        )

        return property_enrichment_v2_rent_listing_history
