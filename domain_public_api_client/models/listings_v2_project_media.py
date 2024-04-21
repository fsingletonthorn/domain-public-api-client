from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v2_project_media_category import ListingsV2ProjectMediaCategory
from ..models.listings_v2_project_media_type import ListingsV2ProjectMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2ProjectMedia")


@_attrs_define
class ListingsV2ProjectMedia:
    """Project Media

    Attributes:
        category (Union[Unset, ListingsV2ProjectMediaCategory]): Gets or Sets Category
        type (Union[Unset, ListingsV2ProjectMediaType]): Gets or Sets Type
        url (Union[None, Unset, str]): Url
        description (Union[None, Unset, str]): Optional description
    """

    category: Union[Unset, ListingsV2ProjectMediaCategory] = UNSET
    type: Union[Unset, ListingsV2ProjectMediaType] = UNSET
    url: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, ListingsV2ProjectMediaCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ListingsV2ProjectMediaCategory(_category)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ListingsV2ProjectMediaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ListingsV2ProjectMediaType(_type)

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        listings_v2_project_media = cls(
            category=category,
            type=type,
            url=url,
            description=description,
        )

        return listings_v2_project_media
