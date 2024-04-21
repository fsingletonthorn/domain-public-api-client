import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenantDetails:
    """
    Attributes:
        lease_date_variable (Union[Unset, bool]):
        lease_options (Union[Unset, str]):
        tenant_info_term_of_lease_from (Union[Unset, int]):
        tenant_info_term_of_lease_to (Union[Unset, int]):
        tenant_name (Union[Unset, str]):
        tenant_rent_details (Union[Unset, str]):
        lease_start_date (Union[Unset, datetime.datetime]):
        lease_end_date (Union[Unset, datetime.datetime]):
    """

    lease_date_variable: Union[Unset, bool] = UNSET
    lease_options: Union[Unset, str] = UNSET
    tenant_info_term_of_lease_from: Union[Unset, int] = UNSET
    tenant_info_term_of_lease_to: Union[Unset, int] = UNSET
    tenant_name: Union[Unset, str] = UNSET
    tenant_rent_details: Union[Unset, str] = UNSET
    lease_start_date: Union[Unset, datetime.datetime] = UNSET
    lease_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lease_date_variable = self.lease_date_variable

        lease_options = self.lease_options

        tenant_info_term_of_lease_from = self.tenant_info_term_of_lease_from

        tenant_info_term_of_lease_to = self.tenant_info_term_of_lease_to

        tenant_name = self.tenant_name

        tenant_rent_details = self.tenant_rent_details

        lease_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.lease_start_date, Unset):
            lease_start_date = self.lease_start_date.isoformat()

        lease_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.lease_end_date, Unset):
            lease_end_date = self.lease_end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease_date_variable is not UNSET:
            field_dict["leaseDateVariable"] = lease_date_variable
        if lease_options is not UNSET:
            field_dict["leaseOptions"] = lease_options
        if tenant_info_term_of_lease_from is not UNSET:
            field_dict["tenantInfoTermOfLeaseFrom"] = tenant_info_term_of_lease_from
        if tenant_info_term_of_lease_to is not UNSET:
            field_dict["tenantInfoTermOfLeaseTo"] = tenant_info_term_of_lease_to
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if tenant_rent_details is not UNSET:
            field_dict["tenantRentDetails"] = tenant_rent_details
        if lease_start_date is not UNSET:
            field_dict["leaseStartDate"] = lease_start_date
        if lease_end_date is not UNSET:
            field_dict["leaseEndDate"] = lease_end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lease_date_variable = d.pop("leaseDateVariable", UNSET)

        lease_options = d.pop("leaseOptions", UNSET)

        tenant_info_term_of_lease_from = d.pop("tenantInfoTermOfLeaseFrom", UNSET)

        tenant_info_term_of_lease_to = d.pop("tenantInfoTermOfLeaseTo", UNSET)

        tenant_name = d.pop("tenantName", UNSET)

        tenant_rent_details = d.pop("tenantRentDetails", UNSET)

        _lease_start_date = d.pop("leaseStartDate", UNSET)
        lease_start_date: Union[Unset, datetime.datetime]
        if isinstance(_lease_start_date, Unset):
            lease_start_date = UNSET
        else:
            lease_start_date = isoparse(_lease_start_date)

        _lease_end_date = d.pop("leaseEndDate", UNSET)
        lease_end_date: Union[Unset, datetime.datetime]
        if isinstance(_lease_end_date, Unset):
            lease_end_date = UNSET
        else:
            lease_end_date = isoparse(_lease_end_date)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tenant_details = cls(
            lease_date_variable=lease_date_variable,
            lease_options=lease_options,
            tenant_info_term_of_lease_from=tenant_info_term_of_lease_from,
            tenant_info_term_of_lease_to=tenant_info_term_of_lease_to,
            tenant_name=tenant_name,
            tenant_rent_details=tenant_rent_details,
            lease_start_date=lease_start_date,
            lease_end_date=lease_end_date,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tenant_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tenant_details

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
