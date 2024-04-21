from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyRadarViewPortfolioResponse200Properties")


@_attrs_define
class PropertyRadarViewPortfolioResponse200Properties:
    """
    Attributes:
        property_ids (Union[Unset, List[str]]):  Example: ['AB-2872-NY', 'RF-8884-AK'].
        gnaf_ids (Union[Unset, List[str]]):  Example: ['GAVIC419677979', 'GANSW710292212'].
    """

    property_ids: Union[Unset, List[str]] = UNSET
    gnaf_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_ids, Unset):
            property_ids = self.property_ids

        gnaf_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.gnaf_ids, Unset):
            gnaf_ids = self.gnaf_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ids is not UNSET:
            field_dict["PropertyIds"] = property_ids
        if gnaf_ids is not UNSET:
            field_dict["GnafIds"] = gnaf_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_ids = cast(List[str], d.pop("PropertyIds", UNSET))

        gnaf_ids = cast(List[str], d.pop("GnafIds", UNSET))

        property_radar_view_portfolio_response_200_properties = cls(
            property_ids=property_ids,
            gnaf_ids=gnaf_ids,
        )

        property_radar_view_portfolio_response_200_properties.additional_properties = d
        return property_radar_view_portfolio_response_200_properties

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
