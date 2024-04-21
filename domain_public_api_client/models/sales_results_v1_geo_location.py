from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SalesResultsV1GeoLocation")


@_attrs_define
class SalesResultsV1GeoLocation:
    """Encapsulates the details of a geo location, long/lat

    Attributes:
        latitude (float): The property's Latitude
        longitude (float): The property's Longitude
    """

    latitude: float
    longitude: float

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        sales_results_v1_geo_location = cls(
            latitude=latitude,
            longitude=longitude,
        )

        return sales_results_v1_geo_location
