from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyActivityAPIV1PortfolioListPortfoliosItem")


@_attrs_define
class PropertyActivityAPIV1PortfolioListPortfoliosItem:
    """
    Attributes:
        portfolio_id (Union[Unset, str]):  Example: PORTFOLIO_7eedc8e01b2942eaaa396de4b512f6a1.
        property_id_count (Union[Unset, int]): Total number of property ids defined
        gnaf_id_count (Union[Unset, int]): Total number of gnaf ids defined
    """

    portfolio_id: Union[Unset, str] = UNSET
    property_id_count: Union[Unset, int] = UNSET
    gnaf_id_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portfolio_id = self.portfolio_id

        property_id_count = self.property_id_count

        gnaf_id_count = self.gnaf_id_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolio_id is not UNSET:
            field_dict["PortfolioId"] = portfolio_id
        if property_id_count is not UNSET:
            field_dict["PropertyIdCount"] = property_id_count
        if gnaf_id_count is not UNSET:
            field_dict["GnafIdCount"] = gnaf_id_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        portfolio_id = d.pop("PortfolioId", UNSET)

        property_id_count = d.pop("PropertyIdCount", UNSET)

        gnaf_id_count = d.pop("GnafIdCount", UNSET)

        property_activity_apiv1_portfolio_list_portfolios_item = cls(
            portfolio_id=portfolio_id,
            property_id_count=property_id_count,
            gnaf_id_count=gnaf_id_count,
        )

        property_activity_apiv1_portfolio_list_portfolios_item.additional_properties = d
        return property_activity_apiv1_portfolio_list_portfolios_item

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
