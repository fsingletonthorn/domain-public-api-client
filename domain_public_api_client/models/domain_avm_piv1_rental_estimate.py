from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainAvmPIV1RentalEstimate")


@_attrs_define
class DomainAvmPIV1RentalEstimate:
    """
    Attributes:
        weekly_rent_estimate (Union[None, Unset, int]):
        percent_yield_rent_estimate (Union[None, Unset, float]):
        rental_fsd (Union[None, Unset, float]):
        estimate_date (Union[None, Unset, str]):
        property_type (Union[None, Unset, str]):
    """

    weekly_rent_estimate: Union[None, Unset, int] = UNSET
    percent_yield_rent_estimate: Union[None, Unset, float] = UNSET
    rental_fsd: Union[None, Unset, float] = UNSET
    estimate_date: Union[None, Unset, str] = UNSET
    property_type: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        weekly_rent_estimate: Union[None, Unset, int]
        if isinstance(self.weekly_rent_estimate, Unset):
            weekly_rent_estimate = UNSET
        else:
            weekly_rent_estimate = self.weekly_rent_estimate

        percent_yield_rent_estimate: Union[None, Unset, float]
        if isinstance(self.percent_yield_rent_estimate, Unset):
            percent_yield_rent_estimate = UNSET
        else:
            percent_yield_rent_estimate = self.percent_yield_rent_estimate

        rental_fsd: Union[None, Unset, float]
        if isinstance(self.rental_fsd, Unset):
            rental_fsd = UNSET
        else:
            rental_fsd = self.rental_fsd

        estimate_date: Union[None, Unset, str]
        if isinstance(self.estimate_date, Unset):
            estimate_date = UNSET
        else:
            estimate_date = self.estimate_date

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if weekly_rent_estimate is not UNSET:
            field_dict["weeklyRentEstimate"] = weekly_rent_estimate
        if percent_yield_rent_estimate is not UNSET:
            field_dict["percentYieldRentEstimate"] = percent_yield_rent_estimate
        if rental_fsd is not UNSET:
            field_dict["rentalFsd"] = rental_fsd
        if estimate_date is not UNSET:
            field_dict["estimateDate"] = estimate_date
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_weekly_rent_estimate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        weekly_rent_estimate = _parse_weekly_rent_estimate(d.pop("weeklyRentEstimate", UNSET))

        def _parse_percent_yield_rent_estimate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percent_yield_rent_estimate = _parse_percent_yield_rent_estimate(d.pop("percentYieldRentEstimate", UNSET))

        def _parse_rental_fsd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rental_fsd = _parse_rental_fsd(d.pop("rentalFsd", UNSET))

        def _parse_estimate_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        estimate_date = _parse_estimate_date(d.pop("estimateDate", UNSET))

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        domain_avm_piv1_rental_estimate = cls(
            weekly_rent_estimate=weekly_rent_estimate,
            percent_yield_rent_estimate=percent_yield_rent_estimate,
            rental_fsd=rental_fsd,
            estimate_date=estimate_date,
            property_type=property_type,
        )

        return domain_avm_piv1_rental_estimate
