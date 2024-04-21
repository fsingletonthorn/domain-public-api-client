from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2PropertySummary")


@_attrs_define
class PropertyEnrichmentV2PropertySummary:
    """Property summary

    Attributes:
        property_type (Union[None, Unset, str]):
        bedrooms (Union[None, Unset, float]):
        bathrooms (Union[None, Unset, float]):
        car_spaces (Union[None, Unset, float]):
        land_size (Union[None, Unset, float]):
        building_size (Union[None, Unset, float]):
    """

    property_type: Union[None, Unset, str] = UNSET
    bedrooms: Union[None, Unset, float] = UNSET
    bathrooms: Union[None, Unset, float] = UNSET
    car_spaces: Union[None, Unset, float] = UNSET
    land_size: Union[None, Unset, float] = UNSET
    building_size: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        bedrooms: Union[None, Unset, float]
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: Union[None, Unset, float]
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        car_spaces: Union[None, Unset, float]
        if isinstance(self.car_spaces, Unset):
            car_spaces = UNSET
        else:
            car_spaces = self.car_spaces

        land_size: Union[None, Unset, float]
        if isinstance(self.land_size, Unset):
            land_size = UNSET
        else:
            land_size = self.land_size

        building_size: Union[None, Unset, float]
        if isinstance(self.building_size, Unset):
            building_size = UNSET
        else:
            building_size = self.building_size

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if car_spaces is not UNSET:
            field_dict["carSpaces"] = car_spaces
        if land_size is not UNSET:
            field_dict["landSize"] = land_size
        if building_size is not UNSET:
            field_dict["buildingSize"] = building_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_bedrooms(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_bathrooms(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_car_spaces(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        car_spaces = _parse_car_spaces(d.pop("carSpaces", UNSET))

        def _parse_land_size(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        land_size = _parse_land_size(d.pop("landSize", UNSET))

        def _parse_building_size(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        building_size = _parse_building_size(d.pop("buildingSize", UNSET))

        property_enrichment_v2_property_summary = cls(
            property_type=property_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            car_spaces=car_spaces,
            land_size=land_size,
            building_size=building_size,
        )

        return property_enrichment_v2_property_summary
