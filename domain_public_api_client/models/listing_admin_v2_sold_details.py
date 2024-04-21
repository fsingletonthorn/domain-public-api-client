from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_sold_details_sold_type import ListingAdminV2SoldDetailsSoldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2SoldDetails")


@_attrs_define
class ListingAdminV2SoldDetails:
    """Sold Details

    Attributes:
        sold_type (ListingAdminV2SoldDetailsSoldType): Sold Type
        sold_price (int): Price property was sold for
        display_sold_price (Union[Unset, bool]): Indicates how the price will be displayed for free to the general
            public, default to true if value not provided
    """

    sold_type: ListingAdminV2SoldDetailsSoldType
    sold_price: int
    display_sold_price: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sold_type = self.sold_type.value

        sold_price = self.sold_price

        display_sold_price = self.display_sold_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "soldType": sold_type,
                "soldPrice": sold_price,
            }
        )
        if display_sold_price is not UNSET:
            field_dict["displaySoldPrice"] = display_sold_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sold_type = ListingAdminV2SoldDetailsSoldType(d.pop("soldType"))

        sold_price = d.pop("soldPrice")

        display_sold_price = d.pop("displaySoldPrice", UNSET)

        listing_admin_v2_sold_details = cls(
            sold_type=sold_type,
            sold_price=sold_price,
            display_sold_price=display_sold_price,
        )

        listing_admin_v2_sold_details.additional_properties = d
        return listing_admin_v2_sold_details

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
