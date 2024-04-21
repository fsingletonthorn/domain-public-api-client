import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.property_enrichment_v2_image_types import PropertyEnrichmentV2ImageTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2ImageUrl")


@_attrs_define
class PropertyEnrichmentV2ImageUrl:
    """Description of advertisement image

    Attributes:
        advert_id (Union[Unset, int]): Internal Domain advertisement identifier
        advert_date (Union[None, Unset, datetime.date]): The date when advertisement was created in YYYY-MM-DD format
        image_url (Union[Unset, str]): URL of image source
        image_type (Union[Unset, PropertyEnrichmentV2ImageTypes]):
    """

    advert_id: Union[Unset, int] = UNSET
    advert_date: Union[None, Unset, datetime.date] = UNSET
    image_url: Union[Unset, str] = UNSET
    image_type: Union[Unset, PropertyEnrichmentV2ImageTypes] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        advert_id = self.advert_id

        advert_date: Union[None, Unset, str]
        if isinstance(self.advert_date, Unset):
            advert_date = UNSET
        elif isinstance(self.advert_date, datetime.date):
            advert_date = self.advert_date.isoformat()
        else:
            advert_date = self.advert_date

        image_url = self.image_url

        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if advert_id is not UNSET:
            field_dict["advertId"] = advert_id
        if advert_date is not UNSET:
            field_dict["advertDate"] = advert_date
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if image_type is not UNSET:
            field_dict["imageType"] = image_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        advert_id = d.pop("advertId", UNSET)

        def _parse_advert_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                advert_date_type_0 = isoparse(data).date()

                return advert_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        advert_date = _parse_advert_date(d.pop("advertDate", UNSET))

        image_url = d.pop("imageUrl", UNSET)

        _image_type = d.pop("imageType", UNSET)
        image_type: Union[Unset, PropertyEnrichmentV2ImageTypes]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = PropertyEnrichmentV2ImageTypes(_image_type)

        property_enrichment_v2_image_url = cls(
            advert_id=advert_id,
            advert_date=advert_date,
            image_url=image_url,
            image_type=image_type,
        )

        return property_enrichment_v2_image_url
