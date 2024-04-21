import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listing_admin_service_v1_model_lease_hold_detail_leasehold_price_unit import (
    DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdPriceUnit,
)
from ..models.domain_listing_admin_service_v1_model_lease_hold_detail_leasehold_rent_period import (
    DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelLeaseHoldDetail")


@_attrs_define
class DomainListingAdminServiceV1ModelLeaseHoldDetail:
    """Contains additional details about a business listing

    Attributes:
        leasehold_rent_period (Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod]): Rent
            period for the existing lease, can be: ['perMonth', 'perAnnum']
        leasehold_price_unit (Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdPriceUnit]): Price
            unit for the existing lease, can be:  ['totalAmount', 'perSqm']
        leasehold_term (Union[Unset, int]): Term of existing lease
        leasehold_start (Union[Unset, datetime.datetime]): Start of existing lease
        leasehold_rent (Union[Unset, float]): Rent amount for the existing lease
    """

    leasehold_rent_period: Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod] = UNSET
    leasehold_price_unit: Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdPriceUnit] = UNSET
    leasehold_term: Union[Unset, int] = UNSET
    leasehold_start: Union[Unset, datetime.datetime] = UNSET
    leasehold_rent: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leasehold_rent_period: Union[Unset, str] = UNSET
        if not isinstance(self.leasehold_rent_period, Unset):
            leasehold_rent_period = self.leasehold_rent_period.value

        leasehold_price_unit: Union[Unset, str] = UNSET
        if not isinstance(self.leasehold_price_unit, Unset):
            leasehold_price_unit = self.leasehold_price_unit.value

        leasehold_term = self.leasehold_term

        leasehold_start: Union[Unset, str] = UNSET
        if not isinstance(self.leasehold_start, Unset):
            leasehold_start = self.leasehold_start.isoformat()

        leasehold_rent = self.leasehold_rent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leasehold_rent_period is not UNSET:
            field_dict["leaseholdRentPeriod"] = leasehold_rent_period
        if leasehold_price_unit is not UNSET:
            field_dict["leaseholdPriceUnit"] = leasehold_price_unit
        if leasehold_term is not UNSET:
            field_dict["leaseholdTerm"] = leasehold_term
        if leasehold_start is not UNSET:
            field_dict["leaseholdStart"] = leasehold_start
        if leasehold_rent is not UNSET:
            field_dict["leaseholdRent"] = leasehold_rent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _leasehold_rent_period = d.pop("leaseholdRentPeriod", UNSET)
        leasehold_rent_period: Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod]
        if isinstance(_leasehold_rent_period, Unset):
            leasehold_rent_period = UNSET
        else:
            leasehold_rent_period = DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod(
                _leasehold_rent_period
            )

        _leasehold_price_unit = d.pop("leaseholdPriceUnit", UNSET)
        leasehold_price_unit: Union[Unset, DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdPriceUnit]
        if isinstance(_leasehold_price_unit, Unset):
            leasehold_price_unit = UNSET
        else:
            leasehold_price_unit = DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdPriceUnit(
                _leasehold_price_unit
            )

        leasehold_term = d.pop("leaseholdTerm", UNSET)

        _leasehold_start = d.pop("leaseholdStart", UNSET)
        leasehold_start: Union[Unset, datetime.datetime]
        if isinstance(_leasehold_start, Unset):
            leasehold_start = UNSET
        else:
            leasehold_start = isoparse(_leasehold_start)

        leasehold_rent = d.pop("leaseholdRent", UNSET)

        domain_listing_admin_service_v1_model_lease_hold_detail = cls(
            leasehold_rent_period=leasehold_rent_period,
            leasehold_price_unit=leasehold_price_unit,
            leasehold_term=leasehold_term,
            leasehold_start=leasehold_start,
            leasehold_rent=leasehold_rent,
        )

        domain_listing_admin_service_v1_model_lease_hold_detail.additional_properties = d
        return domain_listing_admin_service_v1_model_lease_hold_detail

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
