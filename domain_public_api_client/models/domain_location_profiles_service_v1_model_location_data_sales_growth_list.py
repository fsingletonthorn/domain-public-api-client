from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList")


@_attrs_define
class DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList:
    """
    Attributes:
        median_sold_price (Union[Unset, float]):
        annual_growth (Union[Unset, float]):
        number_sold (Union[Unset, int]):
        year (Union[Unset, int]):
    """

    median_sold_price: Union[Unset, float] = UNSET
    annual_growth: Union[Unset, float] = UNSET
    number_sold: Union[Unset, int] = UNSET
    year: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        median_sold_price = self.median_sold_price

        annual_growth = self.annual_growth

        number_sold = self.number_sold

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if median_sold_price is not UNSET:
            field_dict["medianSoldPrice"] = median_sold_price
        if annual_growth is not UNSET:
            field_dict["annualGrowth"] = annual_growth
        if number_sold is not UNSET:
            field_dict["numberSold"] = number_sold
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        median_sold_price = d.pop("medianSoldPrice", UNSET)

        annual_growth = d.pop("annualGrowth", UNSET)

        number_sold = d.pop("numberSold", UNSET)

        year = d.pop("year", UNSET)

        domain_location_profiles_service_v1_model_location_data_sales_growth_list = cls(
            median_sold_price=median_sold_price,
            annual_growth=annual_growth,
            number_sold=number_sold,
            year=year,
        )

        domain_location_profiles_service_v1_model_location_data_sales_growth_list.additional_properties = d
        return domain_location_profiles_service_v1_model_location_data_sales_growth_list

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
