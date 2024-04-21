from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_activity_apiv1_portfolio_list_portfolios_item import (
        PropertyActivityAPIV1PortfolioListPortfoliosItem,
    )


T = TypeVar("T", bound="PropertyActivityAPIV1PortfolioList")


@_attrs_define
class PropertyActivityAPIV1PortfolioList:
    """
    Attributes:
        portfolios (Union[Unset, List['PropertyActivityAPIV1PortfolioListPortfoliosItem']]):
    """

    portfolios: Union[Unset, List["PropertyActivityAPIV1PortfolioListPortfoliosItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portfolios: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.portfolios, Unset):
            portfolios = []
            for portfolios_item_data in self.portfolios:
                portfolios_item = portfolios_item_data.to_dict()
                portfolios.append(portfolios_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolios is not UNSET:
            field_dict["Portfolios"] = portfolios

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_activity_apiv1_portfolio_list_portfolios_item import (
            PropertyActivityAPIV1PortfolioListPortfoliosItem,
        )

        d = src_dict.copy()
        portfolios = []
        _portfolios = d.pop("Portfolios", UNSET)
        for portfolios_item_data in _portfolios or []:
            portfolios_item = PropertyActivityAPIV1PortfolioListPortfoliosItem.from_dict(portfolios_item_data)

            portfolios.append(portfolios_item)

        property_activity_apiv1_portfolio_list = cls(
            portfolios=portfolios,
        )

        property_activity_apiv1_portfolio_list.additional_properties = d
        return property_activity_apiv1_portfolio_list

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
