from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1BasicPrice")


@_attrs_define
class ListingsV1BasicPrice:
    """Basic price information

    Attributes:
        from_ (Union[None, Unset, int]): Lowest price the property is expected to sell/rent for to set search price.
        to (Union[None, Unset, int]): Highest price the property is expected to sell/rent for to set search price.
    """

    from_: Union[None, Unset, int] = UNSET
    to: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[None, Unset, int]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: Union[None, Unset, int]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_from_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        to = _parse_to(d.pop("to", UNSET))

        listings_v1_basic_price = cls(
            from_=from_,
            to=to,
        )

        return listings_v1_basic_price
