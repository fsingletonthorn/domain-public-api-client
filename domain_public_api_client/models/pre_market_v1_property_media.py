from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.pre_market_v1_resource_type import PreMarketV1ResourceType

T = TypeVar("T", bound="PreMarketV1PropertyMedia")


@_attrs_define
class PreMarketV1PropertyMedia:
    """
    Attributes:
        resource_type (PreMarketV1ResourceType):
        url (str):
    """

    resource_type: PreMarketV1ResourceType
    url: str

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "resourceType": resource_type,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_type = PreMarketV1ResourceType(d.pop("resourceType"))

        url = d.pop("url")

        pre_market_v1_property_media = cls(
            resource_type=resource_type,
            url=url,
        )

        return pre_market_v1_property_media
