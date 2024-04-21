from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1GeoCoordinate")


@_attrs_define
class PropertiesV1GeoCoordinate:
    """DomainPropertyIdModelModelsGeoCoordinate

    Attributes:
        lat (Union[None, Unset, float]): Gets or Sets Lat
        lon (Union[None, Unset, float]): Gets or Sets Lon
    """

    lat: Union[None, Unset, float] = UNSET
    lon: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lat: Union[None, Unset, float]
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lon: Union[None, Unset, float]
        if isinstance(self.lon, Unset):
            lon = UNSET
        else:
            lon = self.lon

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_lat(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lon(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lon = _parse_lon(d.pop("lon", UNSET))

        properties_v1_geo_coordinate = cls(
            lat=lat,
            lon=lon,
        )

        return properties_v1_geo_coordinate
