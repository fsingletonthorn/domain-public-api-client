from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.properties_v1_activity_boundary import PropertiesV1ActivityBoundary


T = TypeVar("T", bound="PropertiesV1RentalActivity")


@_attrs_define
class PropertiesV1RentalActivity:
    """
    Attributes:
        first (Union[Unset, PropertiesV1ActivityBoundary]):
        id (Union[None, Unset, int]): Gets or Sets Id
        last (Union[Unset, PropertiesV1ActivityBoundary]):
        property_type (Union[None, Unset, str]): Gets or Sets PropertyType
    """

    first: Union[Unset, "PropertiesV1ActivityBoundary"] = UNSET
    id: Union[None, Unset, int] = UNSET
    last: Union[Unset, "PropertiesV1ActivityBoundary"] = UNSET
    property_type: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if id is not UNSET:
            field_dict["id"] = id
        if last is not UNSET:
            field_dict["last"] = last
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.properties_v1_activity_boundary import PropertiesV1ActivityBoundary

        d = src_dict.copy()
        _first = d.pop("first", UNSET)
        first: Union[Unset, PropertiesV1ActivityBoundary]
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = PropertiesV1ActivityBoundary.from_dict(_first)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        _last = d.pop("last", UNSET)
        last: Union[Unset, PropertiesV1ActivityBoundary]
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = PropertiesV1ActivityBoundary.from_dict(_last)

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        properties_v1_rental_activity = cls(
            first=first,
            id=id,
            last=last,
            property_type=property_type,
        )

        return properties_v1_rental_activity
