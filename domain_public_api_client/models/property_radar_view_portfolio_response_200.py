from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_radar_view_portfolio_response_200_properties import (
        PropertyRadarViewPortfolioResponse200Properties,
    )


T = TypeVar("T", bound="PropertyRadarViewPortfolioResponse200")


@_attrs_define
class PropertyRadarViewPortfolioResponse200:
    """
    Attributes:
        portfolio_id (Union[Unset, str]):  Example: PORTFOLIO_7eedc8e01b2942eaaa396de4b512f6a1.
        properties (Union[Unset, PropertyRadarViewPortfolioResponse200Properties]):
    """

    portfolio_id: Union[Unset, str] = UNSET
    properties: Union[Unset, "PropertyRadarViewPortfolioResponse200Properties"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portfolio_id = self.portfolio_id

        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolio_id is not UNSET:
            field_dict["PortfolioId"] = portfolio_id
        if properties is not UNSET:
            field_dict["Properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_radar_view_portfolio_response_200_properties import (
            PropertyRadarViewPortfolioResponse200Properties,
        )

        d = src_dict.copy()
        portfolio_id = d.pop("PortfolioId", UNSET)

        _properties = d.pop("Properties", UNSET)
        properties: Union[Unset, PropertyRadarViewPortfolioResponse200Properties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PropertyRadarViewPortfolioResponse200Properties.from_dict(_properties)

        property_radar_view_portfolio_response_200 = cls(
            portfolio_id=portfolio_id,
            properties=properties,
        )

        property_radar_view_portfolio_response_200.additional_properties = d
        return property_radar_view_portfolio_response_200

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
