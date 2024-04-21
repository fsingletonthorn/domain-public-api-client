from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details_sale_method import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetailsSaleMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tenant_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tender_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails,
    )


T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails:
    """
    Attributes:
        sale_method (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetailsSaleMethod]):
        sold_details (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails]):
        auction_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails]):
        tender_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails]):
        tenant_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails]):
        annual_return (Union[Unset, int]):
        sale_terms (Union[Unset, str]):
    """

    sale_method: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetailsSaleMethod
    ] = UNSET
    sold_details: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails"] = (
        UNSET
    )
    auction_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails"
    ] = UNSET
    tender_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails"
    ] = UNSET
    tenant_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails"
    ] = UNSET
    annual_return: Union[Unset, int] = UNSET
    sale_terms: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sale_method: Union[Unset, str] = UNSET
        if not isinstance(self.sale_method, Unset):
            sale_method = self.sale_method.value

        sold_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sold_details, Unset):
            sold_details = self.sold_details.to_dict()

        auction_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction_details, Unset):
            auction_details = self.auction_details.to_dict()

        tender_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tender_details, Unset):
            tender_details = self.tender_details.to_dict()

        tenant_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tenant_details, Unset):
            tenant_details = self.tenant_details.to_dict()

        annual_return = self.annual_return

        sale_terms = self.sale_terms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sale_method is not UNSET:
            field_dict["saleMethod"] = sale_method
        if sold_details is not UNSET:
            field_dict["soldDetails"] = sold_details
        if auction_details is not UNSET:
            field_dict["auctionDetails"] = auction_details
        if tender_details is not UNSET:
            field_dict["tenderDetails"] = tender_details
        if tenant_details is not UNSET:
            field_dict["tenantDetails"] = tenant_details
        if annual_return is not UNSET:
            field_dict["annualReturn"] = annual_return
        if sale_terms is not UNSET:
            field_dict["saleTerms"] = sale_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tenant_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tender_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails,
        )

        d = src_dict.copy()
        _sale_method = d.pop("saleMethod", UNSET)
        sale_method: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetailsSaleMethod
        ]
        if isinstance(_sale_method, Unset):
            sale_method = UNSET
        else:
            sale_method = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetailsSaleMethod(
                _sale_method
            )

        _sold_details = d.pop("soldDetails", UNSET)
        sold_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails]
        if isinstance(_sold_details, Unset):
            sold_details = UNSET
        else:
            sold_details = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.from_dict(
                _sold_details
            )

        _auction_details = d.pop("auctionDetails", UNSET)
        auction_details: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails
        ]
        if isinstance(_auction_details, Unset):
            auction_details = UNSET
        else:
            auction_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails.from_dict(
                    _auction_details
                )
            )

        _tender_details = d.pop("tenderDetails", UNSET)
        tender_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails]
        if isinstance(_tender_details, Unset):
            tender_details = UNSET
        else:
            tender_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails.from_dict(
                    _tender_details
                )
            )

        _tenant_details = d.pop("tenantDetails", UNSET)
        tenant_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails]
        if isinstance(_tenant_details, Unset):
            tenant_details = UNSET
        else:
            tenant_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails.from_dict(
                    _tenant_details
                )
            )

        annual_return = d.pop("annualReturn", UNSET)

        sale_terms = d.pop("saleTerms", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details = cls(
            sale_method=sale_method,
            sold_details=sold_details,
            auction_details=auction_details,
            tender_details=tender_details,
            tenant_details=tenant_details,
            annual_return=annual_return,
            sale_terms=sale_terms,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details

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
