from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v2_past_sale_data import ListingsV2PastSaleData


T = TypeVar("T", bound="ListingsV2ComparableData")


@_attrs_define
class ListingsV2ComparableData:
    """Information regarding the past comparable property sales that influenced the setting of the estimation price

    Attributes:
        comparable_property (Union[List['ListingsV2PastSaleData'], None, Unset]): Comparable properties that are of a
            similar standard or condition to the property for sale
        declaration_text (Union[None, Unset, str]): Text description if there are less than three comparable sales
            available
    """

    comparable_property: Union[List["ListingsV2PastSaleData"], None, Unset] = UNSET
    declaration_text: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        comparable_property: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.comparable_property, Unset):
            comparable_property = UNSET
        elif isinstance(self.comparable_property, list):
            comparable_property = []
            for comparable_property_type_0_item_data in self.comparable_property:
                comparable_property_type_0_item = comparable_property_type_0_item_data.to_dict()
                comparable_property.append(comparable_property_type_0_item)

        else:
            comparable_property = self.comparable_property

        declaration_text: Union[None, Unset, str]
        if isinstance(self.declaration_text, Unset):
            declaration_text = UNSET
        else:
            declaration_text = self.declaration_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if comparable_property is not UNSET:
            field_dict["comparableProperty"] = comparable_property
        if declaration_text is not UNSET:
            field_dict["declarationText"] = declaration_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_v2_past_sale_data import ListingsV2PastSaleData

        d = src_dict.copy()

        def _parse_comparable_property(data: object) -> Union[List["ListingsV2PastSaleData"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                comparable_property_type_0 = []
                _comparable_property_type_0 = data
                for comparable_property_type_0_item_data in _comparable_property_type_0:
                    comparable_property_type_0_item = ListingsV2PastSaleData.from_dict(
                        comparable_property_type_0_item_data
                    )

                    comparable_property_type_0.append(comparable_property_type_0_item)

                return comparable_property_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV2PastSaleData"], None, Unset], data)

        comparable_property = _parse_comparable_property(d.pop("comparableProperty", UNSET))

        def _parse_declaration_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        declaration_text = _parse_declaration_text(d.pop("declarationText", UNSET))

        listings_v2_comparable_data = cls(
            comparable_property=comparable_property,
            declaration_text=declaration_text,
        )

        return listings_v2_comparable_data
