from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_point import (
        DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow:
    """Polygon which specifies geographical area for listing search

    Attributes:
        polygon (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint']]): List of points
            making polygon
        bounding_box (Union[Unset, List['DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint']]): Bounding box.
            Not used
    """

    polygon: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint"]] = UNSET
    bounding_box: Union[Unset, List["DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        polygon: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.polygon, Unset):
            polygon = []
            for polygon_item_data in self.polygon:
                polygon_item = polygon_item_data.to_dict()
                polygon.append(polygon_item)

        bounding_box: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bounding_box, Unset):
            bounding_box = []
            for bounding_box_item_data in self.bounding_box:
                bounding_box_item = bounding_box_item_data.to_dict()
                bounding_box.append(bounding_box_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if polygon is not UNSET:
            field_dict["polygon"] = polygon
        if bounding_box is not UNSET:
            field_dict["boundingBox"] = bounding_box

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_geo_point import (
            DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint,
        )

        d = src_dict.copy()
        polygon = []
        _polygon = d.pop("polygon", UNSET)
        for polygon_item_data in _polygon or []:
            polygon_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.from_dict(polygon_item_data)

            polygon.append(polygon_item)

        bounding_box = []
        _bounding_box = d.pop("boundingBox", UNSET)
        for bounding_box_item_data in _bounding_box or []:
            bounding_box_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint.from_dict(
                bounding_box_item_data
            )

            bounding_box.append(bounding_box_item)

        domain_public_adapter_web_api_models_v1_listings_commercial_geo_window = cls(
            polygon=polygon,
            bounding_box=bounding_box,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_geo_window.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_geo_window

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
