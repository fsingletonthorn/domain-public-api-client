from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelSaleInfo")


@_attrs_define
class DomainListingAdminServiceV1ModelSaleInfo:
    """Contains details about a business sales info

    Attributes:
        annual_sales (Union[Unset, float]): Annual sales amount for the business
        annual_profit (Union[Unset, float]): Annual profit amount for the business
        stock_value (Union[Unset, float]): Stock value of the business
    """

    annual_sales: Union[Unset, float] = UNSET
    annual_profit: Union[Unset, float] = UNSET
    stock_value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annual_sales = self.annual_sales

        annual_profit = self.annual_profit

        stock_value = self.stock_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annual_sales is not UNSET:
            field_dict["annualSales"] = annual_sales
        if annual_profit is not UNSET:
            field_dict["annualProfit"] = annual_profit
        if stock_value is not UNSET:
            field_dict["stockValue"] = stock_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        annual_sales = d.pop("annualSales", UNSET)

        annual_profit = d.pop("annualProfit", UNSET)

        stock_value = d.pop("stockValue", UNSET)

        domain_listing_admin_service_v1_model_sale_info = cls(
            annual_sales=annual_sales,
            annual_profit=annual_profit,
            stock_value=stock_value,
        )

        domain_listing_admin_service_v1_model_sale_info.additional_properties = d
        return domain_listing_admin_service_v1_model_sale_info

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
