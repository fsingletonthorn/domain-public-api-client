from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1GeoLocation")


@_attrs_define
class ListingsV1GeoLocation:
    """Encapsulates the details of a geo location, long/lat

    Attributes:
        latitude (Union[None, Unset, float]): Latitude of the property
        longitude (Union[None, Unset, float]): Longitude of the property
    """

    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
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

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        listings_v1_geo_location = cls(
            latitude=latitude,
            longitude=longitude,
        )

        return listings_v1_geo_location
