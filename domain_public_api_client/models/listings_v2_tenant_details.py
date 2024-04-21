import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2TenantDetails")


@_attrs_define
class ListingsV2TenantDetails:
    """Tenant Details

    Attributes:
        lease_date_variable (Union[None, Unset, bool]): Is tenant lease date variable
        lease_options (Union[None, Unset, str]): Leasing options available to a prospective tenant
        tenant_info_term_of_lease_from (Union[None, Unset, int]): The from range of the tenant's current lease
        tenant_info_term_of_lease_to (Union[None, Unset, int]): The to range of the tenant's current lease
        tenant_name (Union[None, Unset, str]): Name of the current tenant of the property
        tenant_rent_details (Union[None, Unset, str]): Information regarding current rental
        lease_start_date (Union[None, Unset, datetime.datetime]): The date on which the tenants lease began, or is due
            to begin. DateTime is in a local timezone.
        lease_end_date (Union[None, Unset, datetime.datetime]): The date on which the tenants lease is due to end.
            DateTime is in a local timezone.
    """

    lease_date_variable: Union[None, Unset, bool] = UNSET
    lease_options: Union[None, Unset, str] = UNSET
    tenant_info_term_of_lease_from: Union[None, Unset, int] = UNSET
    tenant_info_term_of_lease_to: Union[None, Unset, int] = UNSET
    tenant_name: Union[None, Unset, str] = UNSET
    tenant_rent_details: Union[None, Unset, str] = UNSET
    lease_start_date: Union[None, Unset, datetime.datetime] = UNSET
    lease_end_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lease_date_variable: Union[None, Unset, bool]
        if isinstance(self.lease_date_variable, Unset):
            lease_date_variable = UNSET
        else:
            lease_date_variable = self.lease_date_variable

        lease_options: Union[None, Unset, str]
        if isinstance(self.lease_options, Unset):
            lease_options = UNSET
        else:
            lease_options = self.lease_options

        tenant_info_term_of_lease_from: Union[None, Unset, int]
        if isinstance(self.tenant_info_term_of_lease_from, Unset):
            tenant_info_term_of_lease_from = UNSET
        else:
            tenant_info_term_of_lease_from = self.tenant_info_term_of_lease_from

        tenant_info_term_of_lease_to: Union[None, Unset, int]
        if isinstance(self.tenant_info_term_of_lease_to, Unset):
            tenant_info_term_of_lease_to = UNSET
        else:
            tenant_info_term_of_lease_to = self.tenant_info_term_of_lease_to

        tenant_name: Union[None, Unset, str]
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        tenant_rent_details: Union[None, Unset, str]
        if isinstance(self.tenant_rent_details, Unset):
            tenant_rent_details = UNSET
        else:
            tenant_rent_details = self.tenant_rent_details

        lease_start_date: Union[None, Unset, str]
        if isinstance(self.lease_start_date, Unset):
            lease_start_date = UNSET
        elif isinstance(self.lease_start_date, datetime.datetime):
            lease_start_date = self.lease_start_date.isoformat()
        else:
            lease_start_date = self.lease_start_date

        lease_end_date: Union[None, Unset, str]
        if isinstance(self.lease_end_date, Unset):
            lease_end_date = UNSET
        elif isinstance(self.lease_end_date, datetime.datetime):
            lease_end_date = self.lease_end_date.isoformat()
        else:
            lease_end_date = self.lease_end_date

        field_dict: Dict[str, Any] = {}
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

        def _parse_lease_date_variable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        lease_date_variable = _parse_lease_date_variable(d.pop("leaseDateVariable", UNSET))

        def _parse_lease_options(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lease_options = _parse_lease_options(d.pop("leaseOptions", UNSET))

        def _parse_tenant_info_term_of_lease_from(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tenant_info_term_of_lease_from = _parse_tenant_info_term_of_lease_from(
            d.pop("tenantInfoTermOfLeaseFrom", UNSET)
        )

        def _parse_tenant_info_term_of_lease_to(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tenant_info_term_of_lease_to = _parse_tenant_info_term_of_lease_to(d.pop("tenantInfoTermOfLeaseTo", UNSET))

        def _parse_tenant_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        def _parse_tenant_rent_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tenant_rent_details = _parse_tenant_rent_details(d.pop("tenantRentDetails", UNSET))

        def _parse_lease_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_start_date_type_0 = isoparse(data)

                return lease_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        lease_start_date = _parse_lease_start_date(d.pop("leaseStartDate", UNSET))

        def _parse_lease_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_end_date_type_0 = isoparse(data)

                return lease_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        lease_end_date = _parse_lease_end_date(d.pop("leaseEndDate", UNSET))

        listings_v2_tenant_details = cls(
            lease_date_variable=lease_date_variable,
            lease_options=lease_options,
            tenant_info_term_of_lease_from=tenant_info_term_of_lease_from,
            tenant_info_term_of_lease_to=tenant_info_term_of_lease_to,
            tenant_name=tenant_name,
            tenant_rent_details=tenant_rent_details,
            lease_start_date=lease_start_date,
            lease_end_date=lease_end_date,
        )

        return listings_v2_tenant_details
