from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DemographicsV2DemographicsItem")


@_attrs_define
class DemographicsV2DemographicsItem:
    """DemographicsItemModel

    Attributes:
        label (Union[None, Unset, str]): Gets or Sets Label
        value (Union[None, Unset, int]): Gets or Sets Value
        composition (Union[None, Unset, str]): Gets or Sets Composition
    """

    label: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, int] = UNSET
    composition: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        value: Union[None, Unset, int]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        composition: Union[None, Unset, str]
        if isinstance(self.composition, Unset):
            composition = UNSET
        else:
            composition = self.composition

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value
        if composition is not UNSET:
            field_dict["composition"] = composition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_composition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        composition = _parse_composition(d.pop("composition", UNSET))

        demographics_v2_demographics_item = cls(
            label=label,
            value=value,
            composition=composition,
        )

        return demographics_v2_demographics_item
