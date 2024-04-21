from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListingAdminV2SaleInfo")


@_attrs_define
class ListingAdminV2SaleInfo:
    """Contains details about a business sales info

    Attributes:
        annual_sales (float): Annual sales amount for the business
        annual_profit (float): Annual profit amount for the business
        stock_value (float): Stock value of the business
    """

    annual_sales: float
    annual_profit: float
    stock_value: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annual_sales = self.annual_sales

        annual_profit = self.annual_profit

        stock_value = self.stock_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annualSales": annual_sales,
                "annualProfit": annual_profit,
                "stockValue": stock_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        annual_sales = d.pop("annualSales")

        annual_profit = d.pop("annualProfit")

        stock_value = d.pop("stockValue")

        listing_admin_v2_sale_info = cls(
            annual_sales=annual_sales,
            annual_profit=annual_profit,
            stock_value=stock_value,
        )

        listing_admin_v2_sale_info.additional_properties = d
        return listing_admin_v2_sale_info

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
