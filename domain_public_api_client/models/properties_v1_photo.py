import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.properties_v1_photo_image_type import PropertiesV1PhotoImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1Photo")


@_attrs_define
class PropertiesV1Photo:
    """DomainPropertyIdModelModelsPhoto

    Attributes:
        image_type (Union[Unset, PropertiesV1PhotoImageType]): Gets or Sets ImageType
        advert_id (Union[None, Unset, int]): Gets or Sets AdvertId
        date (Union[None, Unset, datetime.datetime]): Gets or Sets Date
        full_url (Union[None, Unset, str]): Gets or Sets FullUrl
        rank (Union[None, Unset, int]): Gets or Sets Rank
    """

    image_type: Union[Unset, PropertiesV1PhotoImageType] = UNSET
    advert_id: Union[None, Unset, int] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    full_url: Union[None, Unset, str] = UNSET
    rank: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        advert_id: Union[None, Unset, int]
        if isinstance(self.advert_id, Unset):
            advert_id = UNSET
        else:
            advert_id = self.advert_id

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        full_url: Union[None, Unset, str]
        if isinstance(self.full_url, Unset):
            full_url = UNSET
        else:
            full_url = self.full_url

        rank: Union[None, Unset, int]
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image_type is not UNSET:
            field_dict["imageType"] = image_type
        if advert_id is not UNSET:
            field_dict["advertId"] = advert_id
        if date is not UNSET:
            field_dict["date"] = date
        if full_url is not UNSET:
            field_dict["fullUrl"] = full_url
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _image_type = d.pop("imageType", UNSET)
        image_type: Union[Unset, PropertiesV1PhotoImageType]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = PropertiesV1PhotoImageType(_image_type)

        def _parse_advert_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        advert_id = _parse_advert_id(d.pop("advertId", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_full_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_url = _parse_full_url(d.pop("fullUrl", UNSET))

        def _parse_rank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rank = _parse_rank(d.pop("rank", UNSET))

        properties_v1_photo = cls(
            image_type=image_type,
            advert_id=advert_id,
            date=date,
            full_url=full_url,
            rank=rank,
        )

        return properties_v1_photo
