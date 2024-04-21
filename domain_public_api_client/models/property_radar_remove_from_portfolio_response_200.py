from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyRadarRemoveFromPortfolioResponse200")


@_attrs_define
class PropertyRadarRemoveFromPortfolioResponse200:
    """
    Attributes:
        missing_property_ids (Union[Unset, List[str]]):  Example: ['AA-0000-AA', 'BB-000-BB'].
        missing_gnaf_ids (Union[Unset, List[str]]):  Example: ['AAAA000000000', 'BBBB000000000'].
    """

    missing_property_ids: Union[Unset, List[str]] = UNSET
    missing_gnaf_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        missing_property_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.missing_property_ids, Unset):
            missing_property_ids = self.missing_property_ids

        missing_gnaf_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.missing_gnaf_ids, Unset):
            missing_gnaf_ids = self.missing_gnaf_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if missing_property_ids is not UNSET:
            field_dict["MissingPropertyIds"] = missing_property_ids
        if missing_gnaf_ids is not UNSET:
            field_dict["MissingGnafIds"] = missing_gnaf_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        missing_property_ids = cast(List[str], d.pop("MissingPropertyIds", UNSET))

        missing_gnaf_ids = cast(List[str], d.pop("MissingGnafIds", UNSET))

        property_radar_remove_from_portfolio_response_200 = cls(
            missing_property_ids=missing_property_ids,
            missing_gnaf_ids=missing_gnaf_ids,
        )

        property_radar_remove_from_portfolio_response_200.additional_properties = d
        return property_radar_remove_from_portfolio_response_200

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
