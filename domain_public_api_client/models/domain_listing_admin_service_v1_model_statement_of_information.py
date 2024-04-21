from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_basic_price import DomainListingAdminServiceV1ModelBasicPrice
    from ..models.domain_listing_admin_service_v1_model_comparable_data import (
        DomainListingAdminServiceV1ModelComparableData,
    )
    from ..models.domain_listing_admin_service_v1_model_median_price_data import (
        DomainListingAdminServiceV1ModelMedianPriceData,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelStatementOfInformation")


@_attrs_define
class DomainListingAdminServiceV1ModelStatementOfInformation:
    """Statement of Information  Regarding sale listing

    Attributes:
        estimated_price (Union[Unset, DomainListingAdminServiceV1ModelBasicPrice]): Basic price information
        comparable_data (Union[Unset, DomainListingAdminServiceV1ModelComparableData]): Information regarding past
            comparable   property sales that influenced the setting of teh estimationPrice
        suburb_median_price (Union[Unset, DomainListingAdminServiceV1ModelMedianPriceData]): Information regarding
            median house/unit price   for the suburb
        documentation_url (Union[Unset, str]): Link to the statement of information documentation file.  Must be a PDF
            file.  File should be less than 10 MB in size  The Statement of Information must be updated if there is a change
            in the indicative selling price.
    """

    estimated_price: Union[Unset, "DomainListingAdminServiceV1ModelBasicPrice"] = UNSET
    comparable_data: Union[Unset, "DomainListingAdminServiceV1ModelComparableData"] = UNSET
    suburb_median_price: Union[Unset, "DomainListingAdminServiceV1ModelMedianPriceData"] = UNSET
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
        from ..models.domain_listing_admin_service_v1_model_basic_price import (
            DomainListingAdminServiceV1ModelBasicPrice,
        )
        from ..models.domain_listing_admin_service_v1_model_comparable_data import (
            DomainListingAdminServiceV1ModelComparableData,
        )
        from ..models.domain_listing_admin_service_v1_model_median_price_data import (
            DomainListingAdminServiceV1ModelMedianPriceData,
        )

        d = src_dict.copy()
        _estimated_price = d.pop("estimatedPrice", UNSET)
        estimated_price: Union[Unset, DomainListingAdminServiceV1ModelBasicPrice]
        if isinstance(_estimated_price, Unset):
            estimated_price = UNSET
        else:
            estimated_price = DomainListingAdminServiceV1ModelBasicPrice.from_dict(_estimated_price)

        _comparable_data = d.pop("comparableData", UNSET)
        comparable_data: Union[Unset, DomainListingAdminServiceV1ModelComparableData]
        if isinstance(_comparable_data, Unset):
            comparable_data = UNSET
        else:
            comparable_data = DomainListingAdminServiceV1ModelComparableData.from_dict(_comparable_data)

        _suburb_median_price = d.pop("suburbMedianPrice", UNSET)
        suburb_median_price: Union[Unset, DomainListingAdminServiceV1ModelMedianPriceData]
        if isinstance(_suburb_median_price, Unset):
            suburb_median_price = UNSET
        else:
            suburb_median_price = DomainListingAdminServiceV1ModelMedianPriceData.from_dict(_suburb_median_price)

        documentation_url = d.pop("documentationUrl", UNSET)

        domain_listing_admin_service_v1_model_statement_of_information = cls(
            estimated_price=estimated_price,
            comparable_data=comparable_data,
            suburb_median_price=suburb_median_price,
            documentation_url=documentation_url,
        )

        domain_listing_admin_service_v1_model_statement_of_information.additional_properties = d
        return domain_listing_admin_service_v1_model_statement_of_information

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
