import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Tenant")


@_attrs_define
class ListingAdminV2Tenant:
    """Tenant Information

    Attributes:
        lease_start (Union[Unset, datetime.datetime]): The date on which the tenants lease began, or is due to begin.
        lease_end (Union[Unset, datetime.datetime]): The date on which the tenants lease is due to end
        name (Union[Unset, str]): Name of the current tenant of the property, up to 100 characters
        rental_details (Union[Unset, str]): Information regarding current rental, up to 100 characters
        lease_options (Union[Unset, str]): Leasing options available to a prospective tenant, up to 100 characters
        tenant_info_term_of_lease_from (Union[Unset, int]): The from range of the tenant's current lease
        tenant_info_term_of_lease_to (Union[Unset, int]): The to range of the tenant's current lease
        lease_date_variable (Union[Unset, bool]): Is tenant lease date variable
    """

    lease_start: Union[Unset, datetime.datetime] = UNSET
    lease_end: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    rental_details: Union[Unset, str] = UNSET
    lease_options: Union[Unset, str] = UNSET
    tenant_info_term_of_lease_from: Union[Unset, int] = UNSET
    tenant_info_term_of_lease_to: Union[Unset, int] = UNSET
    lease_date_variable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lease_start: Union[Unset, str] = UNSET
        if not isinstance(self.lease_start, Unset):
            lease_start = self.lease_start.isoformat()

        lease_end: Union[Unset, str] = UNSET
        if not isinstance(self.lease_end, Unset):
            lease_end = self.lease_end.isoformat()

        name = self.name

        rental_details = self.rental_details

        lease_options = self.lease_options

        tenant_info_term_of_lease_from = self.tenant_info_term_of_lease_from

        tenant_info_term_of_lease_to = self.tenant_info_term_of_lease_to

        lease_date_variable = self.lease_date_variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease_start is not UNSET:
            field_dict["leaseStart"] = lease_start
        if lease_end is not UNSET:
            field_dict["leaseEnd"] = lease_end
        if name is not UNSET:
            field_dict["name"] = name
        if rental_details is not UNSET:
            field_dict["rentalDetails"] = rental_details
        if lease_options is not UNSET:
            field_dict["leaseOptions"] = lease_options
        if tenant_info_term_of_lease_from is not UNSET:
            field_dict["tenantInfoTermOfLeaseFrom"] = tenant_info_term_of_lease_from
        if tenant_info_term_of_lease_to is not UNSET:
            field_dict["tenantInfoTermOfLeaseTo"] = tenant_info_term_of_lease_to
        if lease_date_variable is not UNSET:
            field_dict["leaseDateVariable"] = lease_date_variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _lease_start = d.pop("leaseStart", UNSET)
        lease_start: Union[Unset, datetime.datetime]
        if isinstance(_lease_start, Unset):
            lease_start = UNSET
        else:
            lease_start = isoparse(_lease_start)

        _lease_end = d.pop("leaseEnd", UNSET)
        lease_end: Union[Unset, datetime.datetime]
        if isinstance(_lease_end, Unset):
            lease_end = UNSET
        else:
            lease_end = isoparse(_lease_end)

        name = d.pop("name", UNSET)

        rental_details = d.pop("rentalDetails", UNSET)

        lease_options = d.pop("leaseOptions", UNSET)

        tenant_info_term_of_lease_from = d.pop("tenantInfoTermOfLeaseFrom", UNSET)

        tenant_info_term_of_lease_to = d.pop("tenantInfoTermOfLeaseTo", UNSET)

        lease_date_variable = d.pop("leaseDateVariable", UNSET)

        listing_admin_v2_tenant = cls(
            lease_start=lease_start,
            lease_end=lease_end,
            name=name,
            rental_details=rental_details,
            lease_options=lease_options,
            tenant_info_term_of_lease_from=tenant_info_term_of_lease_from,
            tenant_info_term_of_lease_to=tenant_info_term_of_lease_to,
            lease_date_variable=lease_date_variable,
        )

        listing_admin_v2_tenant.additional_properties = d
        return listing_admin_v2_tenant

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
