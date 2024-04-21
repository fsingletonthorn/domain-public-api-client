from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1GeoLocation")


@_attrs_define
class PreMarketV1GeoLocation:
    """Encapsulates the details of a geo location.

    Attributes:
        latitude (Union[Unset, float]): Latitude of the property.
        longitude (Union[Unset, float]): Longitude of the property.
    """

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        pre_market_v1_geo_location = cls(
            latitude=latitude,
            longitude=longitude,
        )

        return pre_market_v1_geo_location
