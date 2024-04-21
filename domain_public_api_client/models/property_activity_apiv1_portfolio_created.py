from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyActivityAPIV1PortfolioCreated")


@_attrs_define
class PropertyActivityAPIV1PortfolioCreated:
    """
    Attributes:
        portfolio_id (Union[Unset, str]): Unique ID for the portfolio Example:
            PORTFOLIO_7eedc8e01b2942eaaa396de4b512f6a1.
    """

    portfolio_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portfolio_id = self.portfolio_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolio_id is not UNSET:
            field_dict["PortfolioId"] = portfolio_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        portfolio_id = d.pop("PortfolioId", UNSET)

        property_activity_apiv1_portfolio_created = cls(
            portfolio_id=portfolio_id,
        )

        property_activity_apiv1_portfolio_created.additional_properties = d
        return property_activity_apiv1_portfolio_created

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
