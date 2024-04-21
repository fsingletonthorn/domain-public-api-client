from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreMarketV1CreateOrUpdateListingResponse")


@_attrs_define
class PreMarketV1CreateOrUpdateListingResponse:
    """Create or update pre-portal listing response.

    Attributes:
        id (str): Pre-portal listing ID.
    """

    id: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        pre_market_v1_create_or_update_listing_response = cls(
            id=id,
        )

        return pre_market_v1_create_or_update_listing_response
