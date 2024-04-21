import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsBusinessMedia:
    r"""Listing media

    Attributes:
        date_created (Union[Unset, datetime.datetime]): Not used
        image_url (Union[Unset, str]): Resource URL
        media_type (Union[Unset, str]): Media type: \"image\", \"video\"
        type (Union[Unset, str]): Type: \"youtube\", \"vimeo\", \"mp4\"
        video_url (Union[Unset, str]): Video URL
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    image_url: Union[Unset, str] = UNSET
    media_type: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    video_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        image_url = self.image_url

        media_type = self.media_type

        type = self.type

        video_url = self.video_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if type is not UNSET:
            field_dict["type"] = type
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        image_url = d.pop("imageUrl", UNSET)

        media_type = d.pop("mediaType", UNSET)

        type = d.pop("type", UNSET)

        video_url = d.pop("videoUrl", UNSET)

        domain_public_adapter_web_api_models_v1_listings_business_media = cls(
            date_created=date_created,
            image_url=image_url,
            media_type=media_type,
            type=type,
            video_url=video_url,
        )

        domain_public_adapter_web_api_models_v1_listings_business_media.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_business_media

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
