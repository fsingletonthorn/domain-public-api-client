import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listing_admin_service_v1_model_median_price_data_price_type import (
    DomainListingAdminServiceV1ModelMedianPriceDataPriceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelMedianPriceData")


@_attrs_define
class DomainListingAdminServiceV1ModelMedianPriceData:
    """Information regarding median house/unit price   for the suburb

    Attributes:
        price_type (Union[Unset, DomainListingAdminServiceV1ModelMedianPriceDataPriceType]): Type of property this
            median price is based on .
        suburb (Union[Unset, str]): Name of the suburb median price is based on.
        postcode (Union[Unset, str]): Postcode of the suburb
        median_price (Union[Unset, int]): Median price for the suburb .
        source (Union[Unset, str]): Where the Median Price come from
        source_date_from (Union[Unset, datetime.datetime]): Median Price Source Data From Date
        source_date_to (Union[Unset, datetime.datetime]): Median Price Source Data To Date
        declaration_text (Union[Unset, str]): Declaration text should be provided when no median price data available
    """

    price_type: Union[Unset, DomainListingAdminServiceV1ModelMedianPriceDataPriceType] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    median_price: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    source_date_from: Union[Unset, datetime.datetime] = UNSET
    source_date_to: Union[Unset, datetime.datetime] = UNSET
    declaration_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        suburb = self.suburb

        postcode = self.postcode

        median_price = self.median_price

        source = self.source

        source_date_from: Union[Unset, str] = UNSET
        if not isinstance(self.source_date_from, Unset):
            source_date_from = self.source_date_from.isoformat()

        source_date_to: Union[Unset, str] = UNSET
        if not isinstance(self.source_date_to, Unset):
            source_date_to = self.source_date_to.isoformat()

        declaration_text = self.declaration_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if declaration_text is not UNSET:
            field_dict["declarationText"] = declaration_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _price_type = d.pop("priceType", UNSET)
        price_type: Union[Unset, DomainListingAdminServiceV1ModelMedianPriceDataPriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = DomainListingAdminServiceV1ModelMedianPriceDataPriceType(_price_type)

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        median_price = d.pop("medianPrice", UNSET)

        source = d.pop("source", UNSET)

        _source_date_from = d.pop("sourceDateFrom", UNSET)
        source_date_from: Union[Unset, datetime.datetime]
        if isinstance(_source_date_from, Unset):
            source_date_from = UNSET
        else:
            source_date_from = isoparse(_source_date_from)

        _source_date_to = d.pop("sourceDateTo", UNSET)
        source_date_to: Union[Unset, datetime.datetime]
        if isinstance(_source_date_to, Unset):
            source_date_to = UNSET
        else:
            source_date_to = isoparse(_source_date_to)

        declaration_text = d.pop("declarationText", UNSET)

        domain_listing_admin_service_v1_model_median_price_data = cls(
            price_type=price_type,
            suburb=suburb,
            postcode=postcode,
            median_price=median_price,
            source=source,
            source_date_from=source_date_from,
            source_date_to=source_date_to,
            declaration_text=declaration_text,
        )

        domain_listing_admin_service_v1_model_median_price_data.additional_properties = d
        return domain_listing_admin_service_v1_model_median_price_data

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
