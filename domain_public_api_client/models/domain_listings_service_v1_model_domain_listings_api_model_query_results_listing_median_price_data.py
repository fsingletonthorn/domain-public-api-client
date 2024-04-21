from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data_price_type import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData:
    """
    Attributes:
        price_type (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType]):
        suburb (Union[Unset, str]):
        postcode (Union[Unset, str]):
        median_price (Union[Unset, int]):
        source (Union[Unset, str]):
        source_date_from (Union[Unset, str]):
        source_date_to (Union[Unset, str]):
        source_collection_date (Union[Unset, str]):
    """

    price_type: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType
    ] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    median_price: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    source_date_from: Union[Unset, str] = UNSET
    source_date_to: Union[Unset, str] = UNSET
    source_collection_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        suburb = self.suburb

        postcode = self.postcode

        median_price = self.median_price

        source = self.source

        source_date_from = self.source_date_from

        source_date_to = self.source_date_to

        source_collection_date = self.source_collection_date

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
        if source_collection_date is not UNSET:
            field_dict["sourceCollectionDate"] = source_collection_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _price_type = d.pop("priceType", UNSET)
        price_type: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType
        ]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType(
                _price_type
            )

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        median_price = d.pop("medianPrice", UNSET)

        source = d.pop("source", UNSET)

        source_date_from = d.pop("sourceDateFrom", UNSET)

        source_date_to = d.pop("sourceDateTo", UNSET)

        source_collection_date = d.pop("sourceCollectionDate", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data = cls(
            price_type=price_type,
            suburb=suburb,
            postcode=postcode,
            median_price=median_price,
            source=source,
            source_date_from=source_date_from,
            source_date_to=source_date_to,
            source_collection_date=source_collection_date,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data

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
