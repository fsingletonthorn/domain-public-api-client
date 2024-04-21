from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1Price")


@_attrs_define
class PreMarketV1Price:
    """
    Attributes:
        from_ (float): Lower end of the price range.
        to (float): Upper end of the price range.
        display_text (Union[None, Unset, str]): When provided this will be shown instead of the price range, e.g.:
            "Offers over $450K considered"
    """

    from_: float
    to: float
    display_text: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        display_text: Union[None, Unset, str]
        if isinstance(self.display_text, Unset):
            display_text = UNSET
        else:
            display_text = self.display_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if display_text is not UNSET:
            field_dict["displayText"] = display_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from")

        to = d.pop("to")

        def _parse_display_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_text = _parse_display_text(d.pop("displayText", UNSET))

        pre_market_v1_price = cls(
            from_=from_,
            to=to,
            display_text=display_text,
        )

        return pre_market_v1_price
