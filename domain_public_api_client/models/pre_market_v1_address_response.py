from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.pre_market_v1_state import PreMarketV1State

T = TypeVar("T", bound="PreMarketV1AddressResponse")


@_attrs_define
class PreMarketV1AddressResponse:
    """
    Attributes:
        street_number (str): Street (and possibly unit) number component of an address. E.g. 23, 1a, 11/1.
        street (str): Street name, e.g. Punt Road.
        suburb (str):
        state (PreMarketV1State): Australian states
        postcode (str):
        slug (str):
    """

    street_number: str
    street: str
    suburb: str
    state: PreMarketV1State
    postcode: str
    slug: str

    def to_dict(self) -> Dict[str, Any]:
        street_number = self.street_number

        street = self.street

        suburb = self.suburb

        state = self.state.value

        postcode = self.postcode

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "streetNumber": street_number,
                "street": street,
                "suburb": suburb,
                "state": state,
                "postcode": postcode,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street_number = d.pop("streetNumber")

        street = d.pop("street")

        suburb = d.pop("suburb")

        state = PreMarketV1State(d.pop("state"))

        postcode = d.pop("postcode")

        slug = d.pop("slug")

        pre_market_v1_address_response = cls(
            street_number=street_number,
            street=street,
            suburb=suburb,
            state=state,
            postcode=postcode,
            slug=slug,
        )

        return pre_market_v1_address_response
