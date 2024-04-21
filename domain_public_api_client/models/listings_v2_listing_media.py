from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.listings_v2_listing_media_category import ListingsV2ListingMediaCategory
from ..models.listings_v2_listing_media_type import ListingsV2ListingMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2ListingMedia")


@_attrs_define
class ListingsV2ListingMedia:
    """Encapsulates media associated with a Listing

    Attributes:
        url (str): The URL to the property media
        category (Union[Unset, ListingsV2ListingMediaCategory]): Gets or Sets Category
        type (Union[Unset, ListingsV2ListingMediaType]): Gets or Sets Type
    """

    url: str
    category: Union[Unset, ListingsV2ListingMediaCategory] = UNSET
    type: Union[Unset, ListingsV2ListingMediaType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "url": url,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        _category = d.pop("category", UNSET)
        category: Union[Unset, ListingsV2ListingMediaCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ListingsV2ListingMediaCategory(_category)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ListingsV2ListingMediaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ListingsV2ListingMediaType(_type)

        listings_v2_listing_media = cls(
            url=url,
            category=category,
            type=type,
        )

        return listings_v2_listing_media
