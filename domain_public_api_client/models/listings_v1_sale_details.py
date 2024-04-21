from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v1_sale_details_sale_method import ListingsV1SaleDetailsSaleMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v1_auction_details import ListingsV1AuctionDetails
    from ..models.listings_v1_sold_details import ListingsV1SoldDetails
    from ..models.listings_v1_tenant_details import ListingsV1TenantDetails
    from ..models.listings_v1_tender_details import ListingsV1TenderDetails


T = TypeVar("T", bound="ListingsV1SaleDetails")


@_attrs_define
class ListingsV1SaleDetails:
    """The sale detail's of the listing in case of it being for sale or sold

    Attributes:
        sale_method (Union[Unset, ListingsV1SaleDetailsSaleMethod]): Gets or Sets SaleMethod
        sold_details (Union[Unset, ListingsV1SoldDetails]): Sold details in the case of the listing being sold.
        auction_details (Union[Unset, ListingsV1AuctionDetails]): The detail's of the auction in case of a listing for
            sale being auctioned or sold by auction
        tender_details (Union[Unset, ListingsV1TenderDetails]): Tender details
        tenant_details (Union[Unset, ListingsV1TenantDetails]): Tenant Details
        annual_return (Union[None, Unset, int]): Integer value of percentage return on this property or business
        sale_terms (Union[None, Unset, str]): Information relating to aspects of the sale, such as required deposit,
            settlement time
    """

    sale_method: Union[Unset, ListingsV1SaleDetailsSaleMethod] = UNSET
    sold_details: Union[Unset, "ListingsV1SoldDetails"] = UNSET
    auction_details: Union[Unset, "ListingsV1AuctionDetails"] = UNSET
    tender_details: Union[Unset, "ListingsV1TenderDetails"] = UNSET
    tenant_details: Union[Unset, "ListingsV1TenantDetails"] = UNSET
    annual_return: Union[None, Unset, int] = UNSET
    sale_terms: Union[None, Unset, str] = UNSET

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

        annual_return: Union[None, Unset, int]
        if isinstance(self.annual_return, Unset):
            annual_return = UNSET
        else:
            annual_return = self.annual_return

        sale_terms: Union[None, Unset, str]
        if isinstance(self.sale_terms, Unset):
            sale_terms = UNSET
        else:
            sale_terms = self.sale_terms

        field_dict: Dict[str, Any] = {}
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
        from ..models.listings_v1_auction_details import ListingsV1AuctionDetails
        from ..models.listings_v1_sold_details import ListingsV1SoldDetails
        from ..models.listings_v1_tenant_details import ListingsV1TenantDetails
        from ..models.listings_v1_tender_details import ListingsV1TenderDetails

        d = src_dict.copy()
        _sale_method = d.pop("saleMethod", UNSET)
        sale_method: Union[Unset, ListingsV1SaleDetailsSaleMethod]
        if isinstance(_sale_method, Unset):
            sale_method = UNSET
        else:
            sale_method = ListingsV1SaleDetailsSaleMethod(_sale_method)

        _sold_details = d.pop("soldDetails", UNSET)
        sold_details: Union[Unset, ListingsV1SoldDetails]
        if isinstance(_sold_details, Unset):
            sold_details = UNSET
        else:
            sold_details = ListingsV1SoldDetails.from_dict(_sold_details)

        _auction_details = d.pop("auctionDetails", UNSET)
        auction_details: Union[Unset, ListingsV1AuctionDetails]
        if isinstance(_auction_details, Unset):
            auction_details = UNSET
        else:
            auction_details = ListingsV1AuctionDetails.from_dict(_auction_details)

        _tender_details = d.pop("tenderDetails", UNSET)
        tender_details: Union[Unset, ListingsV1TenderDetails]
        if isinstance(_tender_details, Unset):
            tender_details = UNSET
        else:
            tender_details = ListingsV1TenderDetails.from_dict(_tender_details)

        _tenant_details = d.pop("tenantDetails", UNSET)
        tenant_details: Union[Unset, ListingsV1TenantDetails]
        if isinstance(_tenant_details, Unset):
            tenant_details = UNSET
        else:
            tenant_details = ListingsV1TenantDetails.from_dict(_tenant_details)

        def _parse_annual_return(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        annual_return = _parse_annual_return(d.pop("annualReturn", UNSET))

        def _parse_sale_terms(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sale_terms = _parse_sale_terms(d.pop("saleTerms", UNSET))

        listings_v1_sale_details = cls(
            sale_method=sale_method,
            sold_details=sold_details,
            auction_details=auction_details,
            tender_details=tender_details,
            tenant_details=tenant_details,
            annual_return=annual_return,
            sale_terms=sale_terms,
        )

        return listings_v1_sale_details
