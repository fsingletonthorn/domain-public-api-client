from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_basic_price import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_comparable_data import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData,
    )


T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation:
    """
    Attributes:
        estimated_price (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice]):
        comparable_data (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData]):
        suburb_median_price (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData]):
        documentation_url (Union[Unset, str]):
    """

    estimated_price: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice"] = (
        UNSET
    )
    comparable_data: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData"
    ] = UNSET
    suburb_median_price: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData"
    ] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        estimated_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_price, Unset):
            estimated_price = self.estimated_price.to_dict()

        comparable_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comparable_data, Unset):
            comparable_data = self.comparable_data.to_dict()

        suburb_median_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suburb_median_price, Unset):
            suburb_median_price = self.suburb_median_price.to_dict()

        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_price is not UNSET:
            field_dict["estimatedPrice"] = estimated_price
        if comparable_data is not UNSET:
            field_dict["comparableData"] = comparable_data
        if suburb_median_price is not UNSET:
            field_dict["suburbMedianPrice"] = suburb_median_price
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_basic_price import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_comparable_data import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_median_price_data import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData,
        )

        d = src_dict.copy()
        _estimated_price = d.pop("estimatedPrice", UNSET)
        estimated_price: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice]
        if isinstance(_estimated_price, Unset):
            estimated_price = UNSET
        else:
            estimated_price = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingBasicPrice.from_dict(
                _estimated_price
            )

        _comparable_data = d.pop("comparableData", UNSET)
        comparable_data: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData
        ]
        if isinstance(_comparable_data, Unset):
            comparable_data = UNSET
        else:
            comparable_data = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData.from_dict(
                    _comparable_data
                )
            )

        _suburb_median_price = d.pop("suburbMedianPrice", UNSET)
        suburb_median_price: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData
        ]
        if isinstance(_suburb_median_price, Unset):
            suburb_median_price = UNSET
        else:
            suburb_median_price = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.from_dict(
                    _suburb_median_price
                )
            )

        documentation_url = d.pop("documentationUrl", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_statement_of_information = cls(
            estimated_price=estimated_price,
            comparable_data=comparable_data,
            suburb_median_price=suburb_median_price,
            documentation_url=documentation_url,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_statement_of_information.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_statement_of_information

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
