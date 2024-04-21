from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_radar_create_portfolio_body_type_1_empty import PropertyRadarCreatePortfolioBodyType1Empty


T = TypeVar("T", bound="PropertyRadarCreatePortfolioBodyType1")


@_attrs_define
class PropertyRadarCreatePortfolioBodyType1:
    """
    Attributes:
        empty (Union[Unset, PropertyRadarCreatePortfolioBodyType1Empty]): Create an empty portfolio
    """

    empty: Union[Unset, "PropertyRadarCreatePortfolioBodyType1Empty"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        empty: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.empty, Unset):
            empty = self.empty.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_radar_create_portfolio_body_type_1_empty import (
            PropertyRadarCreatePortfolioBodyType1Empty,
        )

        d = src_dict.copy()
        _empty = d.pop("empty", UNSET)
        empty: Union[Unset, PropertyRadarCreatePortfolioBodyType1Empty]
        if isinstance(_empty, Unset):
            empty = UNSET
        else:
            empty = PropertyRadarCreatePortfolioBodyType1Empty.from_dict(_empty)

        property_radar_create_portfolio_body_type_1 = cls(
            empty=empty,
        )

        return property_radar_create_portfolio_body_type_1
